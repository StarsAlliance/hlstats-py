import datetime
import LogParser
import re
import termcolor
import collections
import pprint
import valve.source.a2s


class Parser(LogParser.Parser):
    message_regex = collections.OrderedDict()
    message_regex['PvkiiParrot'] = re.compile(r'"(?P<player>.+?(?:<[^>]*>){3})"\s[a-z]{6}\s"npc_parrot<.+?>"\s[a-z]{5}\s[a-z]{2}\s"(?P<victim>.+?(?:<[^>]*>){3})"\s[a-z]{4}\s"(?P<weapon>[^"]*)"(<properties>.*)')
    message_regex['StandardKill'] = re.compile(r'(?:\(DEATH\))?"(?P<player>.+?(?:<.+?>)*?(?:<setpos_exact\s(?P<player_x>-?\d+?\.\d\d)\s(?P<player_y>-?\d+?\.\d\d)\s(?P<player_z>-?\d+?\.\d\d);[^"]*)?)"(?:\s\[(?P<player_x2>-?\d+)\s(?P<player_y2>-?\d+)\s(?P<player_z2>-?\d+)\])?\skilled\s"(?P<victim>.+?(?:<.+?>)*?(?:<setpos_exact\s(?P<victim_x>-?\d+?\.\d\d)\s(?P<victim_y>-?\d+?\.\d\d)\s(?P<victim_z>-?\d+?\.\d\d);[^"]*)?)"(?:\s\[(?P<victim_x2>-?\d+)\s(?P<victim_y2>-?\d+)\s(?P<victim_z2>-?\d+)\])?\swith\s"(?P<weapon>[^"]*)"(?P<properties>.*)')
    message_regex['L4dIncap'] = re.compile(r'\(INCAP\)"(?P<victim>.+?(?:<.+?>)*?<setpos_exact\s(?P<victim_x>-?\d+?\.\d\d)\s(?P<victim_y>-?\d+?\.\d\d)\s(?P<victim_z>-?\d+?\.\d\d);[^"]*)"\swas\sincapped\sby\s"(<player>.+?(?:<.+?>)*?<setpos_exact\s(?P<player_x>-?\d+?\.\d\d)\s(?P<player_y>-?\d+?\.\d\d)\s(?P<player_z>-?\d+?\.\d\d);[^"]*)"\swith\s"(?P<weapon>[^"]*)"(?P<properties>.*)')
    message_regex['L4dTounge'] = re.compile(r'\(TONGUE\)\sTongue\sgrab\sstarting\.\s+Smoker:"(?P<player>.+?(?:<.+?>)*?(?:|<setpos_exact (?P<player_x>(?:|-)\d+?\.\d\d) (?P<player_y>(?:|-)\d+?\.\d\d) (?P<player_z>(?:|-)\d+?\.\d\d);.*?))"\.\s+Victim:"(?P<victim>.+?(?:<.+?>)*?(?:|<setpos_exact (?P<victim_x>(?:|-)\d+?\.\d\d) (?P<victim_y>(?:|-)\d+?\.\d\d) (?P<victim_z>(?:|-)\d+?\.\d\d);.*?))".*')
    message_regex['Triggered'] = re.compile(r'"(?P<player>.+?(?:<.+?>)*?)"\s(?P<verb>triggered(?:\sa)?)\s"(?P<action>.+?(?:<.+?>)*?)"\s[a-zA-Z]+\s"(?P<victim>.+?(?:<.+?>)*?)"(?:\s[a-zA-Z]+\s"(?P<weapon>.+?)")?(?P<properties>.*)')
    message_regex['WeaponStats'] = re.compile(r'(?:\[STATSME\] )?"(?P<player>.+?(?:<.+?>)*)" triggered "(?P<verb>weaponstats\d{0,1})"(?P<properties>.*)')
    message_regex['TimeStats'] = re.compile(r'(?:\[STATSME\] )?"(?P<player>.+?(?:<.+?>)*)" triggered "(?P<verb>latency|time)"(?P<properties>.*)')
    message_regex['Actions'] = re.compile(r'"(?P<player>.+?(?:<.+?>)*?)" (?P<verb>[a-zA-Z,_\s]+) "(?P<object>.+?)"(?P<properties>.*)')
    message_regex['EnterAndLeave'] = re.compile(r'(?:Kick: )?"(?P<player>.+?(?:<.+?>)*)" (?P<verb>[^\(]+)(?P<properties>.*)')
    message_regex['TeamAction'] = re.compile(r'Team "(?P<team>.+?)" (?P<verb>[^"\(]+) "(?P<object>[^"]+)"(?P<properties>.*)')
    message_regex['Rcon'] = re.compile(r'(?P<verb>Rcon|Bad Rcon): "rcon [^"]+"([^"]+)"\s+(?P<command>.+)" from "(?P<address>[0-9\.]+?):(?P<port>\d+?)"(.*)')
    message_regex['Rcon2'] = re.compile(r'rcon from "(?P<address>.+?):(?P<port>.+?)": (?:command "(?P<command>.*)".*|(?P<bad>Bad) Password)')
    message_regex['AdminMod'] = re.compile(r'\[(.+)\.(smx|amxx)\]\s*(.+)/i')
    message_regex['ServerAndWorld'] = re.compile(r'([^"\(]+) "([^"]+)"(.*)')
    message_regex['ManiAdmin'] = re.compile(r'\[MANI_ADMIN_PLUGIN\]\s*(.+)')
    message_regex['BeetlesMod'] = re.compile(r'\[BeetlesMod\]\s*(.+)')
    message_regex['AdminMod2'] = re.compile(r'\[ADMIN:(.+)\] ADMIN Command: \1 used command (.+)')
    message_regex['DystopiaStatsMe'] = re.compile(r'weapon { steam_id: \'STEAM_\d+:(.+?)\', weapon_id: (\d+), class: \d+, team: \d+, shots: \((\d+),(\d+)\), hits: \((\d+),(\d+)\), damage: \((\d+),(\d+)\), headshots: \((\d+),(\d+)\), kills: \(\d+,\d+\) }')
    message_regex['DystopiaClassChange'] = re.compile(r'(?:join|change)_class { steam_id: \'STEAM_\d+:(.+?)\', .* (?:new_|)class: (\d+), .* }')
    message_regex['DystopiaOjbective'] = re.compile(r'objective { steam_id: \'STEAM_\d+:(.+?)\', class: \d+, team: \d+, objective: \'(.+?)\', time: \d+ }')

    rcon_player_regex = re.compile(r'\#\s*\d+\s+"(?P<name>.+)"\s+(?P<user_id>\d+)\s+(?P<steam_id>[^\s]+)\s+\d+\s+(?P<time_connected>[\d:]+)\s+(?P<latency>\d+)\s+(?P<loss>\d+)\s+(?P<ip>[^:]+):(?P<port>\S+)')
    difficulty_regex = re.compile(r'\s*"z_difficulty"\s*=\s*"(?P<difficulty>[A-Za-z]+)".*')
    player_regex = re.compile(r'(?P<name>.*?)<(?P<user_id>\d+)><(?P<steam_id>[^<>]*)><(?P<team>[^<>]*)>(?:<(?P<role>[^<>]*)>)?.*')
    bot_regex = re.compile(r'\([0-9]+\)')
    timestamp_regex = re.compile(r".*L (?P<month>\d\d)\/(?P<day>\d\d)\/(?P<year>\d{4}) - (?P<hour>\d\d):(?P<minute>\d\d):(?P<second>\d\d):\s+(?P<message>.*)")

    def parse(self, message):
        # Strip off unreadable bytes
        message = message.strip(' \t\r\n\xff')
        # Create an empty buffer
        buf = ""
        # Parse the timestamp off
        timestamp, message = self.parseTimestamp(message)
        # If no timestamp, must be corrupted
        if timestamp is None:
            # Return a buffer indicating a corrupt message
            buf += termcolor.colored("Server sent corrupt message: %s" % (message), 'yellow')+"\n"
            return buf
        # Loop through our regex and find a match
        for key in self.message_regex.keys():
            # run the match
            match = self.message_regex[key].match(message)
            # if there is a match
            if match:
                # get a dictionary
                result = match.groupdict()
                # execute the proper handler
                exec "buf += self.handle%s(result)" % key
                # return the buffer
                return buf
        # If we fall through the loop without returning, we have an unknown message
        #buf += termcolor.colored("Server sent unknown message: %s" % (message), 'yellow')
        # return the buffer
        return buf

    def parseTimestamp(self, message):
        # Run the timestamp match
        match = self.timestamp_regex.match(message)
        # If no match return None
        if not match:
            return None
        # Get a dictionary
        properties = match.groupdict()
        # Return a tuple of (timestamp, remaining message) created from the dictionary
        return (datetime.datetime(int(properties['year']), int(properties['month']), int(properties['day']), int(properties['hour']), int(properties['minute']), int(properties['second'])), properties['message'])

    def parsePlayer(self, message):
        match = self.player_regex.match(message)
        if not match:
            return None
        details = match.groupdict()
        if self.cur_game['code'] == 'l4d' or self.cur_game['code'] == 'l4d2':
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

    def sync(self):
        # Get Server Info
        ip, port = self.cur_server["address"].split(":")
        info = dict(valve.source.a2s.ServerQuerier((ip, int(port))).get_info())
        # Get the map Info
        self.server.update(
            self.cur_server["id"],
            map_id=self.game_map.getOrCreate(game_id=self.cur_game['id'], code=info["map"])["id"],
            act_players=info["player_count"],
            max_players=info["max_players"],
            name=info["server_name"]
        )

    def handlePvkiiParrot(self, result):
        pass

    def handleStandardKill(self, result):
        # Player details
        player_details = self.parsePlayer(result['player'])
        player = self.player.getOrCreate(unique_id=player_details['steam_id'])
        player_game = self.game_player.getOrCreate(player_id=player['id'], game_id=self.cur_game['id'])
        self.game_player.update(player_game['id'], name=player_details["name"])

        # Victim details
        victim_details = self.parsePlayer(result['victim'])
        victim = self.player.getOrCreate(unique_id=victim_details['steam_id'])
        victim_game = self.game_player.getOrCreate(player_id=victim['id'], game_id=self.cur_game['id'])
        self.game_player.update(victim_game['id'], name=victim_details["name"])

        # Weapon details
        weapon_details = self.game_weapon.get(game_id=self.cur_game['id'], code=result['weapon'])

        # Map details
        map_details = self.game_map.get(id=self.cur_server['map_id'])

        return ""

    def handleL4dIncap(self, result):
        player_details = self.parsePlayer(result['player'])
        victim_details = self.parsePlayer(result['victim'])
        return ""

    def handleL4dTounge(self, result):
        player_details = self.parsePlayer(result['player'])
        victim_details = self.parsePlayer(result['victim'])
        return ""

    def handleTriggered(self, result):
        return ""

    def handleWeaponStats(self, result):
        return ""

    def handleTimeStats(self, result):
        return ""

    def handleActions(self, result):
        return ""

    def handleEnterAndLeave(self, result):
        return ""

    def handleTeamAction(self, result):
        return ""

    def handleRcon(self, result):
        return ""

    def handleRcon2(self, result):
        return ""

    def handleAdminMod(self, result):
        return ""

    def handleServerAndWorld(self, result):
        return ""

    def handleManiAdmin(self, result):
        return ""

    def handleBeetlesMod(self, result):
        return ""

    def handleAdminMod2(self, result):
        return ""

    def DystopiaStatsMe(self, result):
        return ""

    def DystopiaClassChange(self, result):
        return ""

    def DystopiaOjbective(self, result):
        return ""
