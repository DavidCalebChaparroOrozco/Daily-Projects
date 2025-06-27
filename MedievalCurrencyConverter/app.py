# A comprehensive tool for converting between modern and historical/fantasy currency systems

class CurrencyConverter:
    # Supported currency systems with their conversion rates
    CURRENCY_SYSTEMS = {
        "standard_fantasy": {
            "name": "Standard Fantasy",
            "rates": {"gold": 1, "silver": 10, "copper": 100},
            "symbols": {"gold": "gp", "silver": "sp", "copper": "cp"}
        },
        "westeros": {
            "name": "Westeros (Game of Thrones)",
            "rates": {"gold_dragon": 1, "silver_stag": 7, "copper_penny": 210},
            "symbols": {"gold_dragon": "GD", "silver_stag": "SS", "copper_penny": "CP"}
        },
        "historical_england": {
            "name": "Medieval England",
            "rates": {"pound": 1, "shilling": 20, "penny": 240},
            "symbols": {"pound": "£", "shilling": "s", "penny": "d"}
        }
    }

    def __init__(self):
        self.current_system = "standard_fantasy"

    # Convert between currencies in the current system
    def convert(self, amount, from_currency, to_currency):
        system = self.CURRENCY_SYSTEMS[self.current_system]
        
        try:
            # Convert to base currency (gold equivalent) first
            base_value = amount / system["rates"][from_currency]
            # Convert to target currency
            result = base_value * system["rates"][to_currency]
            return round(result, 2)
        except KeyError:
            return None

    # Show conversion of one currency to all others in the system
    def show_full_conversion(self, amount, currency):
        system = self.CURRENCY_SYSTEMS[self.current_system]
        print(f"\nConversion in {system['name']} system:")
        
        for curr, rate in system["rates"].items():
            if curr != currency:
                converted = self.convert(amount, currency, curr)
                symbol = system["symbols"][curr]
                print(f"{amount} {currency} = {converted} {symbol} ({curr.replace('_', ' ')})")

    # Display all available currency systems
    def list_systems(self):
        print("\nAvailable Currency Systems:")
        for i, (key, system) in enumerate(self.CURRENCY_SYSTEMS.items(), 1):
            print(f"{i}. {system['name']}")
        return len(self.CURRENCY_SYSTEMS)

# Display the main menu options
def display_menu():
    print("\n" + "=".center(50, "="))
    print("MEDIEVAL CURRENCY CONVERTER PRO".center(50))
    print("=".center(50, "="))
    print("\nMain Menu:")
    print("1. Convert between currencies")
    print("2. Show full currency breakdown")
    print("3. Change currency system")
    print("4. View current rates")
    print("5. Exit")
    print("=".center(50, "="))

# Helper function to get valid currency input
def get_currency_input(converter, prompt):
    system = converter.CURRENCY_SYSTEMS[converter.current_system]
    while True:
        print(f"\nAvailable currencies: {', '.join(system['rates'].keys())}")
        currency = input(prompt).lower()
        if currency in system["rates"]:
            return currency
        print("Invalid currency. Please try again.")

def main():
    converter = CurrencyConverter()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        # Convert between currencies
        if choice == "1":  
            try:
                amount = float(input("\nEnter amount to convert: "))
                from_curr = get_currency_input(converter, "Convert from: ")
                to_curr = get_currency_input(converter, "Convert to: ")
                
                result = converter.convert(amount, from_curr, to_curr)
                if result is not None:
                    symbols = converter.CURRENCY_SYSTEMS[converter.current_system]["symbols"]
                    print(f"\nResult: {amount} {symbols.get(from_curr, from_curr)} = {result} {symbols.get(to_curr, to_curr)}")
                else:
                    print("Conversion failed. Invalid currencies.")
            except ValueError:
                print("Please enter a valid number.")
                
        # Show full breakdown
        elif choice == "2":  
            try:
                amount = float(input("\nEnter amount to convert: "))
                currency = get_currency_input(converter, "Show conversions for which currency? ")
                converter.show_full_conversion(amount, currency)
            except ValueError:
                print("Please enter a valid number.")
                
        # Change system
        elif choice == "3":  
            num_systems = converter.list_systems()
            try:
                sys_choice = int(input(f"\nSelect system (1-{num_systems}): "))
                if 1 <= sys_choice <= num_systems:
                    converter.current_system = list(converter.CURRENCY_SYSTEMS.keys())[sys_choice-1]
                    print(f"\nChanged to {converter.CURRENCY_SYSTEMS[converter.current_system]['name']} system")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")
                
        # View rates
        elif choice == "4":  
            system = converter.CURRENCY_SYSTEMS[converter.current_system]
            print(f"\nCurrent system: {system['name']}")
            print("Exchange rates:")
            for currency, rate in system["rates"].items():
                symbol = system["symbols"][currency]
                print(f"1 {symbol} ({currency.replace('_', ' ')}) = {rate} base units")
                
        # Exit
        elif choice == "5":  
            print("\nThank you for using Medieval Currency Converter Pro!")
            break
            
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()