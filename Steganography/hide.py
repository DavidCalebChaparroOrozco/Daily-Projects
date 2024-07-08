# Importing necessary libraries
from stegano import lsb

# Remplace with your desired message
message = "I would have followed you, my brother... My captain... My king."

# Path of the image you want to hide the message in
image_path = "boromir_death.png"

# Output path for the steganographed image
output_path = "secret_image.png"

# Hide the message in the image
secret_image = lsb.hide(image_path, message)

# Save the modified image
secret_image.save(output_path)
print(f"Message hidden successfully in {output_path}")

# Check if the message can be revealed immediately after hiding it
revealed_text = lsb.reveal(output_path)
print(f"Revealed text immediately after hiding: {revealed_text}")