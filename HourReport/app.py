# Importing necessary libraries
from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize the database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hours (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            task TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# User authentication functions
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['user_id'] = user[0]
            return redirect(url_for('index'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM hours WHERE user_id = ?', (user_id,))
    hours = cursor.fetchall()
    conn.close()

    total_hours = 0
    hours_with_durations = []

    for hour in hours:
        start_time = datetime.strptime(hour[3], '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(hour[4], '%Y-%m-%d %H:%M:%S')
        duration = (end_time - start_time).seconds // 3600
        total_hours += duration
        hours_with_durations.append((hour[0], hour[2], start_time, end_time, duration))
    
    return render_template('index.html', hours=hours_with_durations, total_hours=total_hours)

def is_valid_time(start_datetime):
    # Check if the day is a weekday (Monday to Friday)
    if start_datetime.weekday() >= 5:
        return False
    
    # Check if the time is between 06:00 and 23:00
    if start_datetime.hour < 6 or start_datetime.hour >= 23:
        return False
    
    return True

@app.route('/log', methods=['GET', 'POST'])
def log_hours():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        user_id = session['user_id']
        task = request.form['task']
        start_time = request.form['start_time']
        
        # Convert start_time to datetime
        start_datetime = datetime.strptime(start_time, '%Y-%m-%dT%H:%M')
        
        # Validate the start time
        if not is_valid_time(start_datetime):
            flash('Only weekdays (Monday to Friday) between 06:00 and 23:00 are allowed.')
            return redirect(url_for('log_hours'))
        
        # End time is always one hour later
        end_datetime = start_datetime + timedelta(hours=1)
        end_time = end_datetime.strftime('%Y-%m-%d %H:%M:%S')
        start_time = start_datetime.strftime('%Y-%m-%d %H:%M:%S')
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO hours (user_id, task, start_time, end_time)
            VALUES (?, ?, ?, ?)
        ''', (user_id, task, start_time, end_time))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('log_hours.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_hours(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    if request.method == 'POST':
        task = request.form['task']
        start_time = request.form['start_time']
        
        # Convert start_time to datetime
        start_datetime = datetime.strptime(start_time, '%Y-%m-%dT%H:%M')
        
        # Validate the start time
        if not is_valid_time(start_datetime):
            flash('Only weekdays (Monday to Friday) between 06:00 and 23:00 are allowed.')
            return redirect(url_for('edit_hours', id=id))
        
        # End time is always one hour later
        end_datetime = start_datetime + timedelta(hours=1)
        end_time = end_datetime.strftime('%Y-%m-%d %H:%M:%S')
        start_time = start_datetime.strftime('%Y-%m-%d %H:%M:%S')
        
        cursor.execute('''
            UPDATE hours SET task = ?, start_time = ?, end_time = ? WHERE id = ?
        ''', (task, start_time, end_time, id))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    cursor.execute('SELECT * FROM hours WHERE id = ?', (id,))
    record = cursor.fetchone()
    conn.close()
    
    return render_template('edit_hours.html', record=record)

@app.route('/clear_hours', methods=['POST'])
def clear_hours():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM hours WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
