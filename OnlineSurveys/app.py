from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///polls.db'
db = SQLAlchemy(app)

# Model for Poll
class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    option1 = db.Column(db.String(100), nullable=False)
    option2 = db.Column(db.String(100), nullable=False)
    option1_votes = db.Column(db.Integer, default=0)
    option2_votes = db.Column(db.Integer, default=0)

# Home route to display all polls
@app.route('/')
def index():
    polls = Poll.query.all()
    return render_template('index.html', polls=polls)

# Route to create a new poll
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        question = request.form['question']
        option1 = request.form['option1']
        option2 = request.form['option2']
        if not question or not option1 or not option2:
            flash('Please enter all fields', 'danger')
            return redirect(url_for('create'))
        new_poll = Poll(question=question, option1=option1, option2=option2)
        db.session.add(new_poll)
        db.session.commit()
        flash('Poll created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('create.html')

# Route to vote on a poll
@app.route('/vote/<int:poll_id>', methods=['GET', 'POST'])
def vote(poll_id):
    poll = Poll.query.get_or_404(poll_id)
    if request.method == 'POST':
        vote = request.form['vote']
        if vote == 'option1':
            poll.option1_votes += 1
        elif vote == 'option2':
            poll.option2_votes += 1
        db.session.commit()
        flash('Vote cast successfully!', 'success')
        return redirect(url_for('results', poll_id=poll.id))
    return render_template('vote.html', poll=poll)

# Route to show results of a poll
@app.route('/results/<int:poll_id>')
def results(poll_id):
    poll = Poll.query.get_or_404(poll_id)
    return render_template('results.html', poll=poll)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
