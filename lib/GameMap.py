from HLModel import HLModel
from Singleton import Singleton


class GameMap(Singleton, HLModel):
    cache = {}
    index_keys = ["game_id", "code"]
    index = {}
    debug = False
    locking = True
    table = 'games_maps'
