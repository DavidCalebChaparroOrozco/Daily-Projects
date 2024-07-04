from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'secret_key'

DATA_DIR = 'data'
BOOKS_FILE = os.path.join(DATA_DIR, 'books.json')
MEMBERS_FILE = os.path.join(DATA_DIR, 'members.json')
LOANS_FILE = os.path.join(DATA_DIR, 'loans.json')

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Initialize JSON files if they don't exist
for file in [BOOKS_FILE, MEMBERS_FILE, LOANS_FILE]:
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump([], f)


def load_data(file):
    with open(file, 'r') as f:
        return json.load(f)


def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books')
def books():
    books = load_data(BOOKS_FILE)
    return render_template('books.html', books=books)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        books = load_data(BOOKS_FILE)
        books.append({'title': title, 'author': author})
        save_data(BOOKS_FILE, books)
        flash('Book added successfully!', 'success')
        return redirect(url_for('books'))
    return render_template('add_book.html')


@app.route('/members')
def members():
    members = load_data(MEMBERS_FILE)
    return render_template('members.html', members=members)


@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        name = request.form['name']
        members = load_data(MEMBERS_FILE)
        members.append({'name': name})
        save_data(MEMBERS_FILE, members)
        flash('Member added successfully!', 'success')
        return redirect(url_for('members'))
    return render_template('add_member.html')


@app.route('/loans')
def loans():
    loans = load_data(LOANS_FILE)
    return render_template('loans.html', loans=loans)


@app.route('/loan_book', methods=['POST'])
def loan_book():
    book_title = request.form['book_title']
    member_name = request.form['member_name']
    loans = load_data(LOANS_FILE)
    loans.append({'book_title': book_title, 'member_name': member_name})
    save_data(LOANS_FILE, loans)
    flash('Book loaned successfully!', 'success')
    return redirect(url_for('loans'))


@app.route('/return_book', methods=['POST'])
def return_book():
    book_title = request.form['book_title']
    member_name = request.form['member_name']
    loans = load_data(LOANS_FILE)
    loans = [loan for loan in loans if not (loan['book_title'] == book_title and loan['member_name'] == member_name)]
    save_data(LOANS_FILE, loans)
    flash('Book returned successfully!', 'success')
    return redirect(url_for('loans'))


if __name__ == '__main__':
    app.run(debug=True)
