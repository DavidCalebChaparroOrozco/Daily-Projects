import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
from tkinter import messagebox, PhotoImage, filedialog
import urllib3
from io import BytesIO
import random
import csv

# List to store favorite Pokemon names
favorite_pokemon = []

# List to store search history
search_history = []

# Index to keep track of current search history position
current_index = -1

# Function to toggle the theme of the application
def toggle_theme():
    global dark_theme
    dark_theme = not dark_theme
    if dark_theme:
        window.config(bg="#121212")
        title_label.config(bg="#121212", fg="white")
        pokemon_frame.config(bg="#121212")
        label_id_name.config(bg="#121212", fg="white")
        text_id_name.config(bg="#121212", fg="white")
        info_frame.config(bg="#121212")
        btn_frame.config(bg="#121212")
    else:
        window.config(bg="#FFFFFF")
        title_label.config(bg="#FFFFFF", fg="black")
        label_id_name.config(bg="#FFFFFF", fg="black")
        text_id_name.config(bg="#FFFFFF", fg="black")
        pokemon_frame.config(bg="#FFFFFF")
        info_frame.config(bg="#FFFFFF")
        btn_frame.config(bg="#FFFFFF")

# Function to load Pokemon details
def load_pokemon_details(pokemon):
    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))
    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    info_text = f"{pokemon.dex} - {pokemon.name.title()}\n"
    info_text += f"Height: {pokemon.height}\n"
    info_text += f"Weight: {pokemon.weight}\n"
    pokemon_information.config(text=info_text.title())

    pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())

# Function to load the next Pokemon in the search history list
def next_pokemon():
    global current_index
    if current_index < len(search_history) - 1:
        current_index += 1
        text_id_name.delete(1.0, "end")
        text_id_name.insert("end", search_history[current_index])
        load_pokemon()

# Function to load the previous Pokemon in the search history list
def previous_pokemon():
    global current_index
    if current_index > 0:
        current_index -= 1
        text_id_name.delete(1.0, "end")
        text_id_name.insert("end", search_history[current_index])
        load_pokemon()

# Function to save a Pokemon as favorite
def save_favorite():
    pokemon_name = text_id_name.get(1.0, "end-1c").strip()
    if pokemon_name:
        pokemon_name = pokemon_name.title()
        if pokemon_name not in favorite_pokemon:
            favorite_pokemon.append(pokemon_name)
            messagebox.showinfo("Success", f"Pokemon '{pokemon_name}' added to favorites!")
        else:
            messagebox.showwarning("Warning", f"Pokemon '{pokemon_name}' is already in favorites!")
    else:
        messagebox.showwarning("Warning", "Please enter a Pokemon name to add to favorites!")

# Function to save favorites to a CSV file
def save_favorites_to_file():
    if favorite_pokemon:
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for pokemon in favorite_pokemon:
                    writer.writerow([pokemon])
            messagebox.showinfo("Success", "Favorites saved to file successfully!")
    else:
        messagebox.showwarning("Warning", "No favorite Pokemon to save!")

# Function to load favorites from a CSV file
def load_favorites_from_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            with open(file_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    favorite_pokemon.append(row[0])
            messagebox.showinfo("Success", "Favorites loaded from file successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error loading favorites from file: {str(e)}")

# Function to load a Pokemon from the API
def load_pokemon(event=None):
    pokemon_name = text_id_name.get(1.0, "end-1c").strip()
    try:
        pokemon = pypokedex.get(name=pokemon_name)
    except Exception as e:
        pokemon_image.config(image=None)
        pokemon_information.config(text="")
        pokemon_types.config(text="")
        tk.messagebox.showerror("Error", f"Pokemon '{pokemon_name}' not found!")
        return

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.other_sprites['official-artwork'].front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    info_text = f"{pokemon.dex} - {pokemon.name.title()}\n"
    info_text += f"Height: {pokemon.height}\n"
    info_text += f"Weight: {pokemon.weight}\n"
    pokemon_information.config(text=info_text.title())

    pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())

    if pokemon_name.title() not in search_history:
        search_history.append(pokemon_name.title())
        print("Search history:", search_history)

