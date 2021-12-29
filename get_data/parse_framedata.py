import slippi as slp
import timeit
from slippi import metadata

from slippi.metadata import Metadata
from parse_metadata import get_files
from slippi.parse import parse
from slippi.parse import ParseEvent

files = get_files()
print(files[0])

def parse_json(files):
    rows = []
    for file in files:
        game = slp.Game(file)
        player_1 = game.metadata.players[0].netplay.code
        rows.append(player_1)
    return rows


def parse_api(files):
    md = None
    def set_md(x):
        nonlocal md
        md = x    
    parse(slp.Game(files[0]),{ParseEvent.METADATA: print})
   
parse_api(files)
    
