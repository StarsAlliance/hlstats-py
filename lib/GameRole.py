# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()

#HLStats-py imports

class GameRole(Base):

	# Table structure
	__tablename__ = 'games_roles'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('game_id'))
	code = sqlalchemy.Column(sqlalchemy.String(length=64))
	name = sqlalchemy.Column(sqlalchemy.String(length=64))
	picks = sqlalchemy.Column(sqlalchemy.types.Integer)
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
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp())
