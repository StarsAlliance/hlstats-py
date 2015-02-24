import ConfigParser
import os

APPDIR = os.path.dirname(os.path.realpath(__file__))
BASEDIR = os.path.dirname(APPDIR)
LIBDIR = "%s/lib" % (BASEDIR)
CFGDIR = "%s/etc" % (BASEDIR)
WEBDIR = "%s/htdocs" % (BASEDIR)

config = ConfigParser.ConfigParser()
config.read("%s/hlstats.ini" %(CFGDIR))