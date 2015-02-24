# Base Imports
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import time
import termcolor
import valve.source.rcon
import valve.source.a2s
import re
import pprint
import datetime

from HLModels import *
class Parser():

    def __init__(self, session_lock, session, server):
        self.player_cache = {}
        self.session_lock = session_lock
        self.session = session
        self.server = server
        self.message_regex = {
            'PvkiiParrot' : re.compile(r'"(?P<player>.+?(?:<[^>]*>){3})"\s[a-z]{6}\s"npc_parrot<.+?>"\s[a-z]{5}\s[a-z]{2}\s"(?P<victim>.+?(?:<[^>]*>){3})"\s[a-z]{4}\s"(?P<weapon>[^"]*)"(<properties>.*)'),
            'StandardKill' : re.compile(r'(?:\(DEATH\))?"(?P<player>.+?(?:<.+?>)*?(?:<setpos_exact\s(?P<player_x>-?\d+?\.\d\d)\s(?P<player_y>-?\d+?\.\d\d)\s(?P<player_z>-?\d+?\.\d\d);[^"]*)?)"(?:\s\[(?P<player_x2>-?\d+)\s(?P<player_y2>-?\d+)\s(?P<player_z2>-?\d+)\])?\skilled\s"(?P<victim>.+?(?:<.+?>)*?(?:<setpos_exact\s(?P<victim_x>-?\d+?\.\d\d)\s(?P<victim_y>-?\d+?\.\d\d)\s(?P<victim_z>-?\d+?\.\d\d);[^"]*)?)"(?:\s\[(?P<victim_x2>-?\d+)\s(?P<victim_y2>-?\d+)\s(?P<victim_z2>-?\d+)\])?\swith\s"(?P<weapon>[^"]*)"(?P<properties>.*)'),
            'L4dIncap' : re.compile(r'\(INCAP\)"(?P<victim>.+?(?:<.+?>)*?<setpos_exact\s(?P<victim_x>-?\d+?\.\d\d)\s(?P<victim_y>-?\d+?\.\d\d)\s(?P<victim_z>-?\d+?\.\d\d);[^"]*)"\swas\sincapped\sby\s"(<player>.+?(?:<.+?>)*?<setpos_exact\s(?P<player_x>-?\d+?\.\d\d)\s(?P<player_y>-?\d+?\.\d\d)\s(?P<player_z>-?\d+?\.\d\d);[^"]*)"\swith\s"(?P<weapon>[^"]*)"(?P<properties>.*)'),
            'L4dTounge' : re.compile(r'\(TONGUE\)\sTongue\sgrab\sstarting\.\s+Smoker:"(?P<player>.+?(?:<.+?>)*?(?:|<setpos_exact (?P<player_x>(?:|-)\d+?\.\d\d) (?P<player_y>(?:|-)\d+?\.\d\d) (?P<player_z>(?:|-)\d+?\.\d\d);.*?))"\.\s+Victim:"(?P<victim>.+?(?:<.+?>)*?(?:|<setpos_exact (?P<victim_x>(?:|-)\d+?\.\d\d) (?P<victim_y>(?:|-)\d+?\.\d\d) (?P<victim_z>(?:|-)\d+?\.\d\d);.*?))".*'),
            'Triggered' : re.compile(r'"(?P<player>.+?(?:<.+?>)*?)"\s(?P<verb>triggered(?:\sa)?)\s"(?P<action>.+?(?:<.+?>)*?)"\s[a-zA-Z]+\s"(?P<victim>.+?(?:<.+?>)*?)"(?:\s[a-zA-Z]+\s"(?P<weapon>.+?)")?(?P<properties>.*)'),
            'WeaponStats' : re.compile(r'(?:\[STATSME\] )?"(?P<player>.+?(?:<.+?>)*)" triggered "(?P<verb>weaponstats\d{0,1})"(?P<properties>.*)'),
            'TimeStats' : re.compile(r'(?:\[STATSME\] )?"(?P<player>.+?(?:<.+?>)*)" triggered "(?P<verb>latency|time)"(?P<properties>.*)'),
            'Actions' : re.compile(r'"(?P<player>.+?(?:<.+?>)*?)" (?P<verb>[a-zA-Z,_\s]+) "(?P<object>.+?)"(?P<properties>.*)'),
            'EnterAndLeave' : re.compile(r'(?:Kick: )?"(?P<player>.+?(?:<.+?>)*)" (?P<verb>[^\(]+)(?P<properties>.*)'),
            'TeamAction' : re.compile(r'Team "(?P<team>.+?)" (?P<verb>[^"\(]+) "(?P<object>[^"]+)"(?P<properties>.*)'),
            'Rcon' : re.compile(r'(?P<verb>Rcon|Bad Rcon): "rcon [^"]+"([^"]+)"\s+(?P<command>.+)" from "(?P<address>[0-9\.]+?):(?P<port>\d+?)"(.*)'),
            'Rcon2' : re.compile(r'rcon from "(?P<address>.+?):(?P<port>.+?)": (?:command "(?P<command>.*)".*|(?P<bad>Bad) Password)'),
            'AdminMod' : re.compile(r'\[(.+)\.(smx|amxx)\]\s*(.+)/i'),
            'ServerAndWorld' : re.compile(r'([^"\(]+) "([^"]+)"(.*)'),
            'ManiAdmin' : re.compile(r'\[MANI_ADMIN_PLUGIN\]\s*(.+)'),
            'BeetlesMod' : re.compile(r'\[BeetlesMod\]\s*(.+)'),
            'AdminMod2' : re.compile(r'\[ADMIN:(.+)\] ADMIN Command: \1 used command (.+)'),
            'DystopiaStatsMe' : re.compile(r'weapon { steam_id: \'STEAM_\d+:(.+?)\', weapon_id: (\d+), class: \d+, team: \d+, shots: \((\d+),(\d+)\), hits: \((\d+),(\d+)\), damage: \((\d+),(\d+)\), headshots: \((\d+),(\d+)\), kills: \(\d+,\d+\) }'),
            'DystopiaClassChange' : re.compile(r'(?:join|change)_class { steam_id: \'STEAM_\d+:(.+?)\', .* (?:new_|)class: (\d+), .* }'),
            'DystopiaOjbective' : re.compile(r'objective { steam_id: \'STEAM_\d+:(.+?)\', class: \d+, team: \d+, objective: \'(.+?)\', time: \d+ }')
        }
        self.rcon_player_regex = re.compile(r'\#\s*\d+\s+"(?P<name>.+)"\s+(?P<user_id>\d+)\s+(?P<steam_id>[^\s]+)\s+\d+\s+(?P<time_connected>[\d:]+)\s+(?P<latency>\d+)\s+(?P<loss>\d+)\s+(?P<ip>[^:]+):(?P<port>\S+)')
        self.difficulty_regex = re.compile(r'\s*"z_difficulty"\s*=\s*"(?P<difficulty>[A-Za-z]+)".*')
        self.player_regex = re.compile(r'(?P<name>.*?)<(?P<user_id>\d+)><(?P<steam_id>[^<>]*)><(?P<team>[^<>]*)>(?:<(?P<role>[^<>]*)>)?.*')
        self.bot_regex = re.compile(r'\([0-9]+\)')

        
    # Parses a timestamp from a file
    def parseTimestamp(self, message):
        # Regular expression for matching timestamps
        timestamp_regex = re.compile(r".*L (?P<month>\d\d)\/(?P<day>\d\d)\/(?P<year>\d{4}) - (?P<hour>\d\d):(?P<minute>\d\d):(?P<second>\d\d):\s+(?P<message>.*)")
        # Run the match
        match = timestamp_regex.match(message)	# Run the match
        if not match:				# If it's not a match
            return None			# return None
        properties = match.groupdict()		# get a dict of the match
        # Use the match to generate a datetime object and return the rest of the message
        return (datetime.datetime(int(properties['year']), int(properties['month']), int(properties['day']), int(properties['hour']), int(properties['minute']), int(properties['second'])), properties['message'])
    
    def parse(self, message):
        # Strip whitespace
        message = message.strip(' \t\r\n\xff')
        buf = ""
        # Parse off the timestamp first
        timestamp,message = self.parseTimestamp(message)	
        if timestamp is None:
            buf += termcolor.colored("Server sent corrupt message: %s" % (message), 'yellow')+"\n"
            return buf
        # Loop through items and try and match
        for key, value in self.message_regex.items():
            match = value.match(message)
            if match:
                result = match.groupdict()
                exec "self.handle%s(result)" % key
                return buf
        buf += termcolor.colored("Server sent unknown message: %s" % (message), 'yellow')+"\n"
        return buf

    def serverInfo():
        pass

    def sync(self):
        # Get the current server info
        # Map / Players / Z-Difficulty
        active_players = self.rconStatus()
        for active_player in active_players:
            player = self.lookupPlayer(active_player['steam_id']);

   
    def lookupPlayer(self, unique_id):
        if unique_id in self.player_cache
        commit = False
        self.session_lock.acquire()
        player = self.session.query(Player).filter_by(unique_id=unique_id).first()
        if player is None:
            commit = True
            player = Player(unique_id=unique_id)
        if player.players:
            player.players = [i for i in player.players if i.game_id == self.server.game.id]
        if not player.players:
            commit = True
            game_player = GamePlayer(game_id = self.server.game.id)
            player.players.append(game_player)
        # TODO: Look up server player or add player to server
        if commit:
            self.session.add(player)
            self.session.commit()
        self.session_lock.release()
        return player
    
    def parsePlayer(self, message):
        print message
        match = self.player_regex.match(message)
        print match
        if not match:
            return None
        details = match.groupdict()
        if self.server.game.code == 'l4d' or self.server.game.code == 'l4d2':
            if details['steam_id'] == '':
                if details['name'] == 'infected':
                    details['team'] = 'Infected'
                    details['steam_id'] = 'BOT-Horde'
                elif details['name'] == 'witch':
                    details['team'] = 'Infected'
                    details['steam_id'] = 'Bot-Witch'
            elif details['steam_id'] == 'BOT':
                details['name'] = self.bot_regex.sub('', details['name'])
                details['steam_id'] = "BOT-" + details['name']
        return details
    
    def rconStatus(self):
        # Player regex
        with valve.source.rcon.RCON((self.server.hostname, self.server.port), self.server.rcon_password) as rcon:
            status = rcon('status').split('\n')
        players = []
        for line in status:
            match = self.rcon_player_regex.match(line.strip())
            if match:
                players.append(match.groupdict())
        return players
    
    def handlePvkiiParrot(self, result):
        pass
    
    def handleStandardKill(self, result):
        print result
        player_details = self.parsePlayer(result['player'])
        victim_details = self.parsePlayer(result['victim'])
        
        player = self.lookupPlayer(player_details['steam_id']);
        victim = self.lookupPlayer(victim_details['steam_id']);
        pass
    
    def handleL4dIncap(self, result):
        player_details = self.parsePlayer(result['player'])
        victim_details = self.parsePlayer(result['victim'])
        
        player = self.lookupPlayer(player_details['steam_id']);
        victim = self.lookupPlayer(victim_details['steam_id']);
        pass
    
    def handleL4dTounge(self, result):
        player_details = self.parsePlayer(result['player'])
        victim_details = self.parsePlayer(result['victim'])
        
        player = self.lookupPlayer(player_details['steam_id']);
        victim = self.lookupPlayer(victim_details['steam_id']);
        pass
    
    def handleTriggered(self, result):
        pass
    
    def handleWeaponStats(self, result):
        pass
    
    def handleTimeStats(self, result):
        pass
    
    def handleActions(self, result):
        pass
    
    def handleEnterAndLeave(self, result):
        pass
    
    def handleTeamAction(self, result):
        pass
    
    def handleRcon(self, result):
        pass
    
    def handleRcon2(self, result):
        pass
    
    def handleAdminMod(self, result):
        pass
    
    def handleServerAndWorld(self, result):
        pass
    
    def handleManiAdmin(self, result):
        pass
    
    def handleBeetlesMod(self, result):
        pass
    
    def handleAdminMod2(self, result):
        pass
    
    def DystopiaStatsMe(self, result):
        pass
    
    def DystopiaClassChange(self, result):
        pass
    
    def DystopiaOjbective(self, result):
        pass
    