from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Create DB + table if it doesn't exist
if not os.path.exists('data.db'):
    conn = sqlite3.connect('data.db')
    conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('data.db')
    conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))  # Redirect back to index page

if __name__ == '__main__':
    app.run(debug=True)
