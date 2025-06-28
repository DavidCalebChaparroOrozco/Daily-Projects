# Import necessary libraries
import random
import pandas as pd
from typing import List, Dict, Optional

# A class to generate balanced BBQ menus with random combinations or dietary preferences.
# Generates shopping lists and calculates quantities based on number of guests.
class BBQMenuGenerator:    
    def __init__(self):
        # Initialize menu options in a structured format
        self.menu_data = {
            'meats': {
                'regular': ['Beef ribs', 'Pork sausage', 'Chicken thighs', 'Pork chops', 'Steak'],
                'gluten_free': ['Beef ribs', 'Grilled chicken', 'Lamb chops', 'Salmon fillet'],
                'vegetarian': ['Portobello mushrooms', 'Tofu steaks', 'Veggie burgers', 'Halloumi']
            },
            'sides': {
                'regular': ['Potato salad', 'Grilled corn', 'Garlic bread', 'Coleslaw'],
                'gluten_free': ['Quinoa salad', 'Roasted vegetables', 'Grilled pineapple', 'Sweet potato mash'],
                'vegetarian': ['Caprese salad', 'Grilled zucchini', 'Bruschetta', 'Stuffed bell peppers']
            },
            'salads': {
                'regular': ['Caesar salad', 'Greek salad', 'Waldorf salad'],
                'gluten_free': ['Arugula salad', 'Tomato cucumber salad', 'Kale salad'],
                'vegetarian': ['Spinach salad', 'Beetroot salad', 'Avocado salad']
            },
            'drinks': {
                'regular': ['Beer', 'Soda', 'Lemonade', 'Iced tea'],
                'gluten_free': ['Cider', 'Wine', 'Sparkling water', 'Fruit juice'],
                'vegetarian': ['Same as gluten-free']  # Vegetarian drinks same as gluten-free
            }
        }
        
        # Shopping list multipliers per person
        self.quantity_guide = {
            # kg per person
            'meats': 0.3,  
            # kg per person
            'sides': 0.2,   
            # kg per person
            'salads': 0.15, 
            # drinks per person
            'drinks': 1.5    
        }
    
    # Generate a random BBQ menu based on number of guests and dietary preference.
    def generate_menu(self, guests: int = 4, preference: Optional[str] = None) -> Dict:
        """    
        Args:
            guests: Number of people to serve (default 4)
            preference: Dietary preference ('gluten_free', 'vegetarian', or None)
            
        Returns:
            Dictionary containing the menu and shopping list
        """
        if preference not in [None, 'gluten_free', 'vegetarian']:
            raise ValueError("Invalid preference. Choose 'gluten_free', 'vegetarian', or None.")
        
        menu = {
            'meat': self._select_random_item('meats', preference),
            'side': self._select_random_item('sides', preference),
            'salad': self._select_random_item('salads', preference),
            'drink': self._select_random_item('drinks', preference),
            'guests': guests
        }
        
        menu['shopping_list'] = self._generate_shopping_list(menu, guests)
        
        return menu
    
    # Helper function to select a random item from a category based on preference.
    def _select_random_item(self, category: str, preference: Optional[str]) -> str:
        """
        Args:
            category: Menu category ('meats', 'sides', etc.)
            preference: Dietary preference
            
        Returns:
            Randomly selected menu item
        """
        # If no preference or preference not specified for category, use regular
        key = preference if preference in self.menu_data[category] else 'regular'
        return random.choice(self.menu_data[category][key])
    
    # Create a shopping list with calculated quantities based on number of guests.
    def _generate_shopping_list(self, menu: Dict, guests: int) -> pd.DataFrame:
        """        
        Args:
            menu: Generated menu dictionary
            guests: Number of people to serve
            
        Returns:
            Pandas DataFrame with shopping items and quantities
        """
        items = []
        
        # Add main items with quantities
        items.append({
            'Item': menu['meat'],
            'Quantity': f"{self.quantity_guide['meats'] * guests:.1f} kg",
            'Category': 'Meat'
        })
        
        items.append({
            'Item': menu['side'],
            'Quantity': f"{self.quantity_guide['sides'] * guests:.1f} kg",
            'Category': 'Side'
        })
        
        items.append({
            'Item': menu['salad'],
            'Quantity': f"{self.quantity_guide['salads'] * guests:.1f} kg",
            'Category': 'Salad'
        })
        
        items.append({
            'Item': menu['drink'],
            'Quantity': f"{self.quantity_guide['drinks'] * guests:.0f} bottles/cans",
            'Category': 'Drink'
        })
        
        # Add common BBQ necessities
        common_items = [
            ('Charcoal', f"{0.5 * guests:.1f} kg"),
            ('BBQ Sauce', '1 bottle'),
            ('Salt & Pepper', 'To taste'),
            ('Olive Oil', '1 bottle'),
            ('Plates & Utensils', f"{guests} sets"),
            ('Napkins', f"{guests * 5} pieces")
        ]
        
        for item, quantity in common_items:
            items.append({
                'Item': item,
                'Quantity': quantity,
                'Category': 'Essentials'
            })
        
        return pd.DataFrame(items)
    
    def display_menu(self, menu: Dict) -> None:
        print("\n🔥 BBQ Menu Generator 🔥")
        print(f"\nFor {menu['guests']} guests:")
        print("=".center(50, "="))
        print(f"🍖 Main: {menu['meat']}")
        print(f"🥗 Side: {menu['side']}")
        print(f"🥙 Salad: {menu['salad']}")
        print(f"🍹 Drink: {menu['drink']}")
        print("\n🛒 Shopping List:")
        print(menu['shopping_list'].to_string(index=False))
        print("\nEnjoy your BBQ! 🍍")


# Example usage
if __name__ == "__main__":
    generator = BBQMenuGenerator()
    
    print("Welcome to the BBQ Menu Generator!")
    print("Let's create a perfect BBQ menu for your gathering.\n")
    
    try:
        guests = int(input("Enter number of guests: "))
        preference = input("Any dietary preferences? (gluten_free/vegetarian/none): ").lower() or None
        
        if preference == 'none':
            preference = None
            
        menu = generator.generate_menu(guests, preference)
        generator.display_menu(menu)
        
    except ValueError as e:
        print(f"\nError: {e}. Please enter valid inputs.")