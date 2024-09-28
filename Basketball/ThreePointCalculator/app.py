from flask import Flask, render_template, request, redirect, url_for, session
import secrets

# Generate a random secret key
secret_key = secrets.token_hex(16)
print(secret_key)


app = Flask(__name__)
app.secret_key = secret_key

# Home route to display the form
@app.route('/', methods=['GET', 'POST'])
def three_point_calculator():
    if 'history' not in session:
        session['history'] = []  # Initialize history in session if not present

    percentage = None
    if request.method == 'POST':
        try:
            # Get the number of attempted and successful 3-point shots
            attempted = int(request.form['attempted'])
            made = int(request.form['made'])

            # Input validation
            if attempted <= 0 or made <= 0 or made > attempted:
                raise ValueError("Invalid values! Made shots cannot exceed attempted shots, and values must be non-negative.")

            # Calculate the success percentage
            percentage = (made / attempted) * 100 if attempted > 0 else 0

            # Save the result to history
            session['history'].append({
                'attempted': attempted,
                'made': made,
                'percentage': round(percentage, 2)
            })
            session.modified = True

        except ValueError as e:
            percentage = str(e)

    return render_template('index.html', percentage=percentage, history=session['history'])

# Route to clear the session history
@app.route('/reset', methods=['GET'])
def reset():
    session.clear()  # Clear all session data
    return redirect(url_for('three_point_calculator'))

if __name__ == '__main__':
    app.run(debug=True)
