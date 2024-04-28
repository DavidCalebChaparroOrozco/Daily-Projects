#Import necessary libraries
import tkinter as tk
from langdetect import detect
from langcodes import Language

def check_language():
    input_text = text_entry.get(1.0, tk.END).strip()
    if not input_text:
        result_label.config(text="Hey! You forgot to enter anything...")
    else:
            language_code = detect(input_text)
            language_name = Language.make(language=language_code).display_name()
            result_label.config(text=f"Detected Language: {language_name}")

# Main window settings
root = tk.Tk()
root.title('Language Detection by David Caleb')
root.geometry("500x350")

# Widget to enter text
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=20)

# Button to perform language detection
check_button = tk.Button(root, text="Check Language", command=check_language)
check_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="", wraplength=400)
result_label.pack(pady=10)

root.mainloop()