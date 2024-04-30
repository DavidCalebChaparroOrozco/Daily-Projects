# Importing necessary libraries
import tkinter as tk
from forex_python.converter import CurrencyRates

# List of common currencies
common_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'COP', 'AUD', 'CHF', 'NZD']

class CurrencyConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Currency Converter by David Caleb")
        self.root.geometry('355x180')

        # Creating dropdown menu for 'from' currency selection
        self.from_var = tk.StringVar(self.root)
        self.from_var.set("USD")
        self.from_menu = tk.OptionMenu(self.root, self.from_var, *common_currencies)
        self.from_menu.pack(pady=1)

        # Creating dropdown menu for 'to' currency selection
        self.to_var = tk.StringVar(self.root)
        self.to_var.set("EUR")
        self.to_menu = tk.OptionMenu(self.root, self.to_var, *common_currencies)
        self.to_menu.pack(pady=1)

        # Creating label and entry for amount input
        self.amount_label = tk.Label(self.root, text="Amount: ")
        self.amount_label.pack(pady=1)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=1)

        # Creating button for conversion
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_currency)
        self.convert_button.pack(pady=1)

        # Creating label for displaying conversion result
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=1)

        self.root.mainloop()

    # Convert currency based on user input and display result.
    def convert_currency(self):
        try:
            # Getting 'from' currency selection
            from_currency = self.from_var.get()
            # Getting 'to' currency selection
            to_currency = self.to_var.get()
            # Getting amount to convert
            amount = float(self.amount_entry.get())

            # Creating instance of CurrencyRates class
            c_rates = CurrencyRates()

            # Getting conversion rate
            rate = c_rates.get_rate(from_currency, to_currency)
            # Calculating converted amount
            converted_amount = amount * rate

            # Updating result label with conversion result
            self.result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            
        except ValueError:
            # Handling invalid input
            self.result_label.config(text="Please enter a valid number!")
        except Exception:
            # Handling other exceptions
            self.result_label.config(text="Error ocurred")


if __name__ == "__main__":
    CurrencyConverter()