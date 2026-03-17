import sqlite3
import os

def create_connection():

    con = sqlite3.connect('data/financas.db')
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT,
                descricao TEXT,
                valor REAL,
                tipo TEXT,
                categoria TEXT
                )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS wishes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ativo TEXT,
                quantidade INTEGER,
                preco_medio REAL,
                )
    ''')

    con.commit()
    con.close()

    print("Database and tables created successfully.")

    if __name__ == "__main__":
        create_connection()