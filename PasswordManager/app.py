# Import necessary libraries
import tkinter as tk
from tkinter import messagebox, simpledialog
from cryptography.fernet import Fernet
import random
import string

# Generate a key for encryption and decryption
def generate_key():
    return Fernet.generate_key()

# Encrypt the data
def encrypt_data(data, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Decrypt the data
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

# Generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Save the password entry
def save_entry():
    site = site_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    
    if not (site and user and password):
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return
    
    # Encrypt the password before saving
    encrypted_password = encrypt_data(password, key)
    
    # Save to file (you can change this to a database or other storage)
    with open("passwords.txt", "a") as file:
        file.write(f"{site},{user},{encrypted_password.decode()}\n")
    
    messagebox.showinfo("Success", "Password entry saved successfully!")
    
    # Clear the input fields
    site_entry.delete(0, tk.END)
    user_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# View saved passwords
def view_passwords():
    try:
        with open("passwords.txt", "r") as file:
            entries = file.readlines()
        
        if not entries:
            messagebox.showinfo("No Entries", "No passwords saved yet.")
            return
        
        # Prepare a message to show saved passwords
        message = ""
        for entry in entries:
            site, user, encrypted_password = entry.strip().split(',')
            decrypted_password = decrypt_data(encrypted_password.encode(), key)
            message += f"Site: {site}, User: {user}, Password: {decrypted_password}\n"
        
        # Show saved passwords in a message box
        messagebox.showinfo("Saved Passwords", message.strip())
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while reading passwords: {str(e)}")

# Create main application window
root = tk.Tk()
root.title("Password Manager by David Caleb")
root.geometry("400x350")
root.configure(bg='black')

# Generate a key for encryption (store this securely!)
key = generate_key()

# Create input fields and labels
tk.Label(root, text="Site:", bg='black', fg='white').pack(pady=5)
site_entry = tk.Entry(root, width=40)
site_entry.pack(pady=5)

tk.Label(root, text="Username:", bg='black', fg='white').pack(pady=5)
user_entry = tk.Entry(root, width=40)
user_entry.pack(pady=5)

tk.Label(root, text="Password:", bg='black', fg='white').pack(pady=5)
password_entry = tk.Entry(root, width=40)
password_entry.pack(pady=5)

# Create buttons for saving and generating passwords
save_button = tk.Button(root, text="Save Password", command=save_entry, bg='gray', fg='white')
save_button.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=lambda: clear_and_generate_password(), bg='gray', fg='white')
generate_button.pack(pady=10)

view_button = tk.Button(root, text="View Saved Passwords", command=view_passwords, bg='gray', fg='white')
view_button.pack(pady=10)

# Function to clear the password entry and generate a new password
def clear_and_generate_password():
    new_password = generate_password()
    # Clear the field before inserting new password
    password_entry.delete(0, tk.END)  
    # Insert the newly generated password
    password_entry.insert(0, new_password)  

# Start the Tkinter event loop
root.mainloop()