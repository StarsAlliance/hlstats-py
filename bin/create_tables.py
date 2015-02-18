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
import termcolor
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()


# Load the config file first
config = ConfigParser.ConfigParser()
config.read("%s/hlstats.ini" %(CFGDIR))

engine = sqlalchemy.create_engine(config.get('database', 'uri'))

from HLModels import *
print termcolor.colored("Creating Tables...", 'green')
Base.metadata.create_all(engine)
print termcolor.colored("Tables Created", 'green')
	
