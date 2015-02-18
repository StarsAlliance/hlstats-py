# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()


class GameHeatmapConfig(Base):

	# Table structure
	__tablename__ = 'games_maps_heatmap_config'
	id = sqlalchemy.Column(sqlalchemy.types.Integer, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	map_id = sqlalchemy.Column(sqlalchemy.types.Integer, sqlalchemy.ForeignKey('games_maps.id'))
	xoffset = sqlalchemy.Column(sqlalchemy.types.Float)
	yoffset = sqlalchemy.Column(sqlalchemy.types.Float)
	flipx = sqlalchemy.Column(sqlalchemy.types.Boolean)
	flipy = sqlalchemy.Column(sqlalchemy.types.Boolean)
	rotate = sqlalchemy.Column(sqlalchemy.types.Boolean)
	days = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	brush = sqlalchemy.Column(sqlalchemy.String(length=5))
	scale = sqlalchemy.Column(sqlalchemy.types.Float)
	font = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	thumbw = sqlalchemy.Column(sqlalchemy.types.Float)
	thumbh = sqlalchemy.Column(sqlalchemy.types.Float)
	cropx1 = sqlalchemy.Column(sqlalchemy.types.Integer)
	cropy1 = sqlalchemy.Column(sqlalchemy.types.Integer)
	cropx2 = sqlalchemy.Column(sqlalchemy.types.Integer)
	cropy2 = sqlalchemy.Column(sqlalchemy.types.Integer)