# Function to load a random Pokemon
def load_random_pokemon():
    try:
        random_pokemon = pypokedex.get(dex=random.randint(1, 898))
        text_id_name.delete(1.0, "end")
        text_id_name.insert("end", random_pokemon.name.title())
        load_pokemon()
    except Exception as e:
        tk.messagebox.showerror("Error", "Error loading a random Pokemon. Please try again.")

# Function to load the next Pokemon in the search history list
def load_next_history_pokemon():
    global current_index
    if current_index < len(search_history) - 1:
        current_index += 1
        pokemon_name = search_history[current_index]
        try:
            pokemon = pypokedex.get(name=pokemon_name)
            load_pokemon_details(pokemon)
            text_id_name.delete(1.0, "end")
            text_id_name.insert("end", pokemon_name)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading next Pokemon: {str(e)}")
    else:
        messagebox.showinfo("Info", "This is the last Pokemon in the Pokedex!")

# Function to load the next Pokemon in the search history list
def load_next_history_pokemon():
    pokemon_name = text_id_name.get(1.0, "end-1c").strip().title()
    if pokemon_name in search_history:
        current_index = search_history.index(pokemon_name)
        if current_index < len(search_history) - 1:
            next_pokemon_name = search_history[current_index + 1]
            text_id_name.delete(1.0, "end")
            text_id_name.insert("end", next_pokemon_name)
            load_pokemon()

# Function to load the previous Pokemon in the search history list
def load_previous_pokemon():
    global current_index
    if current_index > 0:
        current_index -= 1
        pokemon_name = search_history[current_index]
        try:
            pokemon = pypokedex.get(name=pokemon_name)
            load_pokemon_details(pokemon)
            text_id_name.delete(1.0, "end")
            text_id_name.insert("end", pokemon_name)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading previous Pokemon: {str(e)}")
    else:
        messagebox.showinfo("Info", "This is the first Pokemon in the Pokedex!")

# Function to load the previous Pokemon in the search history list
def load_previous_history_pokemon():
    pokemon_name = text_id_name.get(1.0, "end-1c").strip().title()
    if pokemon_name in search_history:
        current_index = search_history.index(pokemon_name)
        if current_index > 0:
            previous_pokemon_name = search_history[current_index - 1]
            text_id_name.delete(1.0, "end")
            text_id_name.insert("end", previous_pokemon_name)
            load_pokemon()

# Function to show favorite Pokemon
def show_favorites():
    if not favorite_pokemon:
        messagebox.showinfo("Favorites", "No favorite Pokemon saved yet!")
    else:
        favorites = "\n".join(favorite_pokemon)
        messagebox.showinfo("Favorites", f"Favorite Pokemon:\n{favorites}")

# Function to show search history
def show_search_history():
    if not search_history:
        messagebox.showinfo("Search History", "No recent search history available!")
    else:
        history = "\n".join(search_history)
        messagebox.showinfo("Search History", f"Recent search history:\n{history}")

# Main window configuration
window = tk.Tk()
window.geometry("900x900")
window.title("Pokedex")
window.config(bg="#FFFFFF")
window.tk.call("wm", "iconphoto", window._w, PhotoImage(file="pokedex.png"))

dark_theme = False

window.config(padx=10, pady=10)

# Frame for Pokemon image and information
pokemon_frame = tk.Frame(window, bg="#FFFFFF")
pokemon_frame.pack(side="left", padx=10, pady=10, fill="both")

# Button to toggle theme
toggle_btn = tk.Button(pokemon_frame, text="Toggle Theme", command=toggle_theme, bg="#FFFFFF")
toggle_btn.config(font=("Arial", 8), width=12)
toggle_btn.pack(side="top")

title_label = tk.Label(pokemon_frame, text="Pokedex by David Caleb", bg="#FFFFFF")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(pokemon_frame, bg="#FFFFFF")
pokemon_image.pack(fill='both')

