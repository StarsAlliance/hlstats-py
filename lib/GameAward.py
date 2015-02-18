# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()

#HLStats-py imports
import GamePlayer
import GameAwardRibbon

class GameAward(Base):

	# Table structure
	__tablename__ = 'games_awards'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	code = sqlalchemy.Column(sqlalchemy.String(length=128))
	name = sqlalchemy.Column(sqlalchemy.String(length=128))
	verb = sqlalchemy.Column(sqlalchemy.String(length=128))
	type = sqlalchemy.Column(sqlalchemy.String(length=1))
	global_winner_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('players.id'))
	global_count = sqlalchemy.Column(sqlalchemy.types.Integer)	
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp())

	# Relationships
	global_winner = sqlalchemy.orm.relationship("GamePlayer", uselist=False, foreign_keys=[global_winner_id])
	ribbons = sqlalchemy.orm.relationship("GameAwardRibbon") 
