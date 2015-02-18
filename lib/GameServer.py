# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()

#HLStats-py imports
import GameMap
import GameServerPlayer

class GameServer(Base):

	# Table structure
	__tablename__ = 'games_servers'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('game.id'))
	name = sqlalchemy.Column(sqlalchemy.String(length=45))
	hostname = sqlalchemy.Column(sqlalchemy.String(length=127))
	port = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	hostname_public = sqlalchemy.Column(sqlalchemy.String(length=45))
	map_id = sqlalchemy.Column(sqlalchemy.types.Integer, sqlalchemy.ForeignKey('map.id'))
	rcon_password = sqlalchemy.Column(sqlalchemy.String(length=45))
	sort_order = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
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
	act_players = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	max_players = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	fps = sqlalchemy.Column(sqlalchemy.types.Float)
	uptime = sqlalchemy.Column(sqlalchemy.types.Integer)
	bombs_planeted = sqlalchemy.Column(sqlalchemy.types.Integer)
	bombs_defused = sqlalchemy.Column(sqlalchemy.types.Integer)
	ct_wins = sqlalchemy.Column(sqlalchemy.types.Integer)
	ts_wins	 = sqlalchemy.Column(sqlalchemy.types.Integer)
	ct_shots = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	ct_hits = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	ts_shots = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	ts_hits = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp())

	# Relationships
	players = sqlalchemy.orm.relationship("GameServerPlayer", backref=sqlalchemy.orm.backref("server", uselist=False))
	map = global_winner = sqlalchemy.orm.relationship("GameMap", uselist=False, foreign_keys=[map_id])		
