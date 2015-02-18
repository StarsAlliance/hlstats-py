# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()


class GameHeatmapData(Base):

	# Table structure
	__tablename__ = 'games_maps_heatmap_data'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	map_id = sqlalchemy.Column(sqlalchemy.types.Integer, sqlalchemy.ForeignKey('games_maps.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id'))
	victim_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id'))
	action_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_actions.id'))
	player_x = sqlalchemy.Column(sqlalchemy.types.Integer)
	player_y = sqlalchemy.Column(sqlalchemy.types.Integer)
	victim_x = sqlalchemy.Column(sqlalchemy.types.Integer)
	victim_y = sqlalchemy.Column(sqlalchemy.types.Integer)
	timestamp = sqlalchemy.Column(sqlalchemy.types.BigInteger)

	# Relationsips
	player = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[player_id]) 
	victim = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[victim_id])
	action = sqlalchemy.orm.relationship("GameAction", foreign_keys=[action_id])
