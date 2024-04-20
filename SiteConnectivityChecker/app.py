# Importing necessary libraries
from flask import Flask, render_template, request
import requests
import validators
import logging

# Creating Flask App instance
app = Flask(__name__, template_folder='templates')

# Configuring logging
logging.basicConfig(filename='activity.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to check if URL is valid
def is_valid_url(url):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    return validators.url(url)

# Route to render index.html
@app.route('/')
def index():
    return render_template("index.html")

# Route to handle URL checking
@app.route('/check', methods=['POST'])
def check():
    url = request.form.get('url')

    # Validate the URL
    try:
        if not is_valid_url(url):
            return render_template('error.html', error_message=f"Invalid URL '{url}': No scheme supplied. Perhaps you meant https://{url}?")
    except validators.ValidationFailure:
        return render_template('error.html', error_message=f"Invalid URL '{url}': No scheme supplied. Perhaps you meant https://{url}?")
        
    try:
        # Check the connectivity of the URL
        response = requests.get(url, timeout=10)
        if response.status_code < 400:
            status = 'UP'
        else:
            status = 'DOWN'

    except requests.Timeout:
        return render_template('error.html', error_message='Connection timeout')
    except requests.ConnectionError:
        return render_template('error.html', error_message='Connection error')
    except requests.RequestException as e:
        return render_template('error.html', error_message=str(e))
    
    # Log the activity
    log_message = f"URL: {url}, Status: {status}"
    logging.info(log_message)
    
    # Render the results template
    return render_template('results.html', url=url, status=status)

# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)