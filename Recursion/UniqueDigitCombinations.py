
# Recursively finds all combinations of unique digits that sum up to the target value.
def find_unique_digit_combinations(target, max_digits=9, current_combination=None, start_digit=1, all_combinations=None):
    """    
    Args:
        target: The desired sum for the digit combinations.
        max_digits: Maximum number of digits allowed in a combination (default 9 since digits 1-9).
        current_combination: Current combination being built (used in recursion).
        start_digit: The digit to start with (used in recursion to avoid duplicates).
        all_combinations: List to store all valid combinations (used in recursion).    
    Returns:
        list: All valid combinations of digits that sum to the target.
    """
    # Initialize variables on first call
    if all_combinations is None:
        all_combinations = []
    if current_combination is None:
        current_combination = []
    
    # Base case: if current combination sums to target, add to results
    if sum(current_combination) == target:
        all_combinations.append(current_combination.copy())
        return
    
    # Base case: if sum exceeds target or we've used maximum digits, stop recursion
    if sum(current_combination) >= target or len(current_combination) >= max_digits:
        return
    
    # Recursive case: try adding each digit from start_digit to 9
    for digit in range(start_digit, 10):
        # Skip if digit is already in the current combination
        if digit in current_combination:
            continue
            
        current_combination.append(digit)
        # Recursive call with updated parameters
        find_unique_digit_combinations(
            target,
            max_digits,
            current_combination,
            # Ensure next digits are larger to avoid duplicate combinations
            digit + 1,  
            all_combinations
        )
        current_combination.pop()  # Backtrack
    
    return all_combinations

# Displays the combinations in a user-friendly format.
def display_combinations(combinations):
    """    
    Args:
        combinations: List of digit combinations to display.
    """
    if not combinations:
        print("No valid combinations found.")
        return
    
    print(f"Found {len(combinations)} unique combinations:")
    for i, combo in enumerate(combinations, 1):
        # Format the combination as digits separated by '+'
        combo_str = " + ".join(map(str, combo))
        print(f"{i}. {combo_str} = {sum(combo)}")

def main():
    print("Unique Digit Combinations Generator by David Caleb")
    print("Finds all combinations of unique digits (1-9) that sum to a target value.")
    
    while True:
        try:
            target = int(input("\nEnter target sum (0 to exit): "))
            if target == 0:
                break
            if target < 1:
                print("Please enter a positive integer.")
                continue
                
            # No combination can have more digits than the target sum
            max_digits = min(9, target)  
            combinations = find_unique_digit_combinations(target, max_digits)
            display_combinations(combinations)
            
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()