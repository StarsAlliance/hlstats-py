# Standard Imports

import twisted.internet.protocol
import termcolor
import sqlalchemy.orm

# HLStats-py Imports
import LogParser
from GameServer import GameServer

class LogServer(twisted.internet.protocol.DatagramProtocol):
	
	def startProtocol(self):
		self.session = sqlalchemy.orm.scoped_session(self.factory.db)
		self.parsers = {}

	def datagramReceived(self, data, (host, port)):
		port = str(port)
		# Check to see if we have a thread in the 
		# 	background already running for this server
		if host not in self.parsers:
			self.parsers[host] = {}
		if port not in self.parsers[host]:
			# Look up the game server
			# Spawn a log processor for that game server
			self.parsers[host][port] = LogParser.LogParser(server)
			self.parsers[host][port].daemon = True
			self.parsers[host][port].start()
		
		# Append message to the queue for the appropriate server
		self.parsers[host][port].put((data, (host, port)))

class LogServerFactory(twisted.internet.protocol.Factory):
	protocol = LogServer
	def __init__(self, db):
		self.db = db
	
