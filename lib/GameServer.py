from HLModel import HLModel
from Singleton import Singleton


class GameServer(Singleton, HLModel):
    cache = {}
    index_keys = ["address"]
    index = {}
    debug = False
    locking = True
    table = 'games_servers'
