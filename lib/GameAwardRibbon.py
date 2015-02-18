# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()

#HLStats-py imports


class GameAwardRibbon(Base):

	# Table structure
	__tablename__ = 'games_awards_ribbons'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	award_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_awards.id'))
	special = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	name = sqlalchemy.Column(sqlalchemy.String(length=50))
	count = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	image = sqlalchemy.Column(sqlalchemy.String(length=50))

	# Relationships
