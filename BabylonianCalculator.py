# Import necessary libraries
import tkinter as tk
from tkinter import ttk

class BabylonianCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Babylonian Sexagesimal Calculator by David Caleb")
        self.root.geometry("500x500")
        self.root.configure(bg="#2d2d2d")
        
        # Initialize variables
        self.current_input = ""
        self.result = 0
        self.operation = None
        self.is_new_input = True
        
        # Create GUI
        self.create_widgets()
        
    def create_widgets(self):
        # Style configuration
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=10)
        style.configure("TLabel", font=("Arial", 18), background="#2d2d2d", foreground="#ffffff")
        
        # Display for sexagesimal (base 60) numbers
        self.display = ttk.Label(self.root, text="0", anchor="e")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="ew")
        
        # Buttons for digits 0-9 (we'll use 0-9 and then special notation for higher digits)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('←', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('Sex→Dec', 5, 0), ('Dec→Sex', 5, 1), ('=', 5, 2), ('⌫', 5, 3)
        ]
        
        # Create buttons
        for (text, row, col) in buttons:
            button = ttk.Button(self.root, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        
        # Configure grid weights
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, button_text):
        if button_text in "0123456789":
            if self.is_new_input:
                self.current_input = button_text
                self.is_new_input = False
            else:
                self.current_input += button_text
            self.update_display()
        elif button_text in "+-*/":
            self.perform_operation()
            self.operation = button_text
            self.is_new_input = True
        elif button_text == "=":
            self.perform_operation()
            self.operation = None
            self.is_new_input = True
        elif button_text == "C":
            self.current_input = ""
            self.result = 0
            self.operation = None
            self.is_new_input = True
            self.update_display("0")
        elif button_text == "←":
            self.current_input = self.current_input[:-1]
            if not self.current_input:
                self.current_input = "0"
                self.is_new_input = True
            self.update_display()
        elif button_text == "⌫":
            self.current_input = ""
            self.is_new_input = True
            self.update_display("0")
        elif button_text == "Sex→Dec":
            if self.current_input:
                decimal = self.sexagesimal_to_decimal(self.current_input)
                self.update_display(str(decimal))
                self.current_input = str(decimal)
        elif button_text == "Dec→Sex":
            if self.current_input:
                try:
                    decimal = float(self.current_input)
                    sexagesimal = self.decimal_to_sexagesimal(decimal)
                    self.update_display(sexagesimal)
                    self.current_input = sexagesimal
                except ValueError:
                    self.update_display("Error")
    
    def perform_operation(self):
        if not self.current_input:
            return
            
        try:
            current_value = float(self.sexagesimal_to_decimal(self.current_input))
            
            if self.operation == "+":
                self.result += current_value
            elif self.operation == "-":
                self.result -= current_value
            elif self.operation == "*":
                self.result *= current_value
            elif self.operation == "/":
                self.result /= current_value
            else:
                self.result = current_value
                
            self.current_input = self.decimal_to_sexagesimal(self.result)
            self.update_display(self.current_input)
        except (ValueError, ZeroDivisionError):
            self.update_display("Error")
            self.current_input = ""
            self.result = 0
            self.operation = None
            self.is_new_input = True
    
    def update_display(self, text=None):
        if text is None:
            text = self.current_input if self.current_input else "0"
        self.display.config(text=text)
    
    # Convert a decimal number to sexagesimal (base 60) notation
    @staticmethod
    def decimal_to_sexagesimal(decimal_num):
        decimal_num = float(decimal_num)
        integer_part = int(decimal_num)
        fractional_part = decimal_num - integer_part
        
        # Convert integer part
        sexagesimal_parts = []
        num = integer_part
        while num > 0:
            num, remainder = divmod(num, 60)
            sexagesimal_parts.append(str(remainder))
        
        if not sexagesimal_parts:
            sexagesimal_parts = ["0"]
        
        sexagesimal_str = ",".join(reversed(sexagesimal_parts))
        
        # Convert fractional part if exists
        if fractional_part > 0:
            sexagesimal_str += ";"
            frac = fractional_part
            precision = 5  # Limit precision to avoid infinite loops
            while frac > 0 and precision > 0:
                frac *= 60
                digit = int(frac)
                sexagesimal_str += str(digit)
                frac -= digit
                precision -= 1
        
        return sexagesimal_str
    
    # Convert a sexagesimal (base 60) number to decimal
    @staticmethod
    def sexagesimal_to_decimal(sexagesimal_str):
        if ";" in sexagesimal_str:
            integer_part, fractional_part = sexagesimal_str.split(";")
        else:
            integer_part = sexagesimal_str
            fractional_part = ""
        
        # Process integer part
        integer_digits = [int(d) for d in integer_part.split(",") if d]
        decimal_value = 0
        for i, digit in enumerate(reversed(integer_digits)):
            decimal_value += digit * (60 ** i)
        
        # Process fractional part
        for i, digit in enumerate(fractional_part, start=1):
            decimal_value += int(digit) / (60 ** i)
        
        return decimal_value

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = BabylonianCalculator(root)
    root.mainloop()