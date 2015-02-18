# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()

#HLStats-py imports
import GameTeam

class GameAction(Base):

	# Table structure
	__tablename__ = 'games_actions'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	code = sqlalchemy.Column(sqlalchemy.String(length=64))
	name = sqlalchemy.Column(sqlalchemy.String(length=45))
	player_reward = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	team_reward = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	team_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_teams.id'))
	affects_player = sqlalchemy.Column(sqlalchemy.types.Boolean)
	affects_victim = sqlalchemy.Column(sqlalchemy.types.Boolean)
	affects_team = sqlalchemy.Column(sqlalchemy.types.Boolean)
	count = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp())

	# Relationships
	team = sqlalchemy.orm.relationship("GameTeam", uselist=False, foreign_keys=[team_id])
