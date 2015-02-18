# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time

# Set up SQLAlchemy
Base = sqlalchemy.ext.declarative.declarative_base()

class Engine(Base):

	# Table structure
	__tablename__ = 'engines'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	code = sqlalchemy.Column(sqlalchemy.String(length=12))
	name = sqlalchemy.Column(sqlalchemy.String(length=45))
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())

	# Relationships
	games = sqlalchemy.orm.relationship("Game", backref="engine", foreign_keys="Game.engine_id")

class Player(Base):

	# Table structure
	__tablename__ = 'players'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	unique_id = sqlalchemy.Column(sqlalchemy.String(length=32))
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
	kill_streak = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	death_streak = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())

	# Relationships
	players = sqlalchemy.orm.relationship("GamePlayer", backref=sqlalchemy.orm.backref("player", uselist=False), foreign_keys="GamePlayer.player_id")

class Game(Base):

	# Table structure
	__tablename__ = 'games'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	code = sqlalchemy.Column(sqlalchemy.String(length=64))
	name = sqlalchemy.Column(sqlalchemy.String(length=45))
	engine_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('engines.id'))
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
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())

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

class GameTeam(Base):

	# Table structure
	__tablename__ = 'games_teams'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	code = sqlalchemy.Column(sqlalchemy.String(length=64))
	name = sqlalchemy.Column(sqlalchemy.String(length=64))
	sort_order = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	picks = sqlalchemy.Column(sqlalchemy.types.Integer)

class GameRole(Base):

	# Table structure
	__tablename__ = 'games_roles'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
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
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())

class GameRank(Base):

	# Table structure
	__tablename__ = 'games_ranks'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	kills_min = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	kills_max = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	name = sqlalchemy.Column(sqlalchemy.String(length=50))
	image = sqlalchemy.Column(sqlalchemy.String(length=50))

	# Relationships

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
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())

	# Relationships
	team = sqlalchemy.orm.relationship("GameTeam", uselist=False, foreign_keys=[team_id])

class GamePlayer(Base):

	# Table structure
	__tablename__ = 'games_players'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('players.id'))
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	name = sqlalchemy.Column(sqlalchemy.types.String(length=45))
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
	clan_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_clans.id'))
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
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())

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

class GameAward(Base):

	# Table structure
	__tablename__ = 'games_awards'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	code = sqlalchemy.Column(sqlalchemy.String(length=128))
	name = sqlalchemy.Column(sqlalchemy.String(length=128))
	verb = sqlalchemy.Column(sqlalchemy.String(length=128))
	type = sqlalchemy.Column(sqlalchemy.String(length=1))
	global_winner_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id'))
	global_count = sqlalchemy.Column(sqlalchemy.types.Integer)	
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())

	# Relationships
	global_winner = sqlalchemy.orm.relationship("GamePlayer", uselist=False, foreign_keys=[global_winner_id])
	ribbons = sqlalchemy.orm.relationship("GameAwardRibbon") 

class GameAwardRibbon(Base):

	# Table structure
	__tablename__ = 'games_awards_ribbons'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	award_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_awards.id'))
	special = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	name = sqlalchemy.Column(sqlalchemy.String(length=50))
	count = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	image = sqlalchemy.Column(sqlalchemy.String(length=50))

	# Relationships

class GameWeapon(Base):

	# Table structure
	__tablename__ = 'games_weapons'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	code = sqlalchemy.Column(sqlalchemy.types.String(length=45))
	name = sqlalchemy.Column(sqlalchemy.types.String(length=45))
	modifier = sqlalchemy.Column(sqlalchemy.types.Float)
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
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())

	game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id])

class GameMap(Base):

	# Table structure
	__tablename__ = 'games_maps'
	id = sqlalchemy.Column(sqlalchemy.types.Integer, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	code = sqlalchemy.Column(sqlalchemy.String(length=64))
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
	bombs_planeted = sqlalchemy.Column(sqlalchemy.types.Integer)
	bombs_defused = sqlalchemy.Column(sqlalchemy.types.Integer)
	ct_wins = sqlalchemy.Column(sqlalchemy.types.Integer)
	ts_wins	 = sqlalchemy.Column(sqlalchemy.types.Integer)
	ct_shots = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	ct_hits = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	ts_shots = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	ts_hits = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())

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

