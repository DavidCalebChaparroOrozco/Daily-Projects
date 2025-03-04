# Importing necessary libraries
import whois
import requests
import tkinter as tk
from tkinter import messagebox, filedialog
import re

# Retrieve WHOIS information for a given domain.
def get_whois_info(domain):
    """    
    Args:
        domain: The domain name to look up (e.g., 'example.com').
    Returns:
        dict: A dictionary containing WHOIS information.
    """
    try:
        # Perform WHOIS lookup
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        return {"error": f"Failed to retrieve WHOIS information: {e}"}

# Check if a website is live and accessible.
def check_website_legitimacy(url):
    """    
    Args:
        url: The URL of the website to check.
    Returns:
        bool: True if the website is live, False otherwise.
    """
    try:
        # Send a GET request to the website
        response = requests.get(url, timeout=10)
        # Check if the response status code is 200 (OK)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Validate the domain format using a regular expression.
def validate_domain(domain):
    """
    Args:
        domain: The domain name to validate.
    Returns:
        bool: True if the domain is valid, False otherwise.
    """
    domain_regex = re.compile(
        r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    )
    return bool(domain_regex.match(domain))

# Display WHOIS information in a readable format.
def display_whois_info(domain_info, text_widget):
    """    
    Args:
        domain_info: The WHOIS information to display.
        text_widget: The text widget to display the information.
    """
    text_widget.delete(1.0, tk.END)  # Clear previous content
    text_widget.insert(tk.END, "\nWHOIS Information:\n")
    text_widget.insert(tk.END, "=".center(50, "=") + "\n")
    for key, value in domain_info.items():
        text_widget.insert(tk.END, f"{key}: {value}\n")
    text_widget.insert(tk.END, "=".center(50, "=") + "\n")

# Export WHOIS information to a text file
def export_to_file(domain_info):
    """    
    Args:
        domain_info: The WHOIS information to export.
    """
    try:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write("WHOIS Information:\n")
                file.write("=".center(50, "=") + "\n")
                for key, value in domain_info.items():
                    file.write(f"{key}: {value}\n")
                file.write("=".center(50, "=") + "\n")
            messagebox.showinfo("Export Successful", f"Data exported to {file_path}")
    except Exception as e:
        messagebox.showerror("Export Failed", f"Failed to export data: {e}")

# Main application class
class WHOISLookupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WHOIS Lookup Tool")
        self.root.geometry("600x400")
        self.root.configure(bg="#2E3440")  # Dark background

        # Custom font
        self.custom_font = ("Arial", 12)

        # Title Label
        self.title_label = tk.Label(
            root,
            text="WHOIS Lookup Tool",
            font=("Arial", 18, "bold"),
            fg="#ECEFF4",  # Light text color
            bg="#2E3440"  # Dark background
        )
        self.title_label.pack(pady=10)

        # Domain Entry
        self.domain_label = tk.Label(
            root,
            text="Enter Domain Name:",
            font=self.custom_font,
            fg="#ECEFF4",
            bg="#2E3440"
        )
        self.domain_label.pack()

        self.domain_entry = tk.Entry(
            root,
            font=self.custom_font,
            width=40,
            bg="#3B4252",  # Darker background for entry
            fg="#ECEFF4"  # Light text color
        )
        self.domain_entry.pack(pady=10)

        # Buttons
        self.lookup_button = tk.Button(
            root,
            text="Lookup WHOIS",
            font=self.custom_font,
            bg="#81A1C1",  # Blue button
            fg="#2E3440",
            command=self.perform_lookup
        )
        self.lookup_button.pack(pady=5)

        self.export_button = tk.Button(
            root,
            text="Export Results",
            font=self.custom_font,
            bg="#A3BE8C",  # Green button
            fg="#2E3440",
            command=self.export_results
        )
        self.export_button.pack(pady=5)

        # Result Text Widget
        self.result_text = tk.Text(
            root,
            font=self.custom_font,
            bg="#3B4252",  # Darker background
            fg="#ECEFF4",  # Light text color
            wrap=tk.WORD,
            height=10
        )
        self.result_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Perform WHOIS lookup
    def perform_lookup(self):
        domain = self.domain_entry.get().strip()
        if not domain:
            messagebox.showwarning("Input Error", "Please enter a domain name.")
            return

        if not validate_domain(domain):
            messagebox.showwarning("Input Error", "Invalid domain format.")
            return

        domain_info = get_whois_info(domain)
        if "error" in domain_info:
            messagebox.showerror("Error", domain_info["error"])
        else:
            display_whois_info(domain_info, self.result_text)
            website_url = f"http://{domain}" if not domain.startswith(("http://", "https://")) else domain
            is_legitimate = check_website_legitimacy(website_url)
            if is_legitimate:
                self.result_text.insert(tk.END, f"\nThe website '{domain}' is live and accessible.\n")
            else:
                self.result_text.insert(tk.END, f"\nThe website '{domain}' is not accessible or may not be legitimate.\n")

    # Export results to a file
    def export_results(self):
        domain_info = get_whois_info(self.domain_entry.get().strip())
        if "error" in domain_info:
            messagebox.showerror("Error", domain_info["error"])
        else:
            export_to_file(domain_info)

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = WHOISLookupApp(root)
    root.mainloop()