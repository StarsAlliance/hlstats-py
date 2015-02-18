# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()

#HLStats-py imports
import GameRole
import GameTeam
import GameClan

class GameServerPlayer(Base):

	# Table structure
	__tablename__ = 'games_servers_players'

	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	server_id = sqlalchemy.Column(sqlalchemy.types.Integer) 
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id'))
	role_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_roles.id'))
	team_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_teams.id'))
	connected = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	skill_started = sqlalchemy.Column(sqlalchemy.types.Integer)
	skill_change = sqlalchemy.Column(sqlalchemy.types.Integer)
	is_dead = sqlalchemy.Column(sqlalchemy.Boolean)
	has_bomb = sqlalchemy.Column(sqlalchemy.Boolean)
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
	kill_streak = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	death_streak = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	latency = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	ip = sqlalchemy.Column(sqlalchemy.types.String(length=15))
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp())

	# Relationships
	role = sqlalchemy.orm.relationship("GameRole", backref=sqlalchemy.orm.backref("player", uselist=False), foreign_keys=[role_id])
	team = sqlalchemy.orm.relationship("GameTeam", backref=sqlalchemy.orm.backref("player", uselist=False), foreign_keys=[team_id])
	clan = sqlalchemy.orm.relationship("GameClan", backref=sqlalchemy.orm.backref("player", uselist=False), foreign_keys=[clan_id])
