# Importing necessaries libraries
from flask import Flask, render_template, request, redirect, url_for
import plotly.express as px
import pycountry
import pandas as pd
import os

app = Flask(__name__)

# Function to validate the country names
def validate_country(country_name):
    try:
        return pycountry.countries.lookup(country_name).name
    except LookupError:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Retrieve the country names and values from the form
        countries = request.form.getlist("country")
        values = request.form.getlist("value")
        
        # Validate countries and remove invalid entries
        valid_countries = []
        country_values = []
        for i in range(len(countries)):
            country = countries[i].strip()
            value = values[i].strip()
            valid_country = validate_country(country)
            if valid_country and value.isdigit():
                valid_countries.append(valid_country)
                country_values.append(int(value))
            else:
                return render_template("index.html", error=f"Invalid country '{country}' or non-numeric value '{value}'. Please correct the input.")
        
        # If valid data, create the map
        if valid_countries:
            # Create DataFrame from valid data
            data = pd.DataFrame({"Country": valid_countries, "Values": country_values})
            
            # Generate the choropleth map
            fig = px.choropleth(
                data,
                locations='Country',
                locationmode='country names',
                color='Values',
                color_continuous_scale='Viridis',
                title=f'Country Map Highlighting {", ".join(valid_countries)}'
            )
            # Save the map as an HTML file to be displayed in the template
            fig_html = os.path.join("static", "map.html")
            fig.write_html(fig_html)
            
            return render_template("index.html", map_generated=True, map_url=fig_html)
    
    # GET request will render the main form page
    return render_template("index.html", map_generated=False)

if __name__ == "__main__":
    app.run(debug=True)
