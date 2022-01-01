from get_data import parse_metadata, build_db
import time

parsed_path = r'./data/parsed.csv' #path to csv of parsed files
db_path = r'./data/game_database.sqlite3' #defines dabase path in root folder of package

if __name__ == "__main__":
    build_db.build_db_meta() #creates database with metadata  
    files = parse_metadata.get_files()
    new_games = parse_metadata.check_parsed(files)
    meta = parse_metadata.scrape_metadata(new_games)
    parse_metadata.append_table("metadata",meta)
    parse_metadata.processed(new_games)



    
