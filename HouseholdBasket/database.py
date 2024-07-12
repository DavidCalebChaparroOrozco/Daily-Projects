# Importing necessary libraries
import sqlite3

# Create a connection to the SQLite database
def create_connection():
    conn = sqlite3.connect('household_basket.db')
    return conn

# Create the household_basket table if it does not exist
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS household_basket (
            id INTEGER PRIMARY KEY,
            category TEXT NOT NULL,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Insert an item into the household_basket table
def insert_item(category, name, quantity):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO household_basket (category, name, quantity) VALUES (?, ?, ?)
    ''', (category, name, quantity))
    conn.commit()
    conn.close()

# Retrieve all items from the household_basket table
def get_items():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM household_basket')
    items = cursor.fetchall()
    conn.close()
    return items

# Delete an item from the household_basket table
def delete_item(item_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM household_basket WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