info_frame = tk.Frame(pokemon_frame, bg="#FFFFFF")
info_frame.pack(padx=5, pady=5, fill='both')

pokemon_information = tk.Label(info_frame, bg="#FFFFFF")
pokemon_information.config(font=("Arial",20))
pokemon_information.pack(padx=5, pady=5, fill='both')

pokemon_types = tk.Label(info_frame, bg="#FFFFFF")
pokemon_types.config(font=("Arial",20))
pokemon_types.pack(padx=5, pady=5, fill='both')

# Frame for buttons
btn_frame = tk.Frame(window, bg="#FFFFFF")
btn_frame.pack(side="right", padx=10, pady=10, fill="both")

label_id_name = tk.Label(btn_frame, text="Search Pokemon by ID or name: ", bg="#FFFFFF")
label_id_name.config(font=("Arial", 8))
label_id_name.pack(padx=5, pady=5, fill='both')

text_id_name = tk.Text(btn_frame, height=1, bg="#FFFFFF")
text_id_name.config(font=("Arial", 8))
text_id_name.pack(padx=5, pady=5,  fill='both')
text_id_name.bind('<Return>', load_pokemon)

# Button to load Pokemon
btn_load = tk.Button(btn_frame, text="Load Pokemon", command=load_pokemon, bg="#FFFFFF")
btn_load.config(font=("Arial", 8), width=12)
btn_load.pack(side= "top",padx=5, pady=5,  fill='both')

# Button to load a random Pokemon
btn_random = tk.Button(btn_frame, text="Random Pokemon", command=load_random_pokemon, bg="#FFFFFF")
btn_random.config(font=("Arial", 8), width=12)
btn_random.pack(padx=5, pady=5, fill='both')

## Favorites

# Button to save Pokemon as favorite
btn_favorite = tk.Button(btn_frame, text="Add to Favorites", command=save_favorite, bg="#FFFFFF")
btn_favorite.config(font=("Arial", 8), width=12)
btn_favorite.pack(side="bottom",padx=5, pady=5, fill='both')

# Button to save favorites to a CSV file
btn_save_favorites = tk.Button(btn_frame, text="Save Favorites", command=save_favorites_to_file, bg="#FFFFFF")
btn_save_favorites.config(font=("Arial", 8), width=12)
btn_save_favorites.pack(side="bottom",padx=5, pady=5, fill='both')

# Button to load favorites from a CSV file
btn_load_favorites = tk.Button(btn_frame, text="Load Favorites", command=load_favorites_from_file, bg="#FFFFFF")
btn_load_favorites.config(font=("Arial", 8), width=12)
btn_load_favorites.pack(side="bottom", padx=5, pady=5, fill='both')

# Button to show favorite Pokemon
btn_show_favorites = tk.Button(btn_frame, text="Show Favorites", command=show_favorites, bg="#FFFFFF")
btn_show_favorites.config(font=("Arial", 8), width=12)
btn_show_favorites.pack(side="bottom", padx=5, pady=5, fill='both')

# Button to load the previous Pokemon in the search history list
btn_previous = tk.Button(btn_frame, text="Previous History", command=load_previous_history_pokemon, bg="#FFFFFF")
btn_previous.config(font=("Arial", 8), width=14)
btn_previous.pack(side="top", padx=4, pady=4, fill='x')

# Button to load the next Pokemon in the search history list
btn_next = tk.Button(btn_frame, text="Next History", command=load_next_history_pokemon, bg="#FFFFFF")
btn_next.config(font=("Arial", 8), width=14)
btn_next.pack(side="top", padx=4, pady=4, fill='x')

# Button to show search history
btn_show_search_history = tk.Button(btn_frame, text="Show Search History", command=show_search_history, bg="#FFFFFF")
btn_show_search_history.config(font=("Arial", 8), width=12)
btn_show_search_history.pack(padx=5, pady=5, fill='both')

label_favorites = tk.Label(btn_frame, text="Favorites", bg="#FFFFFF")
label_favorites.config(font=("Arial", 8))
label_favorites.pack(side="bottom", padx=5, pady=5, fill='both')

window.mainloop()