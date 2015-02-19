# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time
import termcolor

from HLModels import *


def parse(server, message):
	print "Parsing with %s" % __name__		
