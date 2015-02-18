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
import GameAction
import GameMap

class GamePlayerAction(Base):

	# Table structure
	__tablename__ = 'games_players_actions'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id'))
	action_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_actions.id'))
	map_id = sqlalchemy.Column(sqlalchemy.types.Integer, sqlalchemy.ForeignKey('games_maps.id'))
	is_victim = sqlalchemy.Column(sqlalchemy.types.Boolean)
	count = sqlalchemy.Column(sqlalchemy.types.Integer)
	count_delta = sqlalchemy.Column(sqlalchemy.types.Integer)
	count_reset = sqlalchemy.Column(sqlalchemy.types.BigInteger)

	# Relationsips
	game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id])
	player = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[player_id]) 
	action = sqlalchemy.orm.relationship("GameAction", foreign_keys=[action_id])
	map = sqlalchemy.orm.relationship("GameMap", foreign_keys=[map_id])
