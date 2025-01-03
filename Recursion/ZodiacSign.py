# Determines the Western zodiac sign based on the birth date.
def zodiac_sign(day, month):
    """    
    Parameters:
    day: Day of birth
    month: Month of birth (in lowercase)
    Returns:
    str: The zodiac sign
    """
    if month == 'december':
        return 'Sagittarius' if day < 22 else 'Capricorn'
    elif month == 'january':
        return 'Capricorn' if day < 20 else 'Aquarius'
    elif month == 'february':
        return 'Aquarius' if day < 19 else 'Pisces'
    elif month == 'march':
        return 'Pisces' if day < 21 else 'Aries'
    elif month == 'april':
        return 'Aries' if day < 20 else 'Taurus'
    elif month == 'may':
        return 'Taurus' if day < 21 else 'Gemini'
    elif month == 'june':
        return 'Gemini' if day < 21 else 'Cancer'
    elif month == 'july':
        return 'Cancer' if day < 23 else 'Leo'
    elif month == 'august':
        return 'Leo' if day < 23 else 'Virgo'
    elif month == 'september':
        return 'Virgo' if day < 23 else 'Libra'
    elif month == 'october':
        return 'Libra' if day < 23 else 'Scorpio'
    elif month == 'november':
        return 'Scorpio' if day < 22 else 'Sagittarius'


# Determines the Chinese zodiac sign based on the birth year.
def chinese_zodiac(year):
    """    
    Parameters:
    year (int): Year of birth
    
    Returns:
    str: The Chinese zodiac sign
    """
    animals = [
        "Rat", "Ox", "Tiger", 
        "Rabbit", "Dragon", "Snake", 
        "Horse", "Goat", "Monkey", 
        "Rooster", "Dog", "Pig"
    ]
    
    # The Chinese zodiac cycle is based on a 12-year cycle
    return animals[year % 12]

def main():
    # Input: Date of birth
    birth_date = input("Enter your birth date (DD-MM-YYYY): ")
    
    # Extracting day, month, and year from input
    day, month, year = map(int, birth_date.split('-'))
    
    # Convert numeric month to string format
    months = ["", "january", "february", "march", "april",
                "may", "june", "july", "august",
                "september", "october", "november", "december"]
    
    # Get zodiac signs
    western_sign = zodiac_sign(day, months[month])
    chinese_sign = chinese_zodiac(year)
    
    # Display results
    print(f"Your Western Zodiac Sign is: {western_sign}")
    print(f"Your Chinese Zodiac Sign is: {chinese_sign}")

if __name__ == '__main__':
    main()