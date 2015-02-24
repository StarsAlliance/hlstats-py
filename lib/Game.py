from HLModel import HLModel
from Singleton import Singleton


class Game(Singleton, HLModel):
    table = 'games'
    debug = False
    cache = {}
    index = {}
    locking = False
    index_keys = []
