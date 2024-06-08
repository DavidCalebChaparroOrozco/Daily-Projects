# # Importing necessary libraries
# from docx2pdf import convert

# convert("HelloWorld.docx", "output.pdf")

# Importing necessary libraries
import tkinter as tk
from tkinter import filedialog, messagebox
from docx2pdf import convert
import os

def convert_to_pdf():
    """
    This function handles the conversion of a single DOCX file to PDF.
    It opens a file dialog for the user to select a DOCX file, then opens a save dialog to specify the output PDF file.
    If both selections are successful, it converts the DOCX file to PDF using the docx2pdf library and shows a success message.
    If any error occurs during the process, it shows an error message.
    """
    try:
        # Open a file dialog for the user to select a DOCX file
        input_path = filedialog.askopenfilename(
            title="Select DOCX file",
            filetypes=(("Word Documents", "*.docx"), ("All Files", "*.*"))
        )
        if not input_path:
            # User cancelled file selection
            return  

        # Open a save dialog for the user to specify the output PDF file
        output_path = filedialog.asksaveasfilename(
            title="Save PDF as",
            defaultextension=".pdf",
            filetypes=(("PDF files", "*.pdf"), ("All Files", "*.*"))
        )
        if not output_path:
            # User cancelled save dialog
            return  

        # Convert the selected DOCX file to PDF
        convert(input_path, output_path)
        
        # Show a success message
        messagebox.showinfo("Success", f"File converted successfully to {output_path}")
    except Exception as e:
        # Show an error message if any exception occurs
        messagebox.showerror("Error", f"An error occurred: {e}")

def convert_multiple_to_pdf():
    """
    This function handles the conversion of multiple DOCX files to PDF.
    It opens a file dialog for the user to select multiple DOCX files, then opens a directory dialog to specify the output directory.
    For each selected DOCX file, it converts the file to PDF and saves it in the specified directory.
    If the process is successful, it shows a success message. If any error occurs, it shows an error message.
    """
    try:
        # Open a file dialog for the user to select multiple DOCX files
        input_paths = filedialog.askopenfilenames(
            title="Select DOCX files",
            filetypes=(("Word Documents", "*.docx"), ("All Files", "*.*"))
        )
        if not input_paths:
            # User cancelled file selection
            return  

        # Open a directory dialog for the user to specify the output directory
        output_dir = filedialog.askdirectory(
            title="Select Output Directory"
        )
        if not output_dir:
            # User cancelled directory selection
            return  

        # Convert each selected DOCX file to PDF and save it in the specified directory
        for input_path in input_paths:
            output_path = os.path.join(output_dir, os.path.splitext(os.path.basename(input_path))[0] + '.pdf')
            convert(input_path, output_path)

        # Show a success message
        messagebox.showinfo("Success", "Files converted successfully")
    except Exception as e:
        # Show an error message if any exception occurs
        messagebox.showerror("Error", f"An error occurred: {e}")

# Setting up the GUI
root = tk.Tk()
root.title("DOCX to PDF Converter by David Caleb")
root.geometry("400x100")

# Single file conversion
btn_single = tk.Button(root, text="Convert Single DOCX to PDF", command=convert_to_pdf)
btn_single.pack(pady=10)

# Multiple files conversion
btn_multiple = tk.Button(root, text="Convert Multiple DOCX to PDF", command=convert_multiple_to_pdf)
btn_multiple.pack(pady=10)

root.mainloop()
