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
import GameTeam
import GameAction
import GameMap

class GamePlayerTeamaction(Base):

	# Table structure
	__tablename__ = 'games_players_teamactions'
	id = sqlalchemy.Column(sqlalchemy.types.Integer, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id'))
	team_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_teams.id'))
	action_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_actions.id'))
	map_id = sqlalchemy.Column(sqlalchemy.types.Integer, sqlalchemy.ForeignKey('games_maps.id'))
	count =  sqlalchemy.Column(sqlalchemy.types.Integer)

	# Relationships
	game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id])
	player = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[player_id])
	team = sqlalchemy.orm.relationship("GameTeam", foreign_keys=[team_id])
	action = sqlalchemy.orm.relationship("GameAction", foreign_keys=[action_id])
	map = sqlalchemy.orm.relationship("GameMap", foreign_keys=[map_id])
