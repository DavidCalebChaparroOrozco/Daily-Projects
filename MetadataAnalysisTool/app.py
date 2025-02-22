# Import necessary libraries
import os
import csv
from tkinter import Tk, Button, Label, filedialog, messagebox, Listbox, MULTIPLE, Text, Scrollbar, ttk, StringVar, OptionMenu
from PIL import Image
from PIL.ExifTags import TAGS
import pdfplumber
from docx import Document
from datetime import datetime

# Logging function
def log_action(action, file_path, status="Success"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {action} - {file_path} - {status}\n"
    with open("metadata_tool_log.txt", "a") as log_file:
        log_file.write(log_entry)

# Extracts metadata from an image file using PIL (Pillow).
def extract_image_metadata(image_path):
    try:
        image = Image.open(image_path)
        metadata = {}
        
        # Extract EXIF data
        exif_data = image._getexif()
        if exif_data:
            for tag_id, value in exif_data.items():
                tag_name = TAGS.get(tag_id, tag_id)
                metadata[tag_name] = value
        
        log_action("Extract Metadata", image_path)
        return metadata
    except Exception as e:
        log_action("Extract Metadata", image_path, f"Error: {str(e)}")
        return {"error": str(e)}

# Extracts metadata from a PDF file using pdfplumber.
def extract_pdf_metadata(pdf_path):
    try:
        metadata = {}
        with pdfplumber.open(pdf_path) as pdf:
            metadata["info"] = pdf.metadata
            metadata["pages"] = len(pdf.pages)
        
        log_action("Extract Metadata", pdf_path)
        return metadata
    except Exception as e:
        log_action("Extract Metadata", pdf_path, f"Error: {str(e)}")
        return {"error": str(e)}

# Extracts metadata from a Word document (DOCX) using python-docx.
def extract_docx_metadata(docx_path):
    try:
        doc = Document(docx_path)
        metadata = {
            "author": doc.core_properties.author,
            "created": doc.core_properties.created,
            "modified": doc.core_properties.modified,
            "last_modified_by": doc.core_properties.last_modified_by,
            "revision": doc.core_properties.revision,
        }
        
        log_action("Extract Metadata", docx_path)
        return metadata
    except Exception as e:
        log_action("Extract Metadata", docx_path, f"Error: {str(e)}")
        return {"error": str(e)}

# Removes metadata from an image file by saving it without EXIF data.
def remove_metadata(image_path):
    try:
        image = Image.open(image_path)
        # Save the image without EXIF data
        image.save(image_path, "JPEG" if image_path.lower().endswith(".jpg") else "PNG")
        log_action("Remove Metadata", image_path)
        return {"status": "Metadata removed successfully"}
    except Exception as e:
        log_action("Remove Metadata", image_path, f"Error: {str(e)}")
        return {"error": str(e)}

# Analyzes metadata based on the file type.
def analyze_file(file_path):
    if file_path.lower().endswith((".jpg", ".jpeg", ".png")):
        return extract_image_metadata(file_path)
    elif file_path.lower().endswith(".pdf"):
        return extract_pdf_metadata(file_path)
    elif file_path.lower().endswith(".docx"):
        return extract_docx_metadata(file_path)
    else:
        return {"error": "Unsupported file type"}

# Opens a file dialog to select one or multiple files.
def select_files():
    file_paths = filedialog.askopenfilenames(
        title="Select Files",
        filetypes=[("All Files", "*.*"), ("Images", "*.jpg *.jpeg *.png"), ("PDFs", "*.pdf"), ("Word Documents", "*.docx")]
    )
    if file_paths:
        for file_path in file_paths:
            file_listbox.insert("end", file_path)

# Analyzes metadata for all selected files.
def analyze_files():
    if file_listbox.size() == 0:
        messagebox.showwarning("No Files Selected", "Please select one or more files to analyze.")
        return
    
    results = ""
    for i in range(file_listbox.size()):
        file_path = file_listbox.get(i)
        metadata = analyze_file(file_path)
        results += f"File: {os.path.basename(file_path)}\n"
        if "error" in metadata:
            results += f"Error: {metadata['error']}\n\n"
        else:
            for key, value in metadata.items():
                results += f"{key}: {value}\n"
            results += "\n"
    
    # Display results in the text box
    result_text.delete(1.0, "end")
    result_text.insert("end", results)

# Removes metadata from all selected image files.
def remove_metadata_from_images():
    if file_listbox.size() == 0:
        messagebox.showwarning("No Files Selected", "Please select one or more image files to remove metadata.")
        return
    
    for i in range(file_listbox.size()):
        file_path = file_listbox.get(i)
        if file_path.lower().endswith((".jpg", ".jpeg", ".png")):
            result = remove_metadata(file_path)
            if "error" in result:
                messagebox.showerror("Error", f"Failed to remove metadata from {os.path.basename(file_path)}: {result['error']}")
            else:
                messagebox.showinfo("Success", f"Metadata removed from {os.path.basename(file_path)}")
        else:
            messagebox.showwarning("Unsupported File", f"Skipping {os.path.basename(file_path)}: Metadata removal is only supported for image files.")

# Exports metadata analysis results to a file (CSV or TXT).
def export_metadata():
    if file_listbox.size() == 0:
        messagebox.showwarning("No Files Selected", "Please select one or more files to export metadata.")
        return
    
    export_format = export_format_var.get()
    if export_format not in ["CSV", "TXT"]:
        messagebox.showwarning("Invalid Format", "Please select a valid export format (CSV or TXT).")
        return
    
    file_path = filedialog.asksaveasfilename(
        defaultextension=f".{export_format.lower()}",
        filetypes=[(f"{export_format} Files", f"*.{export_format.lower()}")]
    )
    if not file_path:
        return
    
    results = []
    for i in range(file_listbox.size()):
        file_path_selected = file_listbox.get(i)
        metadata = analyze_file(file_path_selected)
        if "error" in metadata:
            results.append({"File": os.path.basename(file_path_selected), "Error": metadata["error"]})
        else:
            for key, value in metadata.items():
                results.append({"File": os.path.basename(file_path_selected), "Key": key, "Value": value})
    
    if export_format == "CSV":
        with open(file_path, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["File", "Key", "Value"])
            writer.writeheader()
            writer.writerows(results)
    else:
        with open(file_path, mode="w") as file:
            for result in results:
                file.write(f"{result}\n")
    
    messagebox.showinfo("Export Complete", f"Metadata exported successfully to {file_path}")

# Create the main window
root = Tk()
root.title("Metadata Analysis Tool by David Caleb")
root.geometry("700x600")
root.configure(bg="#2E3440")

# Custom colors
bg_color = "#2E3440" 
button_color = "#4C566A" 
text_color = "#D8DEE9" 
listbox_bg = "#3B4252" 
listbox_fg = text_color 
text_box_bg = listbox_bg 
text_box_fg = text_color 

# File selection button
select_button = Button(root, text="Select Files", command=select_files, bg=button_color, fg=text_color, font=("Arial", 12))
select_button.pack(pady=10)

# Listbox to display selected files
file_listbox = Listbox(root, selectmode=MULTIPLE, width=80, height=10, bg=listbox_bg, fg=listbox_fg, font=("Arial", 10))
file_listbox.pack(pady=10)

# Analyze button
analyze_button = Button(root, text="Analyze Metadata", command=analyze_files, bg=button_color, fg=text_color, font=("Arial", 12))
analyze_button.pack(pady=5)

# Remove metadata button (for images)
remove_button = Button(root, text="Remove Metadata (Images Only)", command=remove_metadata_from_images, bg=button_color, fg=text_color, font=("Arial", 12))
remove_button.pack(pady=5)

# Export metadata button
export_frame = ttk.Frame(root)
export_frame.pack(pady=5)
export_format_var = StringVar(value="CSV")
export_format_menu = OptionMenu(export_frame, export_format_var, "CSV", "TXT")
export_format_menu.config(bg=button_color, fg=text_color, font=("Arial", 10))
export_format_menu.pack(side="left", padx=5)
export_button = Button(export_frame, text="Export Metadata", command=export_metadata, bg=button_color, fg=text_color, font=("Arial", 12))
export_button.pack(side="left")

# Result display text box
result_text = Text(root, wrap="none", width=80, height=15, bg=text_box_bg, fg=text_box_fg, font=("Arial", 10))
scrollbar = Scrollbar(root, command=result_text.yview)
result_text.configure(yscrollcommand=scrollbar.set)
result_text.pack(pady=10)
scrollbar.pack(side="right", fill="y")

# Run the application
root.mainloop()