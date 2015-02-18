# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()

#HLStats-py imports
import GameAction
import GameAward
import GameAwardRibbon
import GameClan
import GameMap
import GameHeatmapConfig
import GameHeatmapData
import GamePlayer
import GameRank
import GameRole
import GameServer
import GameTeam
import GameWeapon

class Game(Base):

	# Table structure
	__tablename__ = 'games'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	code = sqlalchemy.Column(sqlalchemy.String(length=64))
	name = sqlalchemy.Column(sqlalchemy.String(length=45))
	engine_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('engine.id'))
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
	hits_rightleg = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	kpd = sqlalchemy.Column(sqlalchemy.types.Float)
	hpk = sqlalchemy.Column(sqlalchemy.types.Float)
	hidden  = sqlalchemy.Column(sqlalchemy.types.Boolean)
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp())

	# Relationships
	actions = sqlalchemy.orm.relationship("GameAction", backref=sqlalchemy.orm.backref("game", uselist=False))
	awards = sqlalchemy.orm.relationship("GameAward", backref=sqlalchemy.orm.backref("game", uselist=False))
	awards_ribbons = sqlalchemy.orm.relationship("GameAwardRibbon", backref=sqlalchemy.orm.backref("game", uselist=False))
	clans = sqlalchemy.orm.relationship("GameClan", backref=sqlalchemy.orm.backref("game", uselist=False))
	maps = sqlalchemy.orm.relationship("GameMap", backref=sqlalchemy.orm.backref("game", uselist=False))
	maps_heatmap_config = sqlalchemy.orm.relationship("GameHeatmapConfig", backref=sqlalchemy.orm.backref("game", uselist=False))
	maps_heatmap_data = sqlalchemy.orm.relationship("GameHeatmapData", backref=sqlalchemy.orm.backref("game", uselist=False))
	players = sqlalchemy.orm.relationship("GamePlayer", backref=sqlalchemy.orm.backref("game", uselist=False)) 
	ranks = sqlalchemy.orm.relationship("GameRank", backref=sqlalchemy.orm.backref("game", uselist=False))
	roles = sqlalchemy.orm.relationship("GameRole", backref=sqlalchemy.orm.backref("game", uselist=False))
	servers = sqlalchemy.orm.relationship("GameServer", backref=sqlalchemy.orm.backref("game", uselist=False))
	teams = sqlalchemy.orm.relationship("GameTeam", backref=sqlalchemy.orm.backref("game", uselist=False))
	weapons = sqlalchemy.orm.relationship("GameWeapon", backref=sqlalchemy.orm.backref("game", uselist=False))
