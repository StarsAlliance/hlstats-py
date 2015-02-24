# Base Imports
import re

import HLParser


class Parser(HLParser.Parser):
    rcon_player_regex = re.compile(r'\#\s*(?P<user_id>\d+)\s+(?:\d+\s+|)"(?P<name>.+)"\s+(?P<steam_id>.+)\s+(?P<time_connected>[\d:]+)\s+(?P<latency>\d+)\s+(?P<loss>\d+)\s+(?P<state>[A-Za-z]+)\s+(?:\d+\s+|)(?P<ip>[^:]+):(?P<port>\S+)')
