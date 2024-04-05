import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objs as go

st.write("""
# Simple Stock Price App
""")

# Define a dictionary of ticker symbols with corresponding company names
ticker_symbols = {
    'Google (GOOGL)': 'GOOGL',
    'Amazon (AMZN)': 'AMZN',
    'Microsoft (MSFT)': 'MSFT',
    'Nvidia (NVDA)': 'NVDA',
    'Apple (AAPL)': 'AAPL',
    'Facebook (META)': 'META',
    'Tesla (TSLA)': 'TSLA',
    'Alphabet (GOOG)': 'GOOG',
    'Netflix (NFLX)': 'NFLX',
    'Visa (V)': 'V',
    'JPMorgan Chase (JPM)': 'JPM',
    'Johnson & Johnson (JNJ)': 'JNJ',
    'Procter & Gamble (PG)': 'PG',
    'Walmart (WMT)': 'WMT',
    'Mastercard (MA)': 'MA',
    'Intel (INTC)': 'INTC',
    'Adobe (ADBE)': 'ADBE',
    'PayPal (PYPL)': 'PYPL',
    'Cisco (CSCO)': 'CSCO',
    'Broadcom (AVGO)': 'AVGO',
    'Netflix (NFLX)': 'NFLX',
    'Salesforce (CRM)': 'CRM',
    'Oracle (ORCL)': 'ORCL',
    'IBM (IBM)': 'IBM',
    'Coca-Cola (KO)': 'KO',
    'PepsiCo (PEP)': 'PEP',
    'McDonalds (MCD)': 'MCD',
    'Starbucks (SBUX)': 'SBUX',
    'Home Depot (HD)': 'HD',
    'Boeing (BA)': 'BA',
    'General Electric (GE)': 'GE',
    'Exxon Mobil (XOM)': 'XOM',
    'Chevron (CVX)': 'CVX',
    'AT&T (T)': 'T',
    'Verizon (VZ)': 'VZ',
    'Ford (F)': 'F',
    'General Motors (GM)': 'GM'
    # Add more ticker symbols here
}


# Dropdown for selecting ticker symbol
selected_ticker = st.selectbox('Select Ticker Symbol', list(ticker_symbols.keys()))

# Get corresponding ticker symbol
ticker_symbol = ticker_symbols[selected_ticker]

# Get current date
end_date = datetime.now().strftime('%Y-%m-%d')

# Get data on the ticker symbol
try:
    tickerData = yf.Ticker(ticker_symbol)
    tickerDf = tickerData.history(period='1d', start="2010-5-31", end=end_date)

    # Display company name
    st.write(f"## Company Name: {selected_ticker.split(' (')[0]}")

    # Displaying closing price chart
    st.write("""
    ## Closing Price
    """)
    st.line_chart(tickerDf.Close)

    # Displaying volume chart
    st.write("""
    ## Volume
    """)
    st.line_chart(tickerDf.Volume)
    
    # Create candlestick chart
    candlestick = go.Candlestick(x=tickerDf.index,
                                open=tickerDf['Open'],
                                high=tickerDf['High'],
                                low=tickerDf['Low'],
                                close=tickerDf['Close'])

    layout = go.Layout(title=f'Candlestick Chart for {selected_ticker.split(" (")[0]} ({ticker_symbol})',
                        xaxis=dict(title='Date'),
                        yaxis=dict(title='Price'))

    candlestick_fig = go.Figure(data=[candlestick], layout=layout)

    # Display candlestick chart
    st.write("""
    ## Candlestick Chart
    """)
    st.plotly_chart(candlestick_fig)
    
    # Calculate performance metrics
    returns = tickerDf['Close'].pct_change().mean() * 252
    volatility = tickerDf['Close'].pct_change().std() * (252**0.5)
    sharpe_ratio = returns / volatility

    # Display performance metrics
    st.write("""
    ## Performance Metrics
    """)
    st.write(f"### Returns: {returns:.2%}")
    st.write(f"### Volatility: {volatility:.2%}")
    st.write(f"### Sharpe Ratio: {sharpe_ratio:.2}")

except Exception as e:
    st.error(f"Error occurred: {e}")
