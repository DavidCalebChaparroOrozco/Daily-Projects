# Importing necessary libraries
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import uuid

# Initialize the Flask application
app = Flask(__name__)

# Global list to store tickets and a variable for the current ticket
tickets = []
current_ticket = None

# Define the Ticket class
class Ticket:
    def __init__(self, name):
        # Assign a unique ID to the ticket using uuid and truncate to 6 uppercase characters
        self.id = uuid.uuid4().hex[:6].upper()
        # Assign the client's name to the ticket
        self.name = name
        # Assign the current timestamp to the ticket
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Route for the home page
@app.route('/')
def index():
    # Render the HTML template for the client
    return render_template('client.html')

# Route to create a new ticket
@app.route('/create_ticket', methods=['POST'])
def create_ticket():
    # Get the name from the submitted form
    name = request.form['name']
    # Create a new ticket with the provided name
    new_ticket = Ticket(name)
    # Add the new ticket to the list of tickets
    tickets.append(new_ticket)
    # Redirect to the ticket created confirmation page
    return redirect(url_for('ticket_created', ticket_id=new_ticket.id))

# Route to show the ticket created confirmation
@app.route('/ticket_created/<ticket_id>')
def ticket_created(ticket_id):
    # Find the ticket in the list of tickets using the provided ID
    ticket = next((t for t in tickets if t.id == ticket_id), None)
    # Render the HTML template for ticket confirmation with the ticket information
    return render_template('ticket_created.html', ticket=ticket)

# Route for the provider's page
@app.route('/provider')
def provider():
    global current_ticket
    # Select the next ticket in the list if there are tickets available
    next_ticket = tickets[0] if tickets else None
    # Render the HTML template for the provider with the current ticket and the next ticket
    return render_template('provider.html', next_ticket=next_ticket, current_ticket=current_ticket)

# Route to get the next ticket
@app.route('/next_ticket', methods=['POST'])
def next_ticket():
    global current_ticket
    # If there are tickets available, assign the first ticket in the list as the current ticket and remove it from the list
    if tickets:
        current_ticket = tickets.pop(0)
    # Redirect to the provider's page
    return redirect(url_for('provider'))

# Run the application in debug mode
if __name__ == '__main__':
    app.run(debug=True)