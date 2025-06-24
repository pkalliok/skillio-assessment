from configparser import ConfigParser

def config(filename='database.ini', section='postgres'):
    parser = ConfigParser()
    parser.read(filename)
    return dict(parser.items(section))

