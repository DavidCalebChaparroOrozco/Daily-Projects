# Importing necessary libraries
import json
import requests
from fpdf import FPDF
from flask import Flask, request, render_template
from dotenv import load_dotenv
import os

# Loading environment variables
load_dotenv()

# Retrieving API key, host, and URL from environment variables
API_KEY = os.getenv('API_KEY')
API_HOST = os.getenv('API_HOST')
API_URL = os.getenv('API_URL')

# Initializing Flask app
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for predicting weather based on user input
@app.route('/predict_weather', methods=['POST'])
def predict_weather():
    if request.method == 'POST':
        # Extracting location from form input
        q = request.form['location']
        url = API_URL
        querystring = {"q": q}
        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": API_HOST
        }
        try:
            # Making request to weather API
            response = requests.request("GET", url, headers=headers, params=querystring)
            json_data = json.loads(response.text)

            # Extracting weather information from JSON response
            name = json_data['location']['name']
            region = json_data['location']['region']
            country = json_data['location']['country']
            lat = json_data['location']['lat']
            lon = json_data['location']['lon']
            tz_id = json_data['location']['tz_id']
            localtime_epoch = json_data['location']['localtime_epoch']
            localtime = json_data['location']['localtime']
            last_updated_epoch = json_data['current']['last_updated_epoch']
            last_updated = json_data['current']['last_updated']
            temp_c = json_data['current']['temp_c']
            temp_f = json_data['current']['temp_f']
            is_day = json_data['current']['is_day']
            condition_text = json_data['current']['condition']['text']
            condition_icon = json_data['current']['condition']['icon']
            wind_mph = json_data['current']['wind_mph']
            wind_kph = json_data['current']['wind_kph']
            wind_degree = json_data['current']['wind_degree']
            wind_dir = json_data['current']['wind_dir']
            pressure_mb = json_data['current']['pressure_mb']
            pressure_in = json_data['current']['pressure_in']
            precip_mm = json_data['current']['precip_mm']
            precip_in = json_data['current']['precip_in']
            humidity = json_data['current']['humidity']
            cloud = json_data['current']['cloud']
            feelslike_c = json_data['current']['feelslike_c']
            feelslike_f = json_data['current']['feelslike_f']
            vis_km = json_data['current']['vis_km']
            vis_miles = json_data['current']['vis_miles']
            uv = json_data['current']['uv']
            gust_mph = json_data['current']['gust_mph']
            gust_kph = json_data['current']['gust_kph']

            # Rendering weather information on home page
            return render_template('home.html', name=name, region=region, country=country, lat=lat, lon=lon, tz_id=tz_id,
                                    localtime_epoch=localtime_epoch, localtime=localtime,
                                    last_updated_epoch=last_updated_epoch, last_updated=last_updated,
                                    temp_c=temp_c, temp_f=temp_f, is_day=is_day, condition_text=condition_text,
                                    condition_icon=condition_icon, wind_mph=wind_mph, wind_kph=wind_kph,
                                    wind_degree=wind_degree, wind_dir=wind_dir, pressure_mb=pressure_mb,
                                    pressure_in=pressure_in, precip_mm=precip_mm, precip_in=precip_in,
                                    humidity=humidity, cloud=cloud, feelslike_c=feelslike_c, feelslike_f=feelslike_f,
                                    vis_km=vis_km, vis_miles=vis_miles, uv=uv, gust_mph=gust_mph, gust_kph=gust_kph)

        except:
            # Handling invalid input
            return render_template('home.html', error='Please enter a correct Place name...')

if __name__ == '__main__':
    # Running the Flask app
    app.run(debug=True)
