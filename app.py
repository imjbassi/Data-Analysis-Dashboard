# app.py

from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
def connect_db():
    return sqlite3.connect('data.db')

# Sample data for demonstration purposes
def insert_sample_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT, value INTEGER)')
    cursor.execute('INSERT INTO data (name, value) VALUES ("A", 10)')
    cursor.execute('INSERT INTO data (name, value) VALUES ("B", 20)')
    cursor.execute('INSERT INTO data (name, value) VALUES ("C", 15)')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data')
    data = [{'name': row[1], 'value': row[2]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    insert_sample_data()  # Insert sample data before running the app
    app.run(debug=True)
