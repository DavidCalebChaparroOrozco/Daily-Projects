def get_custom_ranges():
    print("Enter your custom grade ranges.")
    custom_ranges = {}
    
    # Get letter grades and their corresponding ranges from user
    while True:
        letter_grade = input("Enter letter grade (or type 'done' to finish): ").strip().upper()
        if letter_grade == 'DONE':
            break
        
        try:
            min_range = float(input(f"Enter minimum score for {letter_grade}: "))
            max_range = float(input(f"Enter maximum score for {letter_grade}: "))
            if min_range > max_range:
                print("Minimum range cannot be greater than maximum range. Please try again.")
                continue
            
            custom_ranges[letter_grade] = (min_range, max_range)
        except ValueError:
            print("Invalid input. Please enter numeric values for ranges.")
    
    return custom_ranges

def convert_grade(numeric_grade, custom_ranges):
    for letter, (min_score, max_score) in custom_ranges.items():
        if min_score <= numeric_grade <= max_score:
            return letter
    return "Invalid Grade"

def main():
    print("Welcome to the Grade Converter!")
    
    # Get custom grade ranges from user
    custom_ranges = get_custom_ranges()
    
    while True:
        try:
            numeric_grade = float(input("Enter a numeric grade (or type 'exit' to quit): "))
            if numeric_grade < 0 or numeric_grade > 100:
                print("Please enter a valid grade between 0 and 100.")
                continue
            
            letter_grade = convert_grade(numeric_grade, custom_ranges)
            print(f"The letter grade for {numeric_grade} is: {letter_grade}")
        
        except ValueError:
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
