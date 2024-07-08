# Importing necessary libraries
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from stegano import lsb
import os

# Creating a Flask app instance
app = Flask(__name__)

# Configuring the upload and secret image folders
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['SECRET_FOLDER'] = 'static/secret_images'

# Ensuring the upload and secret directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['SECRET_FOLDER'], exist_ok=True)

# Route for the main index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling the image hiding functionality
@app.route('/hide', methods=['POST', 'GET'])
def hide():
    if request.method == 'POST':
        # Check if the required form fields are present
        if 'image' not in request.files or 'message' not in request.form:
            return redirect(url_for('index'))
        
        # Get the image and message from the form
        image = request.files['image']
        message = request.form['message']
        
        # Ensure an image file was selected
        if not image or image.filename == '':
            return redirect(url_for('index'))
        
        # Save the uploaded image to the upload folder
        image_filename = secure_filename(image.filename) if image.filename else 'default.png'
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
        image.save(image_path)
        
        # Generate the output filename and path for the steganographed image
        output_filename = 'secret_' + image_filename
        output_path = os.path.join(app.config['SECRET_FOLDER'], output_filename)
        
        try:
            # Hide the message in the image using the Stegano library
            secret_image = lsb.hide(image_path, message)
            secret_image.save(output_path)
            
            # Render the 'hide.html' template with the hidden message and image URL
            return render_template('hide.html', image_url=url_for('static', filename=f'secret_images/{output_filename}'), message=message)
        except Exception as e:
            # Handle any errors that occur during the hiding process
            return f"An error occurred while hiding the message: {str(e)}. <a href='/'>Go back</a>"
    
    # If the request method is GET, redirect to the index page
    return redirect(url_for('index'))

# Route for handling the image revealing functionality
@app.route('/reveal', methods=['POST', 'GET'])
def reveal():
    if request.method == 'POST':
        # Check if the image file is present in the form
        if 'image' not in request.files:
            return redirect(url_for('index'))
        
        # Get the uploaded image
        image = request.files['image']
        
        # Ensure an image file was selected
        if not image or image.filename == '':
            return redirect(url_for('index'))
        
        # Save the uploaded image to the upload folder
        image_filename = secure_filename(image.filename) if image.filename else 'default.png'
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
        image.save(image_path)
        
        # Check if the image file exists at the specified path
        if not os.path.exists(image_path):
            return f"The image at path {image_path} does not exist. <a href='/'>Go back</a>"
        
        try:
            # Reveal the hidden message from the image using the Stegano library
            revealed_text = lsb.reveal(image_path)
            if revealed_text is not None:
                # Render the 'reveal.html' template with the revealed message and image URL
                return render_template('reveal.html', image_url=url_for('static', filename=f'uploads/{image_filename}'), message=revealed_text)
            else:
                # If no hidden message is detected, display a message
                return "No hidden message detected in the image. <a href='/'>Go back</a>"
        except Exception as e:
            # Handle any errors that occur during the revealing process
            return f"An error occurred while revealing the message: {str(e)}. <a href='/'>Go back</a>"
    
    # If the request method is GET, redirect to the index page
    return redirect(url_for('index'))

# Run the Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)