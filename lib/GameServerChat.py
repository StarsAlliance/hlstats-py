# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()

# HLStats-py Imports
import Game
import GamePlayer
import GameMap
import GameServer

class GameServerChat(Base):

	# Table structure
	__tablename__ = 'games_servers_chats'
	id = sqlalchemy.Column(sqlalchemy.types.Integer, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	server_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_servers.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id')) 
	map_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_maps.id'))
	mode = sqlalchemy.Column(sqlalchemy.types.Boolean)
	message = sqlalchemy.Column(sqlalchemy.types.Text)
	date = sqlalchemy.Column(sqlalchemy.types.BigInteger)

	# Relationships
	game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id])
	player = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[player_id])
	map = sqlalchemy.orm.relationship("GameMap", foreign_keys=[map_id])
	server = sqlalchemy.orm.relationship("GameServer", foreign_keys=[server_id])
