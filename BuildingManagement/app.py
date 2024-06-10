# Importing necessary libraries
import sqlite3
import datetime

# Create the database schema
def create_database():
    conn = sqlite3.connect('building_management.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Proprietor (
        id INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT,
        email TEXT,
        phone TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Property (
        code INTEGER PRIMARY KEY,
        area REAL,
        type TEXT,
        proprietor_id INTEGER,
        FOREIGN KEY (proprietor_id) REFERENCES Proprietor(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ownership (
        proprietor_id INTEGER,
        property_code INTEGER,
        percentage REAL,
        balance REAL,
        PRIMARY KEY (proprietor_id, property_code),
        FOREIGN KEY (proprietor_id) REFERENCES Proprietor(id),
        FOREIGN KEY (property_code) REFERENCES Property(code)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS GeneralBudget (
        year INTEGER PRIMARY KEY,
        value REAL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ExtraQuota (
        code INTEGER PRIMARY KEY,
        month INTEGER,
        purpose TEXT,
        value REAL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Invoice (
        code INTEGER PRIMARY KEY AUTOINCREMENT,
        proprietor_id INTEGER,
        property_code INTEGER,
        month INTEGER,
        year INTEGER,
        amount_due REAL,
        overdue_balance REAL,
        late_fee REAL,
        FOREIGN KEY (proprietor_id) REFERENCES Proprietor(id),
        FOREIGN KEY (property_code) REFERENCES Property(code)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Payment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        proprietor_id INTEGER,
        property_code INTEGER,
        payment_date DATE,
        amount_paid REAL,
        FOREIGN KEY (proprietor_id) REFERENCES Proprietor(id),
        FOREIGN KEY (property_code) REFERENCES Property(code)
    )
    ''')

    conn.commit()
    conn.close()

# Function to generate monthly invoices
def generate_invoice(proprietor_id, property_code, month, year):
    conn = sqlite3.connect('building_management.db')
    cursor = conn.cursor()

    # Get general budget
    cursor.execute('SELECT value FROM GeneralBudget WHERE year = ?', (year,))
    budget = cursor.fetchone()
    if not budget:
        print(f"No budget found for the year {year}")
        return
    budget_value = budget[0]

    # Get property area
    cursor.execute('SELECT area FROM Property WHERE code = ?', (property_code,))
    property_area = cursor.fetchone()[0]

    # Calculate monthly amount
    monthly_amount = (budget_value * property_area) / 12

    # Get overdue balance and late fee
    cursor.execute('''
    SELECT SUM(amount_due), SUM(late_fee)
    FROM Invoice
    WHERE proprietor_id = ? AND property_code = ? AND (year < ? OR (year = ? AND month < ?))
    ''', (proprietor_id, property_code, year, year, month))
    overdue_balance, late_fee = cursor.fetchone()

    if overdue_balance is None:
        overdue_balance = 0
    if late_fee is None:
        late_fee = 0

    # Calculate new late fee
    new_late_fee = overdue_balance * 0.015

    # Create invoice
    cursor.execute('''
    INSERT INTO Invoice (proprietor_id, property_code, month, year, amount_due, overdue_balance, late_fee)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (proprietor_id, property_code, month, year, monthly_amount, overdue_balance, new_late_fee))

    conn.commit()
    conn.close()

# Function to make a payment
def make_payment(proprietor_id, property_code, payment_date, amount_paid):
    conn = sqlite3.connect('building_management.db')
    cursor = conn.cursor()

    # Record payment
    cursor.execute('''
    INSERT INTO Payment (proprietor_id, property_code, payment_date, amount_paid)
    VALUES (?, ?, ?, ?)
    ''', (proprietor_id, property_code, payment_date, amount_paid))

    # Update balance
    cursor.execute('''
    UPDATE Ownership
    SET balance = balance - ?
    WHERE proprietor_id = ? AND property_code = ?
    ''', (amount_paid, proprietor_id, property_code))

    conn.commit()
    conn.close()

# Function to get account statement
def get_account_statement(proprietor_id, start_date, end_date):
    conn = sqlite3.connect('building_management.db')
    cursor = conn.cursor()

    # Get payments
    cursor.execute('''
    SELECT payment_date, amount_paid
    FROM Payment
    WHERE proprietor_id = ? AND payment_date BETWEEN ? AND ?
    ''', (proprietor_id, start_date, end_date))
    payments = cursor.fetchall()

    # Get invoices
    cursor.execute('''
    SELECT year, month, amount_due, overdue_balance, late_fee
    FROM Invoice
    WHERE proprietor_id = ? AND (year || '-' || month || '-01') BETWEEN ? AND ?
    ''', (proprietor_id, start_date, end_date))
    invoices = cursor.fetchall()

    conn.close()

    return {'payments': payments, 'invoices': invoices}

# Function to get monthly payments and total
def get_monthly_payments(month, year):
    conn = sqlite3.connect('building_management.db')
    cursor = conn.cursor()

    # Get payments and total
    cursor.execute('''
    SELECT proprietor_id, property_code, payment_date, amount_paid
    FROM Payment
    WHERE strftime('%m', payment_date) = ? AND strftime('%Y', payment_date) = ?
    ''', (str(month).zfill(2), str(year)))
    payments = cursor.fetchall()

    cursor.execute('''
    SELECT SUM(amount_paid)
    FROM Payment
    WHERE strftime('%m', payment_date) = ? AND strftime('%Y', payment_date) = ?
    ''', (str(month).zfill(2), str(year)))
    total = cursor.fetchone()[0]

    conn.close()

    return {'payments': payments, 'total': total}

# Function to get delinquent apartments
def get_delinquent_apartments():
    conn = sqlite3.connect('building_management.db')
    cursor = conn.cursor()

    # Get delinquent apartments
    cursor.execute('''
    SELECT property_code, COUNT(*)
    FROM Invoice
    WHERE amount_due > 0 AND (julianday('now') - julianday(year || '-' || month || '-01')) / 30 > 3
    GROUP BY property_code
    HAVING COUNT(*) > 3
    ''')
    delinquent_apartments = cursor.fetchall()

    conn.close()

    return delinquent_apartments

# Add sample data
def add_sample_data():
    conn = sqlite3.connect('building_management.db')
    cursor = conn.cursor()

    # Add proprietors
    proprietors = [
        (1, 'David Caleb Chaparro Orozco', '123 Maple Street', 'david@example.com', '555-0100'),
        (2, 'Philip J. Fry', '456 Elm Street', 'fry@example.com', '555-0200'),
        (3, 'Rick Sanchez', '789 Oak Street', 'rick@example.com', '555-0300'),
        (4, 'Bender Bending Rodríguez', '101 Pine Street', 'bender@example.com', '555-0400'),
        (5, 'Elliot Alderson', '202 Birch Street', 'elliot@example.com', '555-0500')
    ]
    cursor.executemany("INSERT INTO Proprietor (id, name, address, email, phone) VALUES (?, ?, ?, ?, ?)", proprietors)

    # Add properties
    properties = [
        (101, 150.0, 'apartment', 1),
        (102, 75.0, 'garage', 2),
        (103, 50.0, 'storage', 3),
        (104, 120.0, 'apartment', 4),
        (105, 200.0, 'apartment', 5)
    ]
    cursor.executemany("INSERT INTO Property (code, area, type, proprietor_id) VALUES (?, ?, ?, ?)", properties)

    # Add ownerships
    ownerships = [
        (1, 101, 100, 0),
        (2, 102, 100, 0),
        (3, 103, 100, 0),
        (4, 104, 100, 0),
        (5, 105, 100, 0)
    ]
    cursor.executemany("INSERT INTO Ownership (proprietor_id, property_code, percentage, balance) VALUES (?, ?, ?, ?)", ownerships)

    # Add general budgets
    budgets = [
        (2024, 120000.0),
        (2025, 125000.0)
    ]
    cursor.executemany("INSERT INTO GeneralBudget (year, value) VALUES (?, ?)", budgets)

    conn.commit()
    conn.close()

# Example usage of the functions
if __name__ == '__main__':
    create_database()
    add_sample_data()

    # Generate invoices for June 2024
    generate_invoice(1, 101, 6, 2024)
    generate_invoice(2, 102, 6, 2024)
    generate_invoice(3, 103, 6, 2024)
    generate_invoice(4, 104, 6, 2024)
    generate_invoice(5, 105, 6, 2024)

    # Make some payments
    make_payment(1, 101, '2024-06-10', 500)
    make_payment(2, 102, '2024-06-11', 200)
    make_payment(3, 103, '2024-06-12', 100)
    make_payment(4, 104, '2024-06-13', 300)
    make_payment(5, 105, '2024-06-14', 700)

    # Get account statement for David Caleb Chaparro Orozco
    statement = get_account_statement(1, '2024-01-01', '2024-12-31')
    print("Account Statement for David Caleb Chaparro Orozco:", statement)

    # Get monthly payments and total for June 2024
    monthly_report = get_monthly_payments(6, 2024)
    print("Monthly Payments for June 2024:", monthly_report)

    # Get delinquent apartments
    delinquents = get_delinquent_apartments()
    print("Delinquent Apartments:", delinquents)
