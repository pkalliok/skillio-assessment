from .config import config
import psycopg2

conn = psycopg2.connect(**config(filename='src/data/database.ini'))

