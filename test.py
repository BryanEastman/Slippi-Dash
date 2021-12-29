import slippi
from slippi.id import InGameCharacter
from slippi.id import Stage
from slippi.metadata import Metadata
from enum import Enum
from slippi.parse import parse
from slippi.parse import ParseEvent
import sqlite3
import pandas as pd
import os


path = '/media/beastman/36E8AEA6E8AE63B9/Users/newco/Documents/Slippi/2021-12/Game_20211204T090000.slp'
g = slippi.Game(path)
char = g.metadata.players[0].characters
stag = g.start.stage
end = g.end


"""
just putting this here because it's really important:::

Hi, I'm the author of py-slippi. This isn't really the right place, but I couldn't find a better communication channel. Anyway, nice work! It's great to see my library fulfilling its purpose. Do you have any general feedback about py-slippi? Pain points, suggestions, etc.

A small tip about enums: to avoid the need for functions like character_name, you can use .name to get a human-readable string representation of an enum.

Also, check out py-slippi's streaming branch! There's a new event-driven parsing style that can avoid holding the entire game in memory at once as well as deal with incomplete replays.

In addition, the existing Game constructor should also be much faster in that branch because it defers parsing frame data until needed. I'd love it if you could try it out and let me know what you think.
"""