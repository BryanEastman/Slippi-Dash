import sqlite3

def build_db_meta():
    """
    creates the metadata table
    """
    con = sqlite3.connect('./data/game_database.sqlite3')
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE metadata (
            idx INTEGER,
            date TEXT,
            path TEXT,
            duration_frames INTEGER,
            player_1_tag TEXT,
            player_1_char TEXT,
            player_1_end_stocks INTEGER,
            player_1_end_dmg REAL,
            player_2_tag TEXT,
            player_2_char TEXT,
            player_2_end_stocks INTEGER,
            player_2_end_dmg REAL,
            stage TEXT,
            end_method TEXT,
            lras INTEGER  
        )
        """
        )
    con.commit()
    con.close()

def drop_table():
    """
    For testing purposes, drop table by name 
    """
    con = sqlite3.connect('./data/game_database.sqlite3')
    cur = con.cursor()
    cur.execute(
        """
        DROP TABLE IF EXISTS metadata;
        """      
    )
    con.commit()
    con.close

if __name__ == "__main__":
    build_db_meta()
    #drop_table()
    None