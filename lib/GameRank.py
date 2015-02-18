# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()

#HLStats-py imports


class GameRank(Base):

	# Table structure
	__tablename__ = 'games_ranks'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	kills_min = sqlalchemy.Column(sqlalchemy.types.bigInteger)
	kills_max = sqlalchemy.Column(sqlalchemy.types.bigInteger)
	name = sqlalchemy.Column(sqlalchemy.String(length=50))
	image = sqlalchemy.Column(sqlalchemy.String(length=50))

	# Relationships
