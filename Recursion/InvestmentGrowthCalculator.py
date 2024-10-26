# Recursive Investment Growth Calculator
# This program calculates the future balance of an investment in USD based on compound interest using recursion.

# Calculate the compound interest recursively.
def compound_interest_recursive(principal, rate, years):
    """
    principal: The initial investment amount (USD).
    rate: The annual interest rate (as a decimal).
    years: The number of years to calculate.
    """
    # Base case: if no more years are left, return the principal
    if years == 0:
        return principal
    
    # Recursive case: calculate the interest for the current year and add it to the next year's result
    return compound_interest_recursive(principal * (1 + rate), rate, years - 1)

# Display the year-by-year growth of an investment.
def investment_growth_report(principal, rate, years):
    """
    principal: The initial investment amount (USD).
    rate: The annual interest rate (as a decimal).
    years: The total number of years to display.
    """
    print(f"Initial Investment: ${principal:.2f}")
    print(f"Annual Interest Rate: {rate * 100}%")
    print(f"Investment Period: {years} years\n")
    
    # Display the investment growth for each year
    for year in range(1, years + 1):
        future_value = compound_interest_recursive(principal, rate, year)
        print(f"Year {year}: ${future_value:.2f}")

# Example Usage

# Initial amount in USD
initial_investment = 1000.0  
# 5% interest rate
annual_interest_rate = 0.05  
# Number of years
investment_period = 10       

investment_growth_report(initial_investment, annual_interest_rate, investment_period)
