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
import GameWeapon

class GamePlayerWeapon(Base):

	# Table structure
	__tablename__ = 'games_players_weapons'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id')) 
	weapon_id = sqlalchemy.Column(sqlalchemy.types.Integer, sqlalchemy.ForeignKey('games_weapons.id'))
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
	kills_delta = sqlalchemy.Column(sqlalchemy.types.Integer)
	hits_head_delta = sqlalchemy.Column(sqlalchemy.types.Integer)
	delta_reset = sqlalchemy.Column(sqlalchemy.types.BigInteger)

	# Relationships
	game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id])
	player = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[player_id])
	weapon = sqlalchemy.orm.relationship("GameWeapon", foreign_keys=[weapon_id])
