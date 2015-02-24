#
# Imports MySQLdb and initiates the connection

from HLConfig import config
import MySQLdb
import MySQLdb.cursors

db = MySQLdb.connect(host=config.get('db', 'host'), user=config.get('db', 'user'), passwd=config.get('db', 'passwd'), db=config.get('db', 'name'), cursorclass=MySQLdb.cursors.DictCursor)

