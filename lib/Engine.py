# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()

#HLStats-py imports
import Game

class Engine(Base):

	# Table structure
	__tablename__ = 'engines'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	code = sqlalchemy.Column(sqlalchemy.String(length=12))
	name = sqlalchemy.Column(sqlalchemy.String(length=45))
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, server_default=sqlalchemy.func.unix_timestamp())

	# Relationships
	games = sqlalchemy.orm.relationship("Game", backref="engine", foreign_keys="Game.engine_id")
