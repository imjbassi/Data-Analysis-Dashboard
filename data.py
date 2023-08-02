import os
import sqlite3

def create_table():
    db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.db')
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT, value INTEGER)')
    conn.commit()
    conn.close()

def insert_sample_data():
    db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.db')
    data = [
        ('A', 10),
        ('B', 20),
        ('C', 15)
    ]
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO data (name, value) VALUES (?, ?)', data)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
    insert_sample_data()
