from HLModel import HLModel
from Singleton import Singleton


class Engine(Singleton, HLModel):
    table = "engines"
    cache = {}
    index = {}
    debug = False
    locking = True
    index_keys = []
