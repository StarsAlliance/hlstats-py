# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()

#HLStats-py imports
import GamePlayerAction
import GamePlayerAlias
import GamePlayerAward
import GamePlayerAwardRibbon
import GamePlayerMap
import GamePlayerMapWeapon
import GamePlayerTeamaction
import GamePlayerWeapon

class GamePlayer(Base):

	# Table structure
	__tablename__ = 'games_players'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	player_id
	game_id
	name
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
	skill = sqlalchemy.Column(sqlalchemy.types.Integer)
	kill_streak = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	death_streak = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	ip =  sqlalchemy.Column(sqlalchemy.types.String(length=15))
	rank_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	clan_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	kills_delta = sqlalchemy.Column(sqlalchemy.types.Integer)
	deaths_delta = sqlalchemy.Column(sqlalchemy.types.Integer)
	suicides_delta = sqlalchemy.Column(sqlalchemy.types.Integer)
	team_kills_delta = sqlalchemy.Column(sqlalchemy.types.Integer)
	play_time_delta = sqlalchemy.Column(sqlalchemy.types.Integer)
	kill_streak_delta = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	dealth_streak_delta = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	skill_delta = sqlalchemy.Column(sqlalchemy.types.Integer)
	delta_reset = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	latency = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	latency_weight = sqlalchemy.Column(sqlalchemy.types.Integer)
	latency_delta = sqlalchemy.Column(sqlalchemy.types.Integer)
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp())

	# Relationships
	actions = sqlalchemy.orm.relationship("GamePlayerAction", backref=sqlalchemy.orm.backref("player", uselist=False), foreign_keys="GamePlayerAction.player_id")
	aliases = sqlalchemy.orm.relationship("GamePlayerAlias", backref=sqlalchemy.orm.backref("player", uselist=False), foreign_keys="GamePlayerAlias.player_id")
	awards = sqlalchemy.orm.relationship("GamePlayerAward", backref=sqlalchemy.orm.backref("player", uselist=False), foreign_keys="GamePlayerAward.player_id")
	awards_ribbons = sqlalchemy.orm.relationship("GamePlayerAwardRibbon", backref=sqlalchemy.orm.backref("player", uselist=False), foreign_keys="GamePlayerAwardRibbon.player_id") 
	maps = sqlalchemy.orm.relationship("GamePlayerMap", backref=sqlalchemy.orm.backref("player", uselist=False), foreign_keys="GamePlayerMap.player_id")
	maps_weapons = sqlalchemy.orm.relationship("GamePlayerMapWeapon", backref=sqlalchemy.orm.backref("player", uselist=False), foreign_keys="GamePlayerMapWeapon.player_id")
	roles =  sqlalchemy.orm.relationship("GamePlayerRole", backref=sqlalchemy.orm.backref("player", uselist=False), foreign_keys="GamePlayerRole.player_id") 
	teamactions =  sqlalchemy.orm.relationship("GamePlayerTeamaction", backref=sqlalchemy.orm.backref("player", uselist=False), foreign_keys="GamePlayerTeamAction.player_id")
	weapons = sqlalchemy.orm.relationship("GamePlayerWeapon", backref=sqlalchemy.orm.backref("player", uselist=False), foreign_keys="GamePlayerWeapon.player_id") 
