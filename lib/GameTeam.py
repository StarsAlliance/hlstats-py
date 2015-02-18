# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()

#HLStats-py imports

class GameTeam(Base):

	# Table structure
	__tablename__ = 'games_teams'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('game_id'))
	code = sqlalchemy.Column(sqlalchemy.String(length=64))
	name = sqlalchemy.Column(sqlalchemy.String(length=64))
	sort_order = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	picks = sqlalchemy.Column(sqlalchemy.types.Integer)
