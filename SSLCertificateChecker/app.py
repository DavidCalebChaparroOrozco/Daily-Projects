# Importing necessary libraries
import ssl
import socket
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Function to retrieve SSL certificate information for a given hostname and port
def get_ssl_certificate_info(hostname, port=443):
    """
    Args:
        hostname: The domain name to check (e.g., 'example.com').
        port: The port to connect to (default is 443 for HTTPS).
    Returns:
        dict: A dictionary containing the certificate's issuer, subject, and expiration date.
    """
    context = ssl.create_default_context()
    
    try:
        # Create a socket connection to the host
        with socket.create_connection((hostname, port)) as sock:
            # Wrap the socket with SSL
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()
                
                # Extract relevant information from the certificate
                issuer = dict(x[0] for x in cert['issuer'])
                subject = dict(x[0] for x in cert['subject'])
                expiration_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                
                return {
                    'issuer': issuer,
                    'subject': subject,
                    'expiration_date': expiration_date
                }
    except Exception as e:
        raise Exception(f"Error retrieving SSL certificate for {hostname}: {e}")

# Function to check the validity and expiration of an SSL certificate
def check_ssl_certificate_validity():
    """
    Check the validity and expiration of an SSL certificate for a given hostname.
    """
    hostname = entry_domain.get().strip()
    
    if not hostname:
        messagebox.showerror("Error", "Please enter a valid domain name.")
        return
    
    try:
        cert_info = get_ssl_certificate_info(hostname)
        
        if cert_info:
            # Clear previous results
            result_text.delete(1.0, tk.END)
            
            # Display certificate information
            result_text.insert(tk.END, f"SSL Certificate Information for {hostname}:\n")
            result_text.insert(tk.END, f"Issuer: {cert_info['issuer']}\n")
            result_text.insert(tk.END, f"Subject: {cert_info['subject']}\n")
            result_text.insert(tk.END, f"Expiration Date: {cert_info['expiration_date']}\n")
            
            # Check if the certificate is still valid
            current_time = datetime.now()
            if current_time < cert_info['expiration_date']:
                days_remaining = (cert_info['expiration_date'] - current_time).days
                result_text.insert(tk.END, f"The SSL certificate is valid. Expires in {days_remaining} days.\n")
            else:
                result_text.insert(tk.END, "The SSL certificate has expired.\n")
        else:
            messagebox.showerror("Error", f"No SSL certificate information found for {hostname}.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
app = tk.Tk()
app.title("SSL Certificate Checker by David Caleb ")
app.geometry("500x400")
app.configure(bg="#2E3440")

# Set a modern dark theme
app.tk_setPalette(background="#2E3440", foreground="#D8DEE9", activeBackground="#4C566A", activeForeground="#ECEFF4")

# Create and place widgets
label_title = tk.Label(app, text="SSL Certificate Checker", font=("Arial", 16, "bold"), bg="#2E3440", fg="#88C0D0")
label_title.pack(pady=10)

label_domain = tk.Label(app, text="Enter Domain:", bg="#2E3440", fg="#D8DEE9")
label_domain.pack()

entry_domain = tk.Entry(app, width=40, bg="#4C566A", fg="#D8DEE9", insertbackground="#D8DEE9")
entry_domain.pack(pady=10)

button_check = tk.Button(app, text="Check SSL Certificate", command=check_ssl_certificate_validity, bg="#5E81AC", fg="#ECEFF4", activebackground="#81A1C1", activeforeground="#ECEFF4")
button_check.pack(pady=10)

result_text = tk.Text(app, height=10, width=60, bg="#3B4252", fg="#D8DEE9", wrap=tk.WORD)
result_text.pack(pady=10)

# Run the application
app.mainloop()