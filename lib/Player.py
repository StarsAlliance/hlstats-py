from HLModel import HLModel
from Singleton import Singleton


class Player(Singleton, HLModel):
    cache = {}
    index_keys = ["unique_id"]
    index = {}
    debug = False
    locking = True
    table = 'players'
