# Import necessary libraries
import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from fpdf import FPDF
import streamlit as st
import plotly.express as px
from wordcloud import WordCloud
from icalendar import Calendar, Event
from datetime import datetime
from sklearn.linear_model import LinearRegression
import numpy as np

# Function to classify activities into categories
def classify_activity(activity):
    # Define keywords for each category
    categories = {
        "Recursion": ["recursion", "recursive", "backtracking"],
        "LeetCode": ["LeetCode", "Technical Test"],
        "Data Scientist (Kaggle)": ["Kaggle", "dataset", "data analysis", "data science", "data scientist", "machine learning", "TensorFlow", "Keras", "neural network", "ML", "machine learning"],
        "OOP": ["OOP", "Object-Oriented Programming", "class", "inheritance", "encapsulation", "abstraction"],
        "GUI": ["GUI", "Tkinter", "Flask", "Streamlit", "Pygame"],
        "Web Development": ["Flask", "web application", "HTML", "CSS", "JavaScript", "web", "websites", "website", "flask"],
        "Games": ["game", "Pygame", "Tic-Tac-Toe", "Pong", "Minesweeper"],
        "Data Visualization": ["Matplotlib", "Seaborn", "Plotly", "visualization"],
        # Default category for activities that don't fit elsewhere
        "Others": []  
    }

    # Check which category the activity belongs to
    for category, keywords in categories.items():
        for keyword in keywords:
            if re.search(keyword, activity, re.IGNORECASE):
                return category
    # If no category matches
    return "Others"  

# Read the README.md file
try:
    with open("C:/Users/Usuario/Desktop/Django 4 By Example/DailyProject/README.md", "r", encoding="utf-8") as file:
        content = file.readlines()
except FileNotFoundError:
    st.error("Error: The file README.md was not found. Please check the file path.")
    exit()

# Extract activities
activities = []
for line in content:
    if line.startswith("* Day"):
        activity = line.split(":")[1].strip()
        activities.append(activity)

# Classify activities into categories
classified_activities = [classify_activity(activity) for activity in activities]

# Create a DataFrame to store the data
df = pd.DataFrame({
    "Day": range(1, len(activities) + 1),
    "Activity": activities,
    "Category": classified_activities
})

# Convert 'Day' to a datetime object and extract the month and weekday
df['Date'] = pd.to_datetime('2024-03-15') + pd.to_timedelta(df['Day'] - 1, unit='D')
df['Month'] = df['Date'].dt.month_name()
df['Weekday'] = df['Date'].dt.day_name()

# Streamlit app
def streamlit_app():
    st.set_page_config(page_title="Annual Activity Portfolio by David Caleb", layout="wide")
    st.title("Annual Activity Portfolio by David Caleb")

    # Sidebar filters
    st.sidebar.title("Filters")
    date_range = st.sidebar.date_input("Select Date Range", [df['Date'].min(), df['Date'].max()])
    selected_categories = st.sidebar.multiselect("Select Categories", df['Category'].unique(), default=df['Category'].unique())

    # Filter data based on user selection
    filtered_df = df[(df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))]
    filtered_df = filtered_df[filtered_df['Category'].isin(selected_categories)]

    # Display summary statistics
    st.header("Summary Statistics")
    st.write(f"Total Activities: {len(filtered_df)}")

    if not filtered_df['Category'].mode().empty:
        st.write(f"Most Frequent Category: {filtered_df['Category'].mode()[0]} (Count: {filtered_df['Category'].value_counts().max()})")
    else:
        st.write("Most Frequent Category: No mode found (all categories are unique)")

    if not filtered_df['Month'].mode().empty:
        st.write(f"Most Productive Month: {filtered_df['Month'].mode()[0]} (Count: {filtered_df['Month'].value_counts().max()})")
    else:
        st.write("Most Productive Month: No mode found (all months are unique)")

    # Display plots
    st.header("Activity Distribution by Category")
    fig1 = px.bar(filtered_df, x='Category', y='Day', color='Category', title="Activities by Category")
    st.plotly_chart(fig1)

    st.header("Activities by Month")
    fig2 = px.bar(filtered_df, x='Month', y='Day', color='Category', title="Activities by Month")
    st.plotly_chart(fig2)

    st.header("Word Cloud of Activities")
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(filtered_df['Activity']))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

    # Gantt Chart: Activities Timeline
    st.header("Gantt Chart: Activities Timeline")
    filtered_df['Start'] = filtered_df['Date']
    filtered_df['End'] = filtered_df['Date'] + pd.Timedelta(days=1)  # Each activity lasts one day
    fig_gantt = px.timeline(
        filtered_df, 
        x_start='Start', 
        x_end='End', 
        y='Category', 
        color='Category', 
        title="Activities Timeline"
    )
    fig_gantt.update_yaxes(categoryorder="total ascending")  # Sort categories
    st.plotly_chart(fig_gantt)

    # Monthly Productivity Trends with Linear Regression
    st.header("Monthly Productivity Trends")
    monthly_activities = filtered_df.groupby('Month').size().reset_index(name='Count')
    monthly_activities['Month_Num'] = monthly_activities['Month'].apply(lambda x: datetime.strptime(x, "%B").month)
    monthly_activities = monthly_activities.sort_values('Month_Num')

    # Linear Regression
    X = monthly_activities['Month_Num'].values.reshape(-1, 1)
    y = monthly_activities['Count'].values
    model = LinearRegression()
    model.fit(X, y)
    monthly_activities['Trend'] = model.predict(X)

    fig_trend = px.line(monthly_activities, x='Month', y='Count', title="Monthly Productivity Trends")
    fig_trend.add_scatter(x=monthly_activities['Month'], y=monthly_activities['Trend'], mode='lines', name='Trend Line')
    st.plotly_chart(fig_trend)

    # Activity Distribution by Weekday
    st.header("Activity Distribution by Weekday")
    weekday_distribution = filtered_df['Weekday'].value_counts().reindex([
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    ]).reset_index()
    weekday_distribution.columns = ['Weekday', 'Count']
    fig_weekday = px.bar(weekday_distribution, x='Weekday', y='Count', title="Activity Distribution by Weekday")
    st.plotly_chart(fig_weekday)

    # Export to PDF
    st.header("Export to PDF")
    if st.button("Generate PDF Report"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add title
        pdf.cell(200, 10, txt="Annual Activity Portfolio", ln=True, align="C")

        # Add summary statistics
        pdf.cell(200, 10, txt="=== Summary Statistics ===", ln=True)
        pdf.cell(200, 10, txt=f"Total Activities: {len(filtered_df)}", ln=True)
        pdf.cell(200, 10, txt=f"Most Frequent Category: {filtered_df['Category'].mode()[0]} (Count: {filtered_df['Category'].value_counts().max()})", ln=True)
        pdf.cell(200, 10, txt=f"Most Productive Month: {filtered_df['Month'].mode()[0]} (Count: {filtered_df['Month'].value_counts().max()})", ln=True)

        # Save the PDF
        pdf.output("Annual_Portfolio.pdf")
        st.success("PDF report generated successfully!")

    # Download Data and Charts
    st.header("Download Data and Charts")
    if st.button("Download Data as CSV"):
        filtered_df.to_csv("activities.csv", index=False)
        st.success("Data downloaded as CSV!")

    if st.button("Download Gantt Chart as PNG"):
        fig_gantt.write_image("gantt_chart.png")
        st.success("Gantt Chart downloaded as PNG!")

# Run Streamlit app
if __name__ == "__main__":
    streamlit_app()