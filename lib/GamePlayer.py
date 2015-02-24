from HLModel import HLModel
from Singleton import Singleton


class GamePlayer(Singleton, HLModel):
    cache = {}
    index_keys = ["player_id", "game_id"]
    index = {}
    debug = False
    locking = True
    table = 'games_players'
