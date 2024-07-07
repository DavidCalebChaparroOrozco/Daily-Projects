# Importing necessary libraries
import tkinter as tk
from tkinter import messagebox, PhotoImage
import speedtest

def test_speed():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    results = st.results.dict()

    download_speed = results['download'] / 1_000_000  # Convert to Mbps
    upload_speed = results['upload'] / 1_000_000      # Convert to Mbps
    ping = results['ping']

    result_text.set(f"Download: {download_speed:.2f} Mbps\nUpload: {upload_speed:.2f} Mbps\nPing: {ping:.2f} ms")

def show_info():
    messagebox.showinfo("Information", "This application measures your Internet connection's download and upload speed.")

# Configuration of the main root
root = tk.Tk()
root.title("Internet Speed Test by David Caleb")
root.geometry("400x300+300+110")
root.resizable(0,0)
root.tk.call("wm", "iconphoto", root._w, PhotoImage(file="internet.png"))

# Set the background color to a dark theme
root.configure(bg='#333333')

# Create and position widgets
tk.Label(root, text="Internet Speed Test", font=("Helvetica", 16), fg='white', bg='#333333').pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 14), fg='white', bg='#333333')
result_label.pack(pady=10)

start_button = tk.Button(root, text="Start Test", command=test_speed, font=("Helvetica", 12), bg='#4CAF50', fg='white', activebackground='#3E8E41')
start_button.pack(pady=10)

info_button = tk.Button(root, text="Info", command=show_info, font=("Helvetica", 12), bg='#2196F3', fg='white', activebackground='#0B7DDA')
info_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 12), bg='#F44336', fg='white', activebackground='#D32F2F')
exit_button.pack(pady=10)

# Run the main Tkinter loop
root.mainloop()