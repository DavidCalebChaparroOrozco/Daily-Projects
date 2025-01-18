# Recursively generates all possible ice cream combinations.
def generate_combinations(flavors, toppings, current_combination=None, index=0):
    """
    Args:
        flavors: A list of ice cream flavors.
        toppings: A list of toppings.
        current_combination: Tracks the current combination being generated.
        index: The current index in the topping list to add to combinations.
    Returns:
        list: A list of all possible ice cream combinations.
    """
    # Initialize the list for storing combinations
    if current_combination is None:
        current_combination = []
    
    # Base case: if we've exhausted the toppings list, return the combination
    if index == len(toppings):
        return [current_combination[:]]

    # Recursive case:
    # 1. Include the topping at the current index
    with_topping = generate_combinations(flavors, toppings, current_combination + [toppings[index]], index + 1)
    # 2. Exclude the topping at the current index
    without_topping = generate_combinations(flavors, toppings, current_combination, index + 1)

    # Combine both possibilities
    return with_topping + without_topping


# Main function to showcase the ice cream combination generator.
def main():
    # Define a list of ice cream flavors
    flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint"]
    # Define a list of toppings
    toppings = ["Sprinkles", "Cherries", "Chocolate Syrup", "Nuts"]

    print("Welcome to the Ice Cream Combination Generator by David Caleb!")
    print(f"We have the following flavors: {', '.join(flavors)}")
    print(f"We have the following toppings: {', '.join(toppings)}\n")

    print("Generating all possible combinations...\n")

    # Generate and display combinations for each flavor
    for flavor in flavors:
        print(f"Ice Cream Combinations for {flavor}:")
        combinations = generate_combinations([flavor], toppings)
        for combo in combinations:
            # Format the combination as a human-readable string
            toppings_text = ", ".join(combo) if combo else "No toppings"
            print(f"  - {flavor} with {toppings_text}")
        print()

    print("Enjoy exploring all the ice cream possibilities!")


if __name__ == "__main__":
    main()
