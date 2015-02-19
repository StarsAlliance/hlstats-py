# Standard Imports
import os
import twisted.internet.protocol
import termcolor
import sqlalchemy
import sqlalchemy.orm

# HLStats-py Imports
import LogParser
from HLModels import *

class LogServer(twisted.internet.protocol.DatagramProtocol):
	
	def startProtocol(self):
		self.parsers = {}
		self.db = sqlalchemy.create_engine(self.config.get('database', 'uri'), echo=True)
		self.session = sqlalchemy.orm.scoped_session(sqlalchemy.orm.sessionmaker(self.db))

	def datagramReceived(self, data, (host, port)):
		port = str(port)

		# Check to see if we have a thread in the 
		# 	background already running for this server
		if host not in self.parsers:
			self.parsers[host] = {}
		if port not in self.parsers[host]:
			# Look up the game server
			server = self.session.query(GameServer).filter_by(hostname=host, port=port).first()
			# Check to make sure we support this server
			if server is None:
				print termcolor.colored("Message from Unknown Server (%s:%s), Ignoring" % (host, port), 'yellow')
				self.parsers[host][port] = None
				return
			# Spawn a processor for this server
			self.parsers[host][port] = LogParser.LogParser(server, self.db)
			self.parsers[host][port].daemon = True
			self.parsers[host][port].start()
		
		# Append message to the queue for the appropriate server
		if self.parsers[host][port] is not None:
			self.parsers[host][port].put((data, (host, port)))
