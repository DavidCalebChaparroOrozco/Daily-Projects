from flask import Flask, render_template, request

app = Flask(__name__)

# Home route that displays the BMI form
@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None  # Variable to store the BMI result
    category = None  # Variable to store the health recommendation
    if request.method == "POST":
        # Get the weight and height from the form inputs
        weight = float(request.form.get("weight"))
        height = float(request.form.get("height"))

        # BMI calculation (weight in kg, height in meters)
        bmi = round(weight / (height ** 2), 2)

        # Health recommendation based on BMI value
        if bmi < 18.5:
            category = "Underweight - You should aim to gain some weight."
        elif 18.5 <= bmi <= 24.9:
            category = "Normal weight - You are in a healthy range."
        elif 25 <= bmi <= 29.9:
            category = "Overweight - You should aim to lose some weight."
        else:
            category = "Obese - It's important to consult a healthcare provider."

    return render_template("index.html", bmi=bmi, category=category)

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
