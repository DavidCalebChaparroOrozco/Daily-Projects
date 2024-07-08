# Importing necessary libraries
from stegano import lsb
import os

# Path to the image containing the hidden message
image_path = "secret_image.png"

# Extract the hidden message
if not os.path.exists(image_path):
    print(f"The image at path {image_path} does not exist.")
else:
    revealed_text = lsb.reveal(image_path)
    if revealed_text is not None:
        print(f"The hidden message is: {revealed_text}")
    else:
        print("No hidden message detected in the image.")