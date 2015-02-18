# Standard Imports
import termcolor
import Queue
import threading
import timeit
import time


class LogParser(threading.Thread):

	def __init__(self, server, db):
		super(self.__class__,self).__init__()
		self.queue = Queue.Queue()
		self.server = server
		self.db = db
		self.go = True
		
	def run(self):
		while self.go:
			# Use a non-blocking fetch so we can always quit the loop
			buf = ""
			try:
				message = self.queue.get(False)
			except (Queue.Empty):
				time.sleep(0.1)
				continue
			# Start a timer
			start = timeit.default_timer()

			# Debug header
			buf += termcolor.colored("Processing Message from %s:%s" % (message[1][0], message[1][1]), 'green') +"\n"
	

	
			# Finished, create the end timer
			buf += termcolor.colored("Finished processing message : %.2fms" % (round((timeit.default_timer()-start)*1000, 2)), 'green') + "\n"

			#footer
			buf += termcolor.colored("--------------------------------------", 'green')

			#done
			self.queue.task_done()

			# Print
			print(buf)

	def put(self, data):
		self.queue.put(data)

	def stop(self):
		self.go = False;
