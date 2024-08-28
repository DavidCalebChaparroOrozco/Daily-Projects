# Function to generate all combinations of sodas recursively
def soda_combinations(sodas, current_combo=[], index=0):
    # Base case: if we have gone through all the sodas
    if index == len(sodas):
        # Print the current combination of sodas
        print(current_combo)
        return

    # Recursive case 1: include the current soda in the combination
    soda_combinations(sodas, current_combo + [sodas[index]], index + 1)

    # Recursive case 2: exclude the current soda from the combination
    soda_combinations(sodas, current_combo, index + 1)

# Main function to start the recursive process
def main():
    # List of available soda types
    sodas = ["Cola", "Lemon-Lime", "Ginger Ale", "Root Beer", "Orange Soda"]

    # Start the recursive process to generate combinations
    print("All possible soda combinations:")
    soda_combinations(sodas)

# Run the main function
if __name__ == "__main__":
    main()