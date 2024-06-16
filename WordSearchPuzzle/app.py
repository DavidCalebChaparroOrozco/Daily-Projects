# Importing necessary libraries
import tkinter as tk
from tkinter import messagebox
import random
import string

class WordSearch(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Word Search Puzzle by David Caleb")
        self.words = []
        self.grid = []
        self.selected_cells = []
        self.found_words = set()
        self.timer_running = False
        self.remaining_time = 0
        
        # Input frame for entering words
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Enter words (comma separated):").pack(side=tk.LEFT)
        self.entry = tk.Entry(input_frame, width=50)
        self.entry.pack(side=tk.LEFT)
        
        generate_button = tk.Button(input_frame, text="Generate", command=self.create_word_search)
        generate_button.pack(side=tk.LEFT, padx=10)
        
        # Frame for displaying the word search grid
        self.grid_frame = tk.Frame(self)
        self.grid_frame.pack(pady=10, side=tk.LEFT)
        
        # Frame for displaying the word list
        self.word_list_frame = tk.Frame(self)
        self.word_list_frame.pack(pady=10, side=tk.LEFT)
        
        # Timer frame
        self.timer_frame = tk.Frame(self)
        self.timer_frame.pack(pady=10)
        
        tk.Label(self.timer_frame, text="Select Timer (minutes):").pack(side=tk.LEFT)
        self.timer_var = tk.IntVar(value=5)
        timer_menu = tk.OptionMenu(self.timer_frame, self.timer_var, 5, 6, 7, 8, 9, 10)
        timer_menu.pack(side=tk.LEFT)
        
        # Solve button
        self.solve_button = tk.Button(self, text="Solve", command=self.solve_word_search)
        self.solve_button.pack(pady=10, side=tk.BOTTOM)
        
        self.timer_label = tk.Label(self, text="", font=('Arial', 14))
        self.timer_label.pack(pady=10)

    def generate_grid(self, words):
        size = max(len(max(words, key=len)), len(words)) + 5
        grid = [[' ' for _ in range(size)] for _ in range(size)]
        
        for word in words:
            placed = False
            while not placed:
                direction = random.choice(['horizontal', 'vertical', 'diagonal'])
                if direction == 'horizontal':
                    row = random.randint(0, size - 1)
                    col = random.randint(0, size - len(word))
                    if all(grid[row][col+i] in (' ', letter) for i, letter in enumerate(word)):
                        for i, letter in enumerate(word):
                            grid[row][col+i] = letter
                        placed = True
                elif direction == 'vertical':
                    row = random.randint(0, size - len(word))
                    col = random.randint(0, size - 1)
                    if all(grid[row+i][col] in (' ', letter) for i, letter in enumerate(word)):
                        for i, letter in enumerate(word):
                            grid[row+i][col] = letter
                        placed = True
                elif direction == 'diagonal':
                    row = random.randint(0, size - len(word))
                    col = random.randint(0, size - len(word))
                    if all(grid[row+i][col+i] in (' ', letter) for i, letter in enumerate(word)):
                        for i, letter in enumerate(word):
                            grid[row+i][col+i] = letter
                        placed = True
        
        # Fill the remaining empty spaces with random letters
        for row in range(size):
            for col in range(size):
                if grid[row][col] == ' ':
                    grid[row][col] = random.choice(string.ascii_uppercase)
                    
        return grid

    def display_grid(self, grid):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                label = tk.Label(self.grid_frame, text=grid[row][col], font=('Arial', 14), width=2, height=1, borderwidth=1, relief='solid')
                label.grid(row=row, column=col)
                label.bind("<Button-1>", lambda e, r=row, c=col: self.select_cell(r, c))
                
    def display_word_list(self):
        for widget in self.word_list_frame.winfo_children():
            widget.destroy()
        
        self.word_labels = {}
        for word in self.words:
            label = tk.Label(self.word_list_frame, text=word, font=('Arial', 14))
            label.pack(anchor='w')
            self.word_labels[word] = label

    def select_cell(self, row, col):
        if (row, col) not in self.selected_cells:
            self.selected_cells.append((row, col))
            self.grid_frame.grid_slaves(row=row, column=col)[0].config(bg='yellow')
        
        # Check if the selected cells form any word
        if self.check_word():
            for r, c in self.selected_cells:
                self.grid_frame.grid_slaves(row=r, column=c)[0].config(bg='green')
            self.selected_cells.clear()
            
            if len(self.found_words) == len(self.words):
                messagebox.showinfo("Congratulations!", "You found all the words! You won!")
                if messagebox.askyesno("Play Again?", "Do you want to play again?"):
                    self.reset_game()
        else:
            # Check if the number of selected cells reaches the minimum length of any word
            min_word_length = len(min(self.words, key=len))
            if len(self.selected_cells) >= min_word_length:
                self.after(1500, self.reset_selected_cells)

    def check_word(self):
        word = ''.join(self.grid[r][c] for r, c in self.selected_cells)
        reversed_word = word[::-1]
        if word in self.words or reversed_word in self.words:
            found_word = word if word in self.words else reversed_word
            self.found_words.add(found_word)
            self.word_labels[found_word].config(fg='red', font=('Arial', 14, 'overstrike'))
            return True
        return False

    def reset_selected_cells(self):
        for r, c in self.selected_cells:
            self.grid_frame.grid_slaves(row=r, column=c)[0].config(bg='white')
        self.selected_cells.clear()

    def solve_word_search(self):
        for word in self.words:
            for direction in ['horizontal', 'vertical', 'diagonal']:
                if self.find_and_color_word(word, direction):
                    break
        messagebox.showinfo("Solve", "All words have been highlighted.")

    def find_and_color_word(self, word, direction):
        size = len(self.grid)
        for row in range(size):
            for col in range(size):
                if direction == 'horizontal' and col + len(word) <= size and all(self.grid[row][col + i] == word[i] for i in range(len(word))):
                    for i in range(len(word)):
                        self.grid_frame.grid_slaves(row=row, column=col + i)[0].config(bg='green')
                    return True
                elif direction == 'vertical' and row + len(word) <= size and all(self.grid[row + i][col] == word[i] for i in range(len(word))):
                    for i in range(len(word)):
                        self.grid_frame.grid_slaves(row=row + i, column=col)[0].config(bg='green')
                    return True
                elif direction == 'diagonal' and row + len(word) <= size and col + len(word) <= size and all(self.grid[row + i][col + i] == word[i] for i in range(len(word))):
                    for i in range(len(word)):
                        self.grid_frame.grid_slaves(row=row + i, column=col + i)[0].config(bg='green')
                    return True
        return False

    def create_word_search(self):
        self.words = [word.strip().upper() for word in self.entry.get().split(',')]
        if self.words and any(self.words):
            self.grid = self.generate_grid(self.words)
            self.display_grid(self.grid)
            self.display_word_list()
            self.start_timer()
        else:
            messagebox.showwarning("Input Error", "Please enter at least one word separated by commas.")
    
    def start_timer(self):
        if self.timer_running:
            self.after_cancel(self.timer_id)
        # Convert minutes to seconds
        self.remaining_time = self.timer_var.get() * 60  
        self.timer_running = True
        self.update_timer()
    
    def update_timer(self):
        minutes, seconds = divmod(self.remaining_time, 60)
        self.timer_label.config(text=f"Time remaining: {minutes:02}:{seconds:02}")
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.timer_id = self.after(1000, self.update_timer)
        else:
            self.timer_running = False
            messagebox.showinfo("Time's up!", "Time is up! You did not find all the words. Try again.")
            if messagebox.askyesno("Play Again?", "Do you want to play again?"):
                self.reset_game()
    
    def reset_game(self):
        self.words = []
        self.grid = []
        self.selected_cells = []
        self.found_words.clear()
        self.entry.delete(0, tk.END)
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        for widget in self.word_list_frame.winfo_children():
            widget.destroy()
        self.timer_label.config(text="")
        self.timer_running = False

# Start the main loop
if __name__ == "__main__":
    app = WordSearch()
    app.mainloop()
