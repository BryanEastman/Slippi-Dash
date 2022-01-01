# Slippi-Dash
A work in progress while I figure out the best way to structure this project.

Game Statistics dashboard for Super Smash Bros. Melee on Slippi

Overall package is broken into a group of scripts for generating data and files to store them in a database, which will serve as the base for other applications, namely dashboards.

## data

### test_data
- sample files packaged with the script

### game_database.sqlite3
- sqlite Database containing game data

### parsed.csv
- file to store games already processed

## get_data
scripts to aggregate and store data

### parse_data.py
- identifies all .slp game files from a given root directory
- checks against a list of processed files to avoid redundant processing
- generates a Pandas DataFrame of metadata (filepath, date, game duration in frames, stage, tags, characters, end stocks and damage, and quit-outs)
- pushes datasets to SQL database
- saves a list of processed files by path into a csv

### build_db.py
- creates SQLite database tables to contain data scraped with the parser

