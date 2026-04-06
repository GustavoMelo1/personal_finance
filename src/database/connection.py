import sqlite3

PATH_db = 'data/financas.db'

def create_connection():
    conn = sqlite3.connect(PATH_db)
    return conn