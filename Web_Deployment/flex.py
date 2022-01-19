from flask import Flask, render_template
import sqlite3
from werkzeug.exceptions import abort

app=Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

#To run
#   set FLASK_APP=flex.py
#   set FLASK_ENV=development
#   flask run -h 0.0.0.0 -p 80
