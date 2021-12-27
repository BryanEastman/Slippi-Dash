# Slippi-Dash
Game Statistics dashboard for Super Smash Bros. Melee on Slippi

This is primarily for personal use and built assuming only standard competitive rulesets on Slippi for Windows.

Overall package is broken into a group of scripts for generating data and files to store them

## get_data
scripts on the backend to aggregate and store data

### parse_data
- identifies all .slp game files from a given root directory
- checks against a list of processed files to avoid redundant processing
- generates a Pandas DataFrame of metadata (filepath, date, game duration in frames, stage, tags, characters, end stocks and damage, and quit-outs)
- pushes datasets to SQL database
- saves a list of processed files by path into a csv

### build_db
- SQLite database tables to contain data scraped with the parser

## slippi_dash
- Django application to interactively display game data