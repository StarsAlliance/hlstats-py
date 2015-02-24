# Standard Imports
import twisted.internet.protocol
import termcolor
import time
import threading
import timeit

# HLStats-py Imports
from Engine import Engine
from Game import Game
from GameServer import GameServer
from Player import Player
from GamePlayer import GamePlayer
from GameMap import GameMap
from GameWeapon import GameWeapon
from HLConfig import config


class LogServer(twisted.internet.protocol.DatagramProtocol):

    # This is fired whenever the log server starts up
    def startProtocol(self):
        # Create a dictionary to track our parsers
        self.parsers = {}
        self.lines = 0
        self.time = 0.0
        self.startup = timeit.default_timer()
        self.engine = Engine()
        self.game = Game()

    # This event is fired whenever a log message is recieved
    def datagramReceived(self, data, (host, port)):
        start = timeit.default_timer()
        self.lines += 1
        # Concatenate host and port together
        address = "%s:%d" % (host, port)

        # Look up the game server
        gameserver = GameServer().get(address=address)

        # Is this game server allowed?
        if gameserver is None:
            #print termcolor.colored("Message from Unknown Server (%s), Ignoring" % (address), 'yellow')
            self.time += (timeit.default_timer()-start)
            return

        # Do we have a parser running for this server yet?
        if address not in self.parsers:
            # Get the Game
            game = self.game.get(id=gameserver['game_id'])
            # Get the Engine
            engine = self.engine.get(id=game['engine_id'])
            # Import the Parser for this engine
            exec "from %sParser import Parser" % (engine['code'].upper())
            # Create the parser
            self.parsers[address] = Parser(address)
            # Run the parser
            self.parsers[address].start()

        # Give the message to the parser, let it do it's thing
        self.parsers[address].put(data)
        self.time += (timeit.default_timer()-start)

    # This is fired before the server shuts down
    def shutdown(self):
        elapsed = (timeit.default_timer()-self.startup)
        print ""
        # Loop through all of our parsers and shut them down
        for key, parser in self.parsers.items():
                # Shut it down
                parser.stop()
                # Kill the thread
                parser.join()
        print termcolor.colored("-------------------------------------------------", 'red')
        print termcolor.colored("Shut down Log Server. Total Logs Processed: %d (%.2flps)" % (self.lines, round(self.lines / elapsed, 2)), 'red')
        print termcolor.colored(
            "Log Server was running for %.4f seconds. %.4f was spent processing or blocked. (%.2f%%)" %
            (round(elapsed, 4), round(self.time, 4), round((self.time / elapsed * 100), 2)), 'red')

    def stats(self):
        for key, parser in self.parsers.items():
            parser.stats()
        elapsed = (timeit.default_timer()-self.startup)
        print termcolor.colored("-------------------------------------------------", 'red')
        print termcolor.colored("Total Logs Processed: %d (%.2flps)" % (self.lines, round(self.lines / elapsed, 2)), 'red')
        print termcolor.colored(
            "Log Server is running for %.4f seconds. %.4f has been spent processing or blocked. (%.2f%%)" %
            (round(elapsed, 4), round(self.time, 4), round((self.time / elapsed * 100), 2)), 'red')
        print termcolor.colored("Number of items in Engine cache: %d" % (Engine().getCacheCount()), 'red')
        print termcolor.colored("Number of items in Server cache: %d" % (GameServer().getCacheCount()), 'red')
        print termcolor.colored("Number of items in Game cache: %d" % (Game().getCacheCount()), 'red')
        print termcolor.colored("Number of items in Player cache: %d" % (Player().getCacheCount()), 'red')
        print termcolor.colored("Number of items in GamePlayer cache: %d" % (GamePlayer().getCacheCount()), 'red')
        print termcolor.colored("Number of items in GameMap cache: %d" % (GameMap().getCacheCount()), 'red')
        print termcolor.colored("Number of items in GameWeapon cache: %d" % (GameWeapon().getCacheCount()), 'red')

    def gc(self):
        now = time.time()
        for key, parser in self.parsers.items():
            if parser.getLastMessageTime() < (now-config.getint('timers', 'idle_server_timeout')):
                del self.parsers[key]
                parser.stop()
                parser.join()
        pass

