# Import necessary libraries
from flask import Flask, render_template, jsonify
import pandas as pd
import plotly
import plotly.express as px
import json
import numpy as np

app = Flask(__name__)

# Advanced data preprocessing function
def preprocess_data(data):
    """    
    Args:
        data: Raw sales dataframe
    Returns:
        pandas.DataFrame: Cleaned and transformed dataframe
    """
    # Remove duplicates
    data.drop_duplicates(inplace=True)
    
    # Handle missing values
    data.fillna({
        'amount': data['amount'].mean(),
        'category': 'Unknown'
    }, inplace=True)
    
    # Convert date column
    data['date'] = pd.to_datetime(data['date'])
    
    # Create additional features
    data['month'] = data['date'].dt.month
    data['year'] = data['date'].dt.year
    
    return data

# Calculate month-over-month sales growth
def calculate_sales_growth(data):
    """    
    Args:
        data: Sales dataframe
    Returns:
        float: Sales growth percentage
    """
    monthly_sales = data.groupby(pd.Grouper(key='date', freq='M'))['amount'].sum()
    growth_rate = (monthly_sales.pct_change() * 100).mean()
    
    return growth_rate

# Perform advanced sales analysis
def advanced_sales_analysis(data):
    """    
    Args:
        data: Preprocessed sales dataframe
    Returns:
        dict: Advanced sales insights
    """
    insights = {
        'total_sales': float(data['amount'].sum()),
        'average_sale': float(data['amount'].mean()),
        'top_categories': data.groupby('category')['amount'].sum().nlargest(3).to_dict(),
        'sales_growth': calculate_sales_growth(data)
    }
    
    return insights

# Load and preprocess sales data
def load_data():
    """
    Returns:
        pandas.DataFrame: Preprocessed sales dataframe
    """
    raw_data = pd.read_csv('data/sales.csv')
    return preprocess_data(raw_data)

# Main dashboard route
@app.route('/')
def dashboard():
    """    
    Returns:
        Rendered HTML template with sales charts and insights
    """
    # Load sales dataframe
    data = load_data()
    
    # Create sales by category chart
    sales_by_category = data.groupby('category')['amount'].sum().reset_index()
    fig_category = px.bar(
        sales_by_category, 
        x='category', 
        y='amount', 
        title='Sales by Category'
    )
    category_chart = json.dumps(fig_category, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Create monthly sales chart
    monthly_sales = data.groupby(data['date'].dt.to_period('M'))['amount'].sum().reset_index()
    monthly_sales['date'] = monthly_sales['date'].astype(str)
    
    fig_monthly = px.line(
        monthly_sales, 
        x='date', 
        y='amount', 
        title='Monthly Sales'
    )
    monthly_chart = json.dumps(fig_monthly, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Get advanced sales insights
    sales_insights = advanced_sales_analysis(data)
    
    return render_template(
        'index.html', 
        category_chart=category_chart,
        monthly_chart=monthly_chart,
        insights=sales_insights
    )

# API route to return sales insights
@app.route('/insights')
def get_insights():
    """    
    Returns:
        JSON response with sales insights
    """
    data = load_data()
    insights = advanced_sales_analysis(data)
    return jsonify(insights)

if __name__ == '__main__':
    app.run(debug=True)
