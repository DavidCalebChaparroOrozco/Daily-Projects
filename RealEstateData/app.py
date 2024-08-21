# Import necessary libraries for data handling, visualization, and mapping
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Import dataset and mapping libraries
from sklearn.datasets import fetch_california_housing
import folium
from folium import plugins

# Fetch the California housing dataset and convert it to a DataFrame
data = fetch_california_housing(as_frame=True).frame

# Initialize a folium map centered on the mean latitude and longitude of the data
m = folium.Map(location=[data['Latitude'].mean(),
                         data['Longitude'].mean()],
                         zoom_start=6)

# Determine the range for the median house value and average number of rooms
price_min, price_max = data['MedHouseVal'].min(), data['MedHouseVal'].max()
size_min, size_max = data['AveRooms'].min(), data['AveRooms'].max()

# Iterate over each row in the dataset to create markers on the map
for _, row in data.iterrows():
    # Normalize the median house value for color mapping
    normalized_price = (row['MedHouseVal'] - price_min) / (price_max - price_min)
    color = plt.cm.RdYlGn(1 - normalized_price)

    # Normalize the number of rooms for marker size
    normalized_rooms = (row["AveRooms"] - size_min) / (size_max - size_min)

    # Create a popup with detailed information about each location
    popup_info = f"""Median House Value: ${row['MedHouseVal']:.2f} <br>
    Average Rooms: {row['AveRooms']}<br>
    Population: {row['Population']}<br>
    Median Income: {row['MedInc']:.2f}<br>
    """
    
    # Add a circle marker to the map for each location, with size and color based on the data
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        # Marker size based on normalized number of rooms
        radius= 5 + 20 * normalized_rooms,  
        # Convert color to hex format for folium
        color = mcolors.to_hex(color[:3]),  
        fill=True,
        # Fill color matching the marker color
        fill_color= mcolors.to_hex(color[:3]),  
        # Set the opacity of the marker fill
        fill_opacity=0.7,  
        # Attach the popup to the marker
        popup=folium.Popup(popup_info, max_width=300)  
    ).add_to(m)

# Add a minimap plugin to the map for additional navigation context
plugins.MiniMap().add_to(m)

# Save the resulting map to an HTML file
m.save('real_estate.html')