class GameClan(Base):

	# Table structure
	__tablename__ = 'games_clans'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	tag = sqlalchemy.Column(sqlalchemy.String(length=64))
	name = sqlalchemy.Column(sqlalchemy.String(length=64))
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
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())

	# Relationships
	players = sqlalchemy.orm.relationship("GamePlayer", backref=sqlalchemy.orm.backref("clan", uselist=False), primaryjoin="GameClan.id == GamePlayer.clan_id")


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

class GamePlayerAction(Base):

	# Table structure
	__tablename__ = 'games_players_actions'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id'))
	action_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_actions.id'))
	map_id = sqlalchemy.Column(sqlalchemy.types.Integer, sqlalchemy.ForeignKey('games_maps.id'))
	is_victim = sqlalchemy.Column(sqlalchemy.types.Boolean)
	count = sqlalchemy.Column(sqlalchemy.types.Integer)
	count_delta = sqlalchemy.Column(sqlalchemy.types.Integer)
	count_reset = sqlalchemy.Column(sqlalchemy.types.BigInteger)

	# Relationsips
	game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id])
	player = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[player_id]) 
	action = sqlalchemy.orm.relationship("GameAction", foreign_keys=[action_id])
	map = sqlalchemy.orm.relationship("GameMap", foreign_keys=[map_id])

class GamePlayerAlias(Base):

	# Table structure
	__tablename__ = 'games_players_aliases'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id'))
	name = sqlalchemy.Column(sqlalchemy.types.String(length=64))
	seen_count = sqlalchemy.Column(sqlalchemy.types.Integer)
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())


	# Relationsips
	game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id])
	player = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[player_id]) 

class GamePlayerAward(Base):

	# Table structure
	__tablename__ = 'games_players_awards'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id'))
	award_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_awards.id'))
	date = sqlalchemy.Column(sqlalchemy.types.Date)
	count = sqlalchemy.Column(sqlalchemy.types.SmallInteger)

	# Relationsips
	game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id])
	player = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[player_id]) 
	award = sqlalchemy.orm.relationship("GameAward", foreign_keys=[award_id])

class GamePlayerAwardRibbon(Base):

	# Table structure
	__tablename__ = 'games_players_awards_ribbons'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id'))
	ribbon_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_awards_ribbons.id'))

	# Relationsips
	game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id])
	player = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[player_id]) 
	ribbon = sqlalchemy.orm.relationship("GameAwardRibbon", foreign_keys=[ribbon_id])

class GamePlayerMap(Base):

	# Table structure
	__tablename__ = 'games_players_maps'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id')) 
	map_id = sqlalchemy.Column(sqlalchemy.types.Integer, sqlalchemy.ForeignKey('games_maps.id'))
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
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())

	# Relationships
	game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id])
	player = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[player_id])
	map = sqlalchemy.orm.relationship("GameMap", foreign_keys=[map_id])
	weapons = sqlalchemy.orm.relationship("GamePlayerMapWeapon", backref=sqlalchemy.orm.backref("playermap", uselist=False), primaryjoin="GamePlayerMapWeapon.player_id == GamePlayerMap.player_id")

class GamePlayerWeapon(Base):

	# Table structure
	__tablename__ = 'games_players_weapons'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id')) 
	weapon_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_weapons.id'))
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
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())
	kills_delta = sqlalchemy.Column(sqlalchemy.types.Integer)
	hits_head_delta = sqlalchemy.Column(sqlalchemy.types.Integer)
	delta_reset = sqlalchemy.Column(sqlalchemy.types.BigInteger)

	# Relationships
	game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id])
	player = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[player_id])
	weapon = sqlalchemy.orm.relationship("GameWeapon", foreign_keys=[weapon_id])

class GamePlayerMapWeapon(Base):

	# Table structure
	__tablename__ = 'games_players_maps_weapons'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id')) 
	map_id = sqlalchemy.Column(sqlalchemy.types.Integer, sqlalchemy.ForeignKey('games_maps.id'))
	weapon_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_weapons.id'))
	damage = sqlalchemy.Column(sqlalchemy.types.BigInteger)
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
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())

	# Relationships
	game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id])
	player = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[player_id])
	map = sqlalchemy.orm.relationship("GameMap", foreign_keys=[map_id])
	weapon = sqlalchemy.orm.relationship("GameWeapon", foreign_keys=[weapon_id])

