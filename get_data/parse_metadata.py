import pandas as pd
import os
import csv
import sqlite3

import slippi as slp
from slippi import Game
from slippi.util import try_enum
from slippi.id import InGameCharacter

parsed_path = r'./data/parsed.csv'
db_path = r'./data/game_database.sqlite3'

def get_files():
    """
    return number of slp files in filepath, 
    raise errors if not found
    """
    path = input('Paste path to replays: ').replace("'","")
    game_files = []
    try:
        print('replays found:\n')
        for root,dirs,files in os.walk(path,topdown=True):            
            print('{}: {}'.format(root, sum([x.count('.slp',-4) for x in files])))
            game_files = ([os.path.join(root,x) for x in files if x[-4:] == '.slp'])
    except NameError:
        print("Invalid Path")
    return game_files

def check_parsed(games):
    """
    Returns a list of new, unprocessed game files
    """
    new_games = list()
    with open(parsed_path,'r') as file:
        reader = csv.reader(file,delimiter=",")
        parsed = [x for [x] in reader]
        for game in games:
            if game in parsed:
                games.remove(game)
            else:
                new_games.append(game)
    if len(new_games) < 1:
        print('no new games found')
        exit()
    return new_games

def processed(new_games):
    """
    Writes path to parsed.csv to skip next time processing
    """
    with open(parsed_path,'a') as file:
        writer = csv.writer(file)
        for game in new_games:
            writer.writerow([game])

def scrape_metadata(new_games): # may be possible to use event API to parse more quickly
    """
    Generates a dataframe of game metadata for each new game
    """
    meta_df = pd.DataFrame(columns = [
        'date',
        'path',
        'duration_frames',
        'player_1_tag',
        'player_1_char',
        'player_1_end_stocks',
        'player_1_end_dmg',
        'player_2_tag',
        'player_2_char',
        'player_2_end_stocks',
        'player_2_end_dmg',
        'stage',
        'end_method',
        'lras'      
    ])

    rows = []
    for i, game in enumerate(new_games):
        print(r'parsing {} of {}'.format(i,len(new_games)), end="\r")
        try:
            slp_game = Game(game)
        
            char_1 = slp_game.metadata.players[0].characters
            char_2 = slp_game.metadata.players[0].characters

            row = {
                'date': slp_game.metadata.date,
                'path': game,
                'duration_frames':slp_game.metadata.duration,
                'player_1_tag':slp_game.metadata.players[0].netplay.code,
                'player_1_char': try_enum(InGameCharacter,*char_1).name,
                'player_1_end_stocks':slp_game.frames[-1].ports[0].leader.post.stocks,
                'player_1_end_dmg':slp_game.frames[-1].ports[0].leader.post.damage,
                'player_2_tag':slp_game.metadata.players[1].netplay.code,
                'player_2_char':try_enum(InGameCharacter,*char_2).name,
                'player_2_end_stocks':slp_game.frames[-1].ports[1].leader.post.stocks,
                'player_2_end_dmg':slp_game.frames[-1].ports[1].leader.post.damage,
                'stage':slp_game.start.stage.name,
                'end_method':slp_game.end.method.name,
                'lras': slp_game.end.lras_initiator
                }
        except:
            print('skipping: ', i, game)
            continue
        rows.append(row)
    meta_df = pd.DataFrame.from_dict(rows)
    return meta_df

def append_table(table_name, data):
    con = sqlite3.connect(db_path)
    data.to_sql(
        table_name,
        con,
        if_exists='append',
        index=False,
        chunksize=1000
        )

if __name__ == '__main__':
    games_list = get_files()
    new_games = check_parsed(games_list)
    meta = scrape_metadata(new_games)
    append_table("metadata",meta)
    # processed(new_games)
    
    
