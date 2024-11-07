# Function to calculate BMR using the Harris-Benedict equation
def calculate_bmr(weight, height, age, gender):
    """
    Parameters:
    weight: Weight in kilograms
    height: Height in centimeters
    age: Age in years
    gender: 'male' or 'female'
    
    Returns:
    float: Calculated BMR
    """
    if gender.lower() == 'male':
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:  # female
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

# Function to calculate TDEE based on activity level
def calculate_tdee(bmr, activity_level):
    """
    Parameters:
    bmr: Basal Metabolic Rate
    activity_level: Activity level ('sedentary', 'light', 'moderate', 'active', 'very active')
    
    Returns:
    float: Total Daily Energy Expenditure
    """
    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very active': 1.9
    }
    
    return bmr * activity_multipliers.get(activity_level.lower(), 1)

# Recursive function to process a list of individuals' data for TDEE calculation
def process_tdee_data(data, index=0):
    """    
    Parameters:
    data: Each tuple contains (weight, height, age, gender, activity_level)
    index: Current index in the data list for recursion
    
    rns:
    list: A list of results containing BMR and TDEE for each individual
    """
    # Base case: if index is equal to the length of data, return an empty list
    if index == len(data):
        return []

    # Extract individual data from the current tuple
    weight, height, age, gender, activity_level = data[index]
    
    # Calculate BMR
    bmr = calculate_bmr(weight, height, age, gender)
    
    # Calculate TDEE based on BMR and activity level
    tdee = calculate_tdee(bmr, activity_level)
    
    # Recursive call for the next individual
    return [(weight, height, age, gender, bmr, tdee)] + process_tdee_data(data, index + 1)

# Sample data: List of tuples with (weight in kg, height in cm, age in years, gender, activity level)
health_data = [
    (70, 175, 25, 'male', 'moderate'),
    (60, 160, 30, 'female', 'light'),
    (80, 180, 40, 'male', 'active'),
]

# Process the health data recursively and print results
results = process_tdee_data(health_data)
for result in results:
    weight, height, age, gender, bmr, tdee = result
    print(f"Weight: {weight} kg, Height: {height} cm, Age: {age} years, Gender: {gender}, "
        f"BMR: {bmr:.2f} kcal/day, TDEE: {tdee:.2f} kcal/day")