class GamePlayerRole(Base):

	# Table structure
	__tablename__ = 'games_players_roles'
	id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id')) 
	role_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_roles.id'))
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
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())

	# Relationships
	game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id])
	player = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[player_id])
	role = sqlalchemy.orm.relationship("GameRole", foreign_keys=[role_id])

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

class GameServer(Base):

	# Table structure
	__tablename__ = 'games_servers'
	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	name = sqlalchemy.Column(sqlalchemy.String(length=45))
	hostname = sqlalchemy.Column(sqlalchemy.String(length=127))
	port = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	hostname_public = sqlalchemy.Column(sqlalchemy.String(length=45))
	map_id = sqlalchemy.Column(sqlalchemy.types.Integer, sqlalchemy.ForeignKey('games_maps.id'))
	rcon_password = sqlalchemy.Column(sqlalchemy.String(length=45))
	sort_order = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
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
	act_players = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	max_players = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
	fps = sqlalchemy.Column(sqlalchemy.types.Float)
	uptime = sqlalchemy.Column(sqlalchemy.types.Integer)
	bombs_planeted = sqlalchemy.Column(sqlalchemy.types.Integer)
	bombs_defused = sqlalchemy.Column(sqlalchemy.types.Integer)
	ct_wins = sqlalchemy.Column(sqlalchemy.types.Integer)
	ts_wins	 = sqlalchemy.Column(sqlalchemy.types.Integer)
	ct_shots = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	ct_hits = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	ts_shots = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	ts_hits = sqlalchemy.Column(sqlalchemy.types.BigInteger)
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())

	# Relationships
	players = sqlalchemy.orm.relationship("GameServerPlayer", backref=sqlalchemy.orm.backref("server", uselist=False))
	map = global_winner = sqlalchemy.orm.relationship("GameMap", uselist=False, foreign_keys=[map_id])		

class GameServerPlayer(Base):

	# Table structure
	__tablename__ = 'games_servers_players'

	id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	server_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger,  sqlalchemy.ForeignKey('games_servers.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id'))
	role_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_roles.id'))
	team_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_teams.id'))
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
	created_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp(), onupdate=sqlalchemy.func.unix_timestamp())
	updated_at = sqlalchemy.Column(sqlalchemy.types.BigInteger, default=sqlalchemy.func.unix_timestamp())

	# Relationships
	role = sqlalchemy.orm.relationship("GameRole", backref=sqlalchemy.orm.backref("player", uselist=False), foreign_keys=[role_id])
	team = sqlalchemy.orm.relationship("GameTeam", backref=sqlalchemy.orm.backref("player", uselist=False), foreign_keys=[team_id])
	player = sqlalchemy.orm.relationship("GamePlayer", backref=sqlalchemy.orm.backref("server_player", uselist=False), foreign_keys=[player_id])

class GameServerChat(Base):

	# Table structure
	__tablename__ = 'games_servers_chats'
	id = sqlalchemy.Column(sqlalchemy.types.Integer, primary_key=True)
	game_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games.id'))
	server_id = sqlalchemy.Column(sqlalchemy.types.SmallInteger, sqlalchemy.ForeignKey('games_servers.id'))
	player_id = sqlalchemy.Column(sqlalchemy.types.BigInteger, sqlalchemy.ForeignKey('games_players.id')) 
	map_id = sqlalchemy.Column(sqlalchemy.types.Integer, sqlalchemy.ForeignKey('games_maps.id'))
	mode = sqlalchemy.Column(sqlalchemy.types.Boolean)
	message = sqlalchemy.Column(sqlalchemy.types.Text)
	date = sqlalchemy.Column(sqlalchemy.types.BigInteger)

	# Relationships
	game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id])
	player = sqlalchemy.orm.relationship("GamePlayer", foreign_keys=[player_id])
	map = sqlalchemy.orm.relationship("GameMap", foreign_keys=[map_id])
	server = sqlalchemy.orm.relationship("GameServer", foreign_keys=[server_id])
