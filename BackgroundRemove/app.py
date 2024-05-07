# Importing necessary libraries
import cv2
import os
from rembg import remove
from PIL import Image
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template

UPLOAD_FOLDER = 'static/uploads'
EXTENSIONS = set(['png', 'jpg', 'jpeg', 'webp'])

# Create necessary directories if they don't exist.
if 'static' not in os.listdir('.'):
    os.mkdir('static')

if 'uploads' not in os.listdir('static/'):
    os.mkdir('static/uploads')

app = Flask(__name__)
# Set caching behavior to disable caching.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# Set the upload folder configuration.
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if a file has an allowed extension.
def allowed_file(file):
    return '.' in file and file.rsplit('.',1)[1] in EXTENSIONS

# Function to remove background from an image.
def remove_background(input_path, output_path):
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)

@app.route('/')
def home():
    return render_template('index.html')

# Route for background removal process.
@app.route('/remback',methods=["POST"])
def remback():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        rembg_img_name = filename.split('.')[0]+"_rembg.png"
        remove_background(UPLOAD_FOLDER+'/'+filename,UPLOAD_FOLDER+'/'+rembg_img_name)
        return render_template('index.html',org_img_name=filename,rembg_img_name=rembg_img_name)

if __name__ == "__main__":
    app.run(debug=True)