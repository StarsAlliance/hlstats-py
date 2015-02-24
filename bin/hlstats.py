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

# Load Configuration
from HLConfig import config
from Engine import Engine
from Game import Game
from GamePlayer import GamePlayer
from GameServer import GameServer
from GameMap import GameMap
from Player import Player

# Load Log Server
from LogServer import LogServer

# Load Twisted
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from twisted.web import static, server

# Create the log server for UDP connections
logserver = LogServer()
logserver.config = config

# Install SIGINT handler
reactor.addSystemEventTrigger('before', 'shutdown', logserver.shutdown)

# Setup Log Server
reactor.listenUDP(27501, logserver)

# Set Up Garbage Collector for log server
gc = LoopingCall(logserver.gc)
gc.start(config.getint('timers', 'idle_server_search_interval'))

stats = LoopingCall(logserver.stats)
stats.start(config.getint('timers', 'print_stats'))


# Set up Model Garbage Collectors
def model_gc():
    Engine().garbageCollector()
    Game().garbageCollector()
    GamePlayer().garbageCollector()
    GameServer().garbageCollector()
    GameMap().garbageCollector()
    Player().garbageCollector()

modelgc = LoopingCall(model_gc)
modelgc.start(config.getint('timers', 'gc_interval'))


# Set up Model Flushing
def model_flush():
    Engine().flush()
    Game().flush()
    GamePlayer().flush()
    GameServer().flush()
    GameMap().flush()
    Player().flush()
modelflush = LoopingCall(model_flush)
modelflush.start(config.getint('timers', 'flush_interval'))

# Setup Web Server
root = static.File(WEBDIR)
reactor.listenTCP(config.getint('http', 'port'), server.Site(root))

# Run servers
reactor.run()
