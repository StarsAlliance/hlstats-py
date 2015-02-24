from HLModel import HLModel
from Singleton import Singleton


class GameWeapon(Singleton, HLModel):
    cache = {}
    index_keys = ["code", "game_id"]
    index = {}
    debug = False
    locking = True
    table = 'games_weapons'
