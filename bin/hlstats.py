#!/usr/bin/python
#
# HLStats-py Package
#

# Standard Imports
import sys
import os

# Get bin directory
APPDIR = os.path.dirname(os.path.realpath(__file__))
BASEDIR = os.path.dirname(APPDIR)
LIBDIR = "%s/lib" % (BASEDIR)
CFGDIR = "%s/etc" % (BASEDIR)
WEBDIR = "%s/htdocs" % (BASEDIR)
sys.path.append(LIBDIR)

# Other Imports
import ConfigParser
from twisted.internet import reactor
from twisted.web import static, server

# Load the config file first
config = ConfigParser.ConfigParser()
config.read("%s/hlstats.ini" %(CFGDIR))
# Connect to the database server
import sqlalchemy
import sqlalchemy.orm

db = sqlalchemy.create_engine(config.get('database', 'uri'))
session = sqlalchemy.orm.scoped_session(sqlalchemy.orm.sessionmaker(db, autoflush=True, autocommit=True))

# HLStats imports
from LogServer import LogServer

# Setup Web Server
root = static.File(WEBDIR)
reactor.listenTCP(config.get('web', 'port'), server.Site(root))

# Setup Log Server
reactor.listenUDP(27501, LogServerFactory(db))

# Run all
reactor.run()
