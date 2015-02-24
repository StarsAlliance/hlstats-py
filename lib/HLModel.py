from Database import db
from Singleton import Singleton
import threading
import time
from HLConfig import config
import copy

class HLModel:
    dbcon = db
    db = db.cursor()
    updateLock = threading.Lock()

    def get(self, getone=True, doLock=True, nocache=False, **kwargs):
        # Acquire object lock
        if self.locking and doLock:
            self.updateLock.acquire()
        # Try and see if we are in the cache
        search_values = []
        if not nocache:
            if len(kwargs) == 1 and "id" in kwargs:
                if kwargs["id"] in self.cache:
                    if self.locking and doLock:
                        self.updateLock.release()
                    return self.cache[kwargs["id"]]
            for key, value in kwargs.iteritems():
                # if this isn't an indexed key we can't return a cache
                if key not in self.index_keys:
                    # break the loop
                    search_values = []
                    break
                # if this value isn't in this cache
                if key not in self.index or value not in self.index[key]:
                    # break
                    search_values = []
                    break
                #if str(self.__class__) == "<class 'GamePlayer.GamePlayer'>":
                #    print "Appending: " + str(self.index[key][value])
                search_values.append(self.index[key][value])
            if search_values:
                #if str(self.__class__) == "<class 'GamePlayer.GamePlayer'>":
                #    print "Intersection of " + str(search_values)
                cacheKeys = set.intersection(*search_values)
                if cacheKeys:
                    result = [self.cache[x] for x in cacheKeys]
                    if self.locking and doLock:
                        self.updateLock.release()
                    if getone:
                        return result[0]
                    else:
                        return result
        # Base of query
        query = "SELECT * FROM `"+self.table+"`"
        # Start looping through arguments
        subquery = []
        for key, value in kwargs.iteritems():
            subquery.append(" `"+key+"` = %s")
        if subquery:
            query += " WHERE " + " AND ".join(subquery)
        if getone:
            query += " LIMIT 1"
        if self.debug:
            print "SQL DB RUNNING QUERY: %s - %s" % (query, str(tuple(kwargs.values())))
        self.db.execute(query, tuple(kwargs.values()))
        if self.db.rowcount:
            results = self.db.fetchall()
            if getone:
                results = self.cacheResult(results[0])
            else:
                results = self.cacheResults(results)
        else:
            results = self.cacheNoneResult(**kwargs)
        if self.locking and doLock:
            self.updateLock.release()
        return results

    def cacheNoneResult(self, **kwargs):
        # We are going to cache the None result
        for key in self.index_keys:
            if key in kwargs:
                if key not in self.index:
                    self.index[key] = {}
                if kwargs[key] not in self.index[key]:
                    self.index[key][kwargs[key]] = set()
                for k, v in self.index[key].iteritems():
                    self.index[key][k].discard(None)
                self.index[key][kwargs[key]].add(None)
        self.cache[None] = None
        return None

    def cacheResult(self, result):
        # If the result is None
        # Append meta to the dict
        result['_updated'] = result['_flushed'] = time.time()
        # Put the item in the cache using the row id as a key
        self.cache[result["id"]] = result
        # Loop through the indexable keys
        for key in self.index_keys:
            # If our indexable key is in the result
            if key in result:
                # If the index doesn't exist for this key
                if key not in self.index:
                    # Create a dict of key values to put a value:set dict in
                    self.index[key] = {}
                # If the value doesn't exist for this index_key
                if result[key] not in self.index[key]:
                    # Create a set of distinct row ids
                    self.index[key][result[key]] = set()
                # Loop through all of the values in this index key and discard
                #   our row id if it is present anywhere else
                for k, v in self.index[key].iteritems():
                    self.index[key][k].discard(result["id"])
                # Now add the result id to the cache key
                self.index[key][result[key]].add(result["id"])
        # return the pointer to the cache result
        return self.cache[result["id"]]

    def cacheResults(self, results):
        # List of return results
        return_results = []
        # Loop through the results
        for key, value in results.iteritems():
            # Cache each one individually
            return_results = append(self.cacheResult)
        # Return the results
        return return_results

    def create(self, **kwargs):
        if self.locking:
            self.updateLock.acquire()
        query = "INSERT INTO `"+self.table + "` SET "
        subquery = []
        for key, value in kwargs.iteritems():
            subquery.append(" `"+key+"` = %s")
        query += ", ".join(subquery)
        if self.debug:
            print "SQL DB RUNNING QUERY: %s - %s" % (query, str(tuple(kwargs.values())))
        self.db.execute(query, tuple(kwargs.values()))
        # We need to cachebust all None results
        for key in self.index_keys:
            if key in self.index:
                for k2, v2 in self.index[key].items():
                    self.index[key][k2].discard(None)
        # Retrieve and cache the result
        result = self.get(doLock=False, id=self.db.lastrowid)
        if self.locking:
            self.updateLock.release()
        return result

    def getOrCreate(self, **kwargs):
        result = self.get(**kwargs)
        if result is None:
            return self.create(**kwargs)
        return result

    def garbageCollector(self):
        if self.locking:
            self.updateLock.acquire()
        prune_time = time.time() - config.getint('timers', 'gc_age')
        for index, value in self.cache.items():
            if self.cache[index] is not None and self.cache[index]["_flushed"] >= self.cache[index]["_updated"] and self.cache[index]["_flushed"] < prune_time:
                for index_key in self.index_keys:
                    if index_key in self.index and index_key in self.cache[index] and self.cache[index][index_key] in self.index[index_key]:
                        self.index[index_key][self.cache[index][index_key]].discard(index)
                del(self.cache[index])
        if self.locking:
            self.updateLock.release()

    def getCacheCount(self):
        return len(self.cache)

    def update(self, id, **kwargs):
        if self.locking:
            self.updateLock.acquire()
        if id not in self.cache:
            self.get(doLock=False, id=id)
            if id not in self.cache:
                if self.locking:
                    self.updateLock.acquire()
                return False
        old_values = copy.deepcopy(self.cache[id])
        for key, value in kwargs.items():
            self.cache[id][key] = value
            if self.cache[id][key] != old_values[key]:
                self.cache[id]["_updated"] = time.time()
                if key not in self.index_keys:
                    continue
                # Cache bust the old value
                if key in self.index and old_values[key] in self.index[key]:
                    self.index[key][old_values[key]].discard(id)
                # Put in the new value
                if key not in self.index:
                    self.index[key] = {}
                if value not in self.index[key]:
                    self.index[key][value] = set()
                self.index[key][value].add(id)
        if self.locking:
            self.updateLock.release()

    def flush(self):
        if self.locking:
            self.updateLock.acquire()
        now = time.time()
        for key in self.cache.keys():
            if self.cache[key] is None:
                continue
            if self.cache[key]["_updated"] > self.cache[key]["_flushed"]:
                query = "UPDATE `"+self.table + "` SET "
                subquery = []
                subquery_values = []
                for item, value in self.cache[key].items():
                    if item[:1] == "_" or item == "id":
                        continue
                    subquery.append(" `"+item+"` = %s")
                    subquery_values.append(value)
                query += ", ".join(subquery) + " WHERE `id` = %s"
                subquery_values.append(key)
                self.db.execute(query, tuple(subquery_values))
                self.dbcon.commit()
                self.cache[key]["_flushed"] = now
        if self.locking:
            self.updateLock.release()

