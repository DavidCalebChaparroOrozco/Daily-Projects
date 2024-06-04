from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# List of roulette options
options = []

@app.route('/')
def index():
    return render_template('index.html', options=options)

@app.route('/spin')
def spin():
    if options:
        selected_option = random.choice(options)
    else:
        selected_option = None
    return render_template('index.html', options=options, selected_option=selected_option)

@app.route('/add', methods=['GET', 'POST'])
def add_option():
    if request.method == 'POST':
        new_option = request.form['option']
        if new_option:
            options.append(new_option)
        return redirect(url_for('index'))
    return render_template('add_option.html')

@app.route('/modify', methods=['GET', 'POST'])
def modify_options():
    if request.method == 'POST':
        new_options = request.form.getlist('options')
        global options
        # Filter empty options
        options = [opt for opt in new_options if opt]  
        return redirect(url_for('index'))
    return render_template('modify_options.html', options=options)

if __name__ == '__main__':
    app.run(debug=True)
