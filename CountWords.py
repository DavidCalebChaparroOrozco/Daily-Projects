# Importing necessary libraries
import tkinter as tk

# Function to count the number of words and characters in the input text.
def count_words():
    # Get the text from the text box
    text = text_box.get("1.0", tk.END).strip()
    
    # Split the text into words
    words = text.split()
    
    # Count the number of words and characters
    word_count = len(words)
    char_count = len(text)
    
    # Update the labels with the counts
    result_label.config(text=f"Word Count: {word_count}")
    char_label.config(text=f"Character Count: {char_count}")

# Function to clear the text box and reset counts.
def clear_text():
    text_box.delete("1.0", tk.END)  # Clear the text box
    result_label.config(text="Word Count: 0")  # Reset word count
    char_label.config(text="Character Count: 0")  # Reset character count

# Create the main window
root = tk.Tk()
root.title("Word Counter")
root.configure(bg="#2E2E2E")  # Dark background color

# Create a label for instructions
instruction_label = tk.Label(root, text="Enter your text below:", bg="#2E2E2E", fg="white")
instruction_label.pack(pady=10)

# Create a text box for user input
text_box = tk.Text(root, height=10, width=50, bg="#3C3C3C", fg="white", insertbackground='white')
text_box.pack(pady=10)

# Create a button to count words
count_button = tk.Button(root, text="Count Words", command=count_words, bg="#4CAF50", fg="white")
count_button.pack(pady=5)

# Create a button to clear text
clear_button = tk.Button(root, text="Clear Text", command=clear_text, bg="#F44336", fg="white")
clear_button.pack(pady=5)

# Create labels to display results
result_label = tk.Label(root, text="Word Count: 0", bg="#2E2E2E", fg="white")
result_label.pack(pady=5)

char_label = tk.Label(root, text="Character Count: 0", bg="#2E2E2E", fg="white")
char_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()