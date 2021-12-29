from configparser import ConfigParser
config = ConfigParser()

config.read('config.ini')
config.add_section('player')
config.set()