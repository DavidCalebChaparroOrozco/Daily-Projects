# Importing necessary libraries
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import io
import base64

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the main page
@app.route('/', methods=["GET", "POST"])
def index():
    # Handle form submission when the request method is POST
    if request.method == "POST":
        # Retrieve form data
        initial_deposit = float(request.form["initial_deposit"])
        interest_rate = float(request.form["interest_rate"])
        contribution = float(request.form["contribution"])
        compounding_type = request.form["compounding_type"]
        time_period_years = int(request.form["time_period_years"])

        # Determine the compounding frequency
        n = 12 if compounding_type == 'monthly' else 1

        # Calculate the total amount with interest over time
        total_amount = initial_deposit * (1 + interest_rate / n) ** (n * time_period_years)
        total_contributions = contribution * (((1 + interest_rate / n) ** (n * time_period_years) - 1) / (interest_rate / n))
        final_amount_with_interest = total_amount + total_contributions

        # Calculate the total contributions without interest
        total_contributions_without_interest = initial_deposit + contribution * time_period_years * n
        difference = final_amount_with_interest - total_contributions_without_interest

        # Initialize lists to store the amounts over time
        amount_with_interest = []
        amount_without_interest = []

        # Generate a list of years for the time period
        years = list(range(time_period_years + 1))

        # Calculate the amount for each year
        for year in range(time_period_years + 1):
            year_amount = initial_deposit * (1 + interest_rate / n) ** (n * year)
            year_total_contributions = contribution * (((1 + interest_rate / n) ** (n * year) - 1) / (interest_rate / n))

            year_total_contribution_without_interest = initial_deposit + contribution * year * n

            # Append the calculated amounts to the lists
            amount_with_interest.append(year_amount + year_total_contributions)
            amount_without_interest.append(year_total_contribution_without_interest)

        # Plot the results using Matplotlib
        plt.figure(figsize=(10, 5))
        plt.plot(years, amount_with_interest, marker='o', label="With Interest")
        plt.plot(years, amount_without_interest, marker='o', label="Without Interest")
        plt.title("Compound Interest Over Time Comparison")
        plt.xlabel("Years")
        plt.ylabel("Amount ($)")
        plt.grid(True)
        plt.legend()

        # Save the plot as an image in memory
        img = io.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        # Render the result template with the calculated values and the plot
        return render_template("result.html", final_amount=final_amount_with_interest, difference=difference, plot_url=plot_url)
    else:
        # Render the initial form page
        return render_template('index.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
