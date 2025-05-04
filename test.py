# list = ["Python", "Java", "C++", "C#"]

# for i, lenguaje in enumerate(list):
#     print(i, lenguaje)

"""
Customer Retention Rate KPI Calculator
This script calculates the percentage of customers who return during a specific period.
The retention rate is a key metric for understanding customer loyalty and business health.
"""

def calculate_retention_rate(returning_customers, total_customers_at_start, period_name):
    """
    Calculate the customer retention rate for a given period.
    
    Parameters:
    - returning_customers (int): Number of customers who made repeat purchases
    - total_customers_at_start (int): Total customers at beginning of period
    - period_name (str): Name of the period being analyzed (e.g., "Q1 2023")
    
    Returns:
    - float: Retention rate percentage
    - str: Formatted output string with the results
    """
    
    # Validate input values
    if total_customers_at_start <= 0:
        raise ValueError("Total customers must be greater than zero")
    if returning_customers < 0:
        raise ValueError("Returning customers cannot be negative")
    if returning_customers > total_customers_at_start:
        raise ValueError("Returning customers cannot exceed total customers")
    
    # Calculate retention rate percentage
    retention_rate = (returning_customers / total_customers_at_start) * 100
    
    # Create formatted output
    result_str = (f"\nCustomer Retention Rate Analysis - {period_name}\n"
                    f"==========================================\n"
                    f"Total customers at start: {total_customers_at_start:,}\n"
                    f"Returning customers: {returning_customers:,}\n"
                    f"Retention Rate: {retention_rate:.2f}%\n")
    
    return retention_rate, result_str

def analyze_retention_trends(period_data):
    """
    Analyze retention trends across multiple periods and provide insights.
    
    Parameters:
    - period_data (list of dicts): List containing period data with keys:
        'period_name', 'returning_customers', 'total_customers_at_start'
    
    Returns:
    - str: Formatted analysis of retention trends
    """
    
    if not period_data:
        return "No data provided for analysis"
    
    analysis = "\nCustomer Retention Trend Analysis\n"
    analysis += "=================================\n"
    
    rates = []
    for period in period_data:
        try:
            rate, result = calculate_retention_rate(
                period['returning_customers'],
                period['total_customers_at_start'],
                period['period_name']
            )
            rates.append(rate)
            analysis += result + "\n"
        except ValueError as e:
            analysis += f"Error analyzing {period['period_name']}: {str(e)}\n"
    
    if len(rates) > 1:
        trend = "improving" if rates[-1] > rates[0] else "declining" if rates[-1] < rates[0] else "stable"
        analysis += f"\nOverall Trend: Retention rate is {trend} across periods\n"
        analysis += f"Starting Rate: {rates[0]:.2f}% | Ending Rate: {rates[-1]:.2f}%\n"
    
    return analysis

def main():
    """Main function to demonstrate the retention rate calculation"""
    
    # Example data for demonstration
    sample_data = [
        {
            'period_name': "Q1 2023",
            'returning_customers': 450,
            'total_customers_at_start': 1000
        },
        {
            'period_name': "Q2 2023",
            'returning_customers': 480,
            'total_customers_at_start': 1100
        },
        {
            'period_name': "Q3 2023",
            'returning_customers': 520,
            'total_customers_at_start': 1200
        }
    ]
    
    # Calculate and display retention analysis
    print(analyze_retention_trends(sample_data))
    
    # Single period calculation example
    try:
        rate, result = calculate_retention_rate(300, 500, "Q4 2023")
        print(result)
    except ValueError as e:
        print(f"Calculation error: {str(e)}")

if __name__ == "__main__":
    main()