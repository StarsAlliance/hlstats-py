# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()

# HLStats-py imports
import Game
import GamePlayer
import GameAward

class GamePlayerAward(Base):

	# Table structure
	__tablename__ = 'games_players_awards'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id'))
	award_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_awards.id'))
	date = sqlalchemy.Column(sqlalchemy.types.Date)
	count = sqlalchemy.Column(sqlalchemy.types.SmallInteger)

	# Relationsips
	game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id])
	player = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[player_id]) 
	award = sqlalchemy.orm.relationship("GameAward", foreign_keys=[award_id])
