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

class GamePlayerMap(Base):

	# Table structure
	__tablename__ = 'games_players_maps'
	id = sqlalchemy.Column(sqlalchemy.types.Integer, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id')) 
	map_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_maps.id'))
	rounds = sqlalchemy.Column(sqlalchemy.types.Integer)
	play_time = sqlalchemy.Column(sqlalchemy.types.Integer)
	kills = sqlalchemy.Column(sqlalchemy.types.Integer)
	team_kills = sqlalchemy.Column(sqlalchemy.types.Integer)
	deaths = sqlalchemy.Column(sqlalchemy.types.Integer)
	suicides = sqlalchemy.Column(sqlalchemy.types.Integer)
	shots = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	hits_head = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	hits_chest = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	hits_stomach = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	hits_leftarm = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	hits_leftleg = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	kpd = sqlalchemy.Column(sqlalchemy.types.Float)
	hpk = sqlalchemy.Column(sqlalchemy.types.Float)
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp())

	# Relationships
	game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id])
	player = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[player_id])
	map = sqlalchemy.orm.relationship("GameMap", foreign_keys=[map_id])
	weapons = sqlalchemy.orm.relationship("GamePlayerMapWeapon", backref=sqlalchemy.orm.backref("playermap", uselist=False), foreign_keys="GamePlayerMapWeapon.map_id")
