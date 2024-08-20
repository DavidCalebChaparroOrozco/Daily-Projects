# Importing necessary libraries
import tkinter as tk  
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageDraw, ImageTk

# Function to load an image from the file system
def load_image():
    # Open a file dialog to select an image file
    image_path = filedialog.askopenfilename(
        title="Select an Image", 
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    # If no file is selected, return None
    if not image_path:  
        return None
    try:
        # Open the image and convert it to RGB format
        img = Image.open(image_path)
        img = img.convert("RGB")
        # Return the image object and the file path
        return img, image_path

    # Handle any errors that occur during image loading
    except Exception as e:  
        messagebox.showerror("Error", f"Error loading image: {e}")
        return None

# Function to apply the floodfill operation on the image
def apply_floodfill(img, target_pixel, target_color, thresh=0):
    try:
        # Perform floodfill on the image at the specified pixel with the chosen color
        ImageDraw.floodfill(img, target_pixel, target_color, thresh=thresh)
    except Exception as e:  # Handle any errors that occur during floodfill
        messagebox.showerror("Error", f"Error during floodfill: {e}")
        return None

# Function to save the modified image
def save_image(img):
    # Open a save file dialog to specify the output file path and format
    output_path = filedialog.asksaveasfilename(
        defaultextension=".png", 
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
    )
    # If the user specifies a file path
    if output_path:  
        try:
            # Save the image to the specified file path
            img.save(output_path)
            messagebox.showinfo("Image Saved", f"Image saved as {output_path}")
        # Handle any errors that occur during image saving
        except Exception as e:  
            messagebox.showerror("Error", f"Error saving image: {e}")

# Function to handle the event when the "Open Image" button is clicked
def on_open_image():
    # Use global variables to store the image and its path
    global img, img_path, img_tk  
    # Load the selected image
    result = load_image()  
    # If an image was successfully loaded
    if result:  
        # Store the image and its path
        img, img_path = result  
        # Convert the image to a format suitable for displaying in Tkinter
        img_tk = ImageTk.PhotoImage(img)
        # Display the image on the canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        # Adjust the canvas size to fit the image dimensions
        canvas.config(width=img.width, height=img.height)

# Function to handle the event when the "Apply Floodfill" button is clicked
def on_floodfill():
    # Use global variables for the image and its display format
    global img, img_tk  
    # If no image is loaded, show a warning
    if img is None:  
        messagebox.showwarning("No Image", "Please load an image first.")
        return

    # Open a color chooser dialog to select the fill color
    target_color = colorchooser.askcolor()[0]
    # If no color is selected, return
    if target_color is None:  
        return
    
    # Default pixel location for floodfill; adjust as needed
    target_pixel = (500, 310)  

    # Check if the target pixel is within the image bounds
    if target_pixel[0] >= img.width or target_pixel[1] >= img.height:
        messagebox.showwarning("Invalid Pixel", "The target pixel is out of the image range.")
        return

    # Convert the selected color to an integer tuple
    target_color = tuple(map(int, target_color))
    # Apply the floodfill operation to the image
    apply_floodfill(img, target_pixel, target_color)
    # Update the image on the canvas with the modified image
    img_tk = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

# Function to handle the event when the "Save Image" button is clicked
def on_save_image():
    # If no image is loaded, show a warning
    if img is None:  
        messagebox.showwarning("No Image", "Please load an image first.")
        return
    # Save the modified image
    save_image(img) 

# Main GUI setup
root = tk.Tk()  
root.title("Floodfill Image Color Changer by David Caleb")
root.configure(bg='#333333')  # Set the background color to dark gray

# Create a canvas widget to display the image
canvas = tk.Canvas(root, bg='#333333')  # Set the canvas background color to dark gray
canvas.pack()

# Initialize global variables to store image data
img = None
img_path = None
img_tk = None

# Create and pack the "Open Image" button
btn_open = tk.Button(root, text="Open Image", command=on_open_image, bg='#4CAF50', fg='white', font=('Arial', 12))
btn_open.pack(side=tk.LEFT, padx=10, pady=10)

# Create and pack the "Apply Floodfill" button
btn_floodfill = tk.Button(root, text="Apply Floodfill", command=on_floodfill, bg='#2196F3', fg='white', font=('Arial', 12))
btn_floodfill.pack(side=tk.LEFT, padx=10, pady=10)

# Create and pack the "Save Image" button
btn_save = tk.Button(root, text="Save Image", command=on_save_image, bg='#E91E63', fg='white', font=('Arial', 12))
btn_save.pack(side=tk.LEFT, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()