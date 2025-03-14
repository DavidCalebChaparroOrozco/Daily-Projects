# Importing necessary libraries
import tkinter as tk
from tkinter import messagebox, filedialog

# Define font style for the GUI
FONT = ("calibri", 20, "bold")

class CaesarCipherGUI:
    def __init__(self, master):
        # Set the title of the window
        master.title("Caesar Cipher GUI by David Caleb")
        
        # Configure the background color of the master window
        master.configure(bg="#2E3440")
        
        # StringVar to store plaintext and ciphertext, IntVar to store the key
        self.plaintext = tk.StringVar(master, value="")
        self.ciphertext = tk.StringVar(master, value="")
        self.key = tk.IntVar(master)

        # Create the menu bar
        self.create_menu(master)

        # Plaintext controls
        self.plain_label = tk.Label(master, text="Plaintext", fg="#88C0D0", bg="#2E3440", font=FONT)
        self.plain_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.plain_entry = tk.Entry(master, textvariable=self.plaintext, width=50, font=FONT, bg="#4C566A", fg="#ECEFF4")
        self.plain_entry.grid(row=0, column=1, padx=20, pady=10)
        
        self.encrypt_button = tk.Button(master, text="Encrypt", command=lambda: self.encrypt_callback(), font=FONT, bg="#5E81AC", fg="#ECEFF4")
        self.encrypt_button.grid(row=0, column=2, padx=10, pady=10)
        
        self.plain_clear = tk.Button(master, text="Clear", command=lambda: self.clear('plain'), font=FONT, bg="#BF616A", fg="#ECEFF4")
        self.plain_clear.grid(row=0, column=3, padx=10, pady=10)

        # Key controls
        self.key_label = tk.Label(master, text="Key", font=FONT, bg="#2E3440", fg="#88C0D0")
        self.key_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.key_entry = tk.Entry(master, textvariable=self.key, width=10, font=FONT, bg="#4C566A", fg="#ECEFF4")
        self.key_entry.grid(row=1, column=1, sticky=tk.W, padx=20, pady=10)

        # Ciphertext controls
        self.cipher_label = tk.Label(master, text="Ciphertext", fg="#88C0D0", bg="#2E3440", font=FONT)
        self.cipher_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.cipher_entry = tk.Entry(master, textvariable=self.ciphertext, width=50, font=FONT, bg="#4C566A", fg="#ECEFF4")
        self.cipher_entry.grid(row=2, column=1, padx=20, pady=10)
        
        self.decrypt_button = tk.Button(master, text="Decrypt", command=lambda: self.decrypt_callback(), font=FONT, bg="#5E81AC", fg="#ECEFF4")
        self.decrypt_button.grid(row=2, column=2, padx=10, pady=10)
        
        self.cipher_clear = tk.Button(master, text="Clear", command=lambda: self.clear('cipher'), font=FONT, bg="#BF616A", fg="#ECEFF4")
        self.cipher_clear.grid(row=2, column=3, padx=10, pady=10)

        # Brute Force Button
        self.brute_force_button = tk.Button(master, text="Brute Force", command=lambda: self.brute_force_decrypt(), font=FONT, bg="#D08770", fg="#ECEFF4")
        self.brute_force_button.grid(row=3, column=1, pady=20)

    # Create a menu bar with File and Help options.
    def create_menu(self, master):
        menubar = tk.Menu(master)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open Plaintext", command=lambda: self.open_file('plain'))
        file_menu.add_command(label="Save Plaintext", command=lambda: self.save_file(self.plain_entry.get()))
        file_menu.add_command(label="Open Ciphertext", command=lambda: self.open_file('cipher'))
        file_menu.add_command(label="Save Ciphertext", command=lambda: self.save_file(self.cipher_entry.get()))
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)
        
        master.config(menu=menubar)

    # Display an about dialog.
    def show_about(self):
        messagebox.showinfo("About", "Caesar Cipher GUI\nVersion 1.0\nA simple encryption/decryption tool.")

    # Clear the plaintext or ciphertext entry based on the input.
    def clear(self, str_val):
        if str_val == 'cipher':
            self.cipher_entry.delete(0, 'end')
        elif str_val == 'plain':
            self.plain_entry.delete(0, 'end')

    # Retrieve the key value from the entry field.
    def get_key(self):
        try:
            key_val = self.key.get()
            if not 1 <= key_val <= 25:
                messagebox.showerror("Invalid Key", "Key must be between 1 and 25.")
                return None
            return key_val
        except tk.TclError:
            messagebox.showerror("Invalid Key", "Key must be a valid integer.")
            return None

    # Encrypt the plaintext using the Caesar Cipher algorithm.
    def encrypt_callback(self):
        key = self.get_key()
        if key is None:
            return
        plaintext = self.plain_entry.get()
        if not plaintext:
            messagebox.showerror("Error", "Plaintext field is empty.")
            return
        ciphertext = encrypt(plaintext, key)
        self.cipher_entry.delete(0, tk.END)
        self.cipher_entry.insert(0, ciphertext)

    # Decrypt the ciphertext using the Caesar Cipher algorithm.
    def decrypt_callback(self):
        key = self.get_key()
        if key is None:
            return
        ciphertext = self.cipher_entry.get()
        if not ciphertext:
            messagebox.showerror("Error", "Ciphertext field is empty.")
            return
        plaintext = decrypt(ciphertext, key)
        self.plain_entry.delete(0, tk.END)
        self.plain_entry.insert(0, plaintext)

    # Attempt to decrypt the ciphertext using all possible keys (1–25).
    def brute_force_decrypt(self):
        ciphertext = self.cipher_entry.get()
        if not ciphertext:
            messagebox.showerror("Error", "Ciphertext field is empty.")
            return
        
        results = ""
        for key in range(1, 26):
            decrypted = decrypt(ciphertext, key)
            results += f"Key {key}: {decrypted}\n"
        
        # Display results in a new window
        result_window = tk.Toplevel()
        result_window.title("Brute Force Results")
        result_text = tk.Text(result_window, wrap=tk.WORD, font=FONT, bg="#4C566A", fg="#ECEFF4")
        result_text.insert(tk.END, results)
        result_text.pack(fill=tk.BOTH, expand=True)

    # Open a file and load its content into the plaintext or ciphertext field.
    def open_file(self, target):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                if target == 'plain':
                    self.plain_entry.delete(0, tk.END)
                    self.plain_entry.insert(0, content)
                elif target == 'cipher':
                    self.cipher_entry.delete(0, tk.END)
                    self.cipher_entry.insert(0, content)

    # Save the content to a file.
    def save_file(self, content):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)


# Encrypt the plaintext using the Caesar Cipher algorithm.
def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isupper():
            ciphertext += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            ciphertext += chr((ord(char) + key - 97) % 26 + 97)
        else:
            ciphertext += char
    return ciphertext


# Decrypt the ciphertext using the Caesar Cipher algorithm.
def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isupper():
            plaintext += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            plaintext += chr((ord(char) - key - 97) % 26 + 97)
        else:
            plaintext += char
    return plaintext


if __name__ == "__main__":
    # Create the main window and run the application
    root = tk.Tk()
    caesar = CaesarCipherGUI(root)
    root.mainloop()