# Handles user interface presentation
class CatView:  
    @staticmethod
    def display_menu():
        print("\n🐾 Cat Management System by David Caleb🐾")
        print("1. View all cats")
        print("2. Add new cat")
        print("3. Remove cat")
        print("4. Search by breed")
        print("5. Update cat age")
        print("6. Show statistics")
        print("7. Save data")
        print("8. Load data")
        print("9. Visualize Data")
        print("10. Exit")
    
    @staticmethod
    def display_message(message):
        print(f"\n{message}")
    
    # Displays list of cats in formatted table
    @staticmethod
    def display_cats(cats):
        if not cats:
            print("\nNo cats found")
            return
            
        print("\n{:<15} {:<20} {:<10}".format('NAME', 'BREED', 'AGE'))
        print("=".center(50,"="))
        for name, breed, age in cats:
            print("{:<15} {:<20} {:<10}".format(name, breed, age))

    # Displays system statistics
    @staticmethod
    def display_statistics(stats):
        print("\n📊 System Statistics 📊")
        print(f"Total Cats: {stats['total_cats']}")
        print(f"Average Age: {stats['average_age']:.1f} years")
        print(f"Most Common Breed: {stats['most_common_breed']}")
    
    # Gets validated user input
    @staticmethod
    def get_input(prompt, validation_func=None):
        while True:
            value = input(prompt).strip()
            if validation_func is None or validation_func(value):
                return value
            print("Invalid input, please try again")
