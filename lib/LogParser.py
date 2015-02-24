# Standard Imports
import termcolor
import Queue
import threading
import time
import timeit

from Engine import Engine
from GameServer import GameServer
from Game import Game
from Player import Player
from GamePlayer import GamePlayer
from GameMap import GameMap
from GameWeapon import GameWeapon


class Parser(threading.Thread):

    def __init__(self, address):
        super(Parser, self).__init__()
        self.address = address
        self.queue = Queue.Queue()
        self.go = True
        self.time = 0.0
        self.startup = timeit.default_timer()
        self.last_message = time.time()
        self.server = GameServer()
        self.game = Game()
        self.engine = Engine()
        self.player = Player()
        self.game_player = GamePlayer()
        self.game_map = GameMap()
        self.game_weapon = GameWeapon()
        self.cur_server = self.server.get(address=self.address)
        self.cur_game = self.game.get(id=self.cur_server['game_id'])

    def run(self):
        start = timeit.default_timer()
        self.sync()
        # Process the messages
        while self.go:
            self.last_message = time.time()
            # Use a non-blocking fetch so we can always quit the loop
            buf = ""
            try:
                try:
                    message = self.queue.get(False)
                except (KeyboardInterrupt):
                    return
                except (Queue.Empty):
                    try:
                        time.sleep(0.1)
                        continue
                    except:
                        pass
            except:
                pass

            # Start a timer
            start = timeit.default_timer()

            buf += self.parse(message)
            # Finished, create the end timer
            self.time += (timeit.default_timer()-start)

            #done
            self.queue.task_done()
            # Print
            if buf:
                print(buf)

    def put(self, data):
        self.queue.put(data)

    def stop(self):
        elapsed = (timeit.default_timer()-self.startup)
        print termcolor.colored(
            "Thread was running for %10.4f seconds. %10.4f was spent processing or blocked. (%6.2f%%): %s" %
            (round(elapsed, 4), round(self.time, 4), round((self.time / elapsed * 100), 2), self.address), 'red')
        self.go = False
    
    def stats(self):
        elapsed = (timeit.default_timer()-self.startup)
        print termcolor.colored(
            "Thread running for %10.4f seconds. %10.4f has been spent processing or blocked. (%6.2f%%): %s" %
            (round(elapsed, 4), round(self.time, 4), round((self.time / elapsed * 100), 2), self.address), 'red')
        
    def parse(self, message):
        return ""

    def getLastMessageTime(self):
        return self.last_message

