# Import necessary libraries
import streamlit as st
import pandas as pd
import joblib
import os
import plotly.express as px
from sklearn.exceptions import ConvergenceWarning
import warnings

# Ignore convergence warnings
warnings.filterwarnings("ignore", category=ConvergenceWarning)

# Get absolute paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "model", "stacked_model.pkl")
data_path = os.path.join(BASE_DIR, "data", "enhanced_data.csv")

# Load model and data
try:
    model = joblib.load(model_path)
    df = pd.read_csv(data_path)
    
    # Convert columns to proper types
    df['is_team'] = df['is_team'].astype(bool)
    df['is_team_event'] = df['is_team_event'].astype(bool)
    df['year_date'] = pd.to_datetime(df['year_date'])
    
    # Create medal mapping
    medal_map = {0: "Bronze", 1: "Gold", 2: "Silver"}
    df['medal_name'] = df['medal_encoded'].map(medal_map)
    
except Exception as e:
    st.error(f"Error loading data or model: {str(e)}")
    st.stop()

# Features used in the model
features = ['country', 'sport', 'event_gender', 'event_name', 'year', 'decade',
            'host_city', 'is_team_event', 'medal_count_country', 'medal_count_sport',
            'avg_medal_event']

# Page configuration
st.set_page_config(page_title="Olympic Medal Predictor", layout="wide")
st.title("🏅 Olympic Medal Predictor Dashboard")

# Sidebar filters
st.sidebar.header("🔍 Filters")

# Add season filter
season_options = {0: "Summer", 1: "Winter"}
selected_season = st.sidebar.selectbox(
    "🌞❄️ Season",
    options=list(season_options.keys()),
    format_func=lambda x: season_options[x]
)

# Filter countries and sports based on selected season
filtered_df = df[df['season'] == selected_season]
countries = sorted(filtered_df['country'].unique())
sports = sorted(filtered_df['sport'].unique())

country = st.sidebar.selectbox("🌍 Country", countries)
sport = st.sidebar.selectbox("🏃 Sport", sports)
year = st.sidebar.slider(
    "📅 Year", 
    int(df['year'].min()), 
    int(df['year'].max()), 
    int(df[df['year'] >= 2000]['year'].min())
)

# Filter dataset for prediction
filtered = df[
    (df['country'] == country) &
    (df['sport'] == sport) &
    (df['year'] == year) &
    (df['season'] == selected_season)
]

# Prediction section
st.subheader("🔮 Medal Prediction")

if filtered.empty:
    st.warning("No historical data found for this combination. Making prediction based on similar events.")
    # Create synthetic input for prediction
    input_data = pd.DataFrame([{
        'country': country,
        'sport': sport,
        'event_gender': 0,  # Default value
        'event_name': 0,    # Default value
        'year': year,
        'decade': year // 10 * 10,
        'host_city': 0,     # Default value
        'is_team_event': False,
        'medal_count_country': df[df['country'] == country]['medal_count_country'].mean(),
        'medal_count_sport': df[df['sport'] == sport]['medal_count_sport'].mean(),
        'avg_medal_event': df['avg_medal_event'].mean()
    }])
else:
    input_data = filtered.head(1)[features]

if st.button("Predict Medal"):
    try:
        prediction = model.predict(input_data)
        predicted_medal = medal_map.get(prediction[0], "Unknown")
        
        # Show animated celebration for gold medal prediction
        if predicted_medal == "Gold":
            st.balloons()
        
        st.success(f"🎖️ Predicted Medal: {predicted_medal}")
        
        # Show probability estimates if available
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(input_data)[0]
            proba_df = pd.DataFrame({
                "Medal": ["Bronze", "Gold", "Silver"],
                "Probability": proba
            })
            fig_proba = px.bar(proba_df, x="Medal", y="Probability", 
                              color="Medal", title="Probability Estimates")
            st.plotly_chart(fig_proba, use_container_width=True)
            
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")

# Key metrics section
st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Medals", df.shape[0])
with col2:
    st.metric("Countries", df['country'].nunique())
with col3:
    st.metric("Sports", df['sport'].nunique())
with col4:
    st.metric("Years Covered", f"{df['year'].min()} - {df['year'].max()}")

# Tabs for different visualizations
tab1, tab2, tab3 = st.tabs(["Country Analysis", "Sport Analysis", "Historical Trends"])

with tab1:
    st.subheader(f"🇺🇳 {country} Performance Analysis")
    
    # Country medal trend
    country_trend = df[df['country'] == country].groupby(['year', 'medal_name']).size().unstack().fillna(0)
    fig_country_trend = px.line(country_trend, x=country_trend.index, y=["Gold", "Silver", "Bronze"],
                               title=f"Medal Trend for {country}")
    st.plotly_chart(fig_country_trend, use_container_width=True)
    
    # Country sport distribution
    country_sports = df[df['country'] == country].groupby('sport')['medal_name'].count().nlargest(10)
    fig_country_sports = px.pie(country_sports, names=country_sports.index, values=country_sports.values,
                               title=f"Top Sports for {country}")
    st.plotly_chart(fig_country_sports, use_container_width=True)

with tab2:
    st.subheader(f"🏅 {sport} Analysis")
    
    # Sport medal trend
    sport_trend = df[df['sport'] == sport].groupby(['year', 'medal_name']).size().unstack().fillna(0)
    fig_sport_trend = px.line(sport_trend, x=sport_trend.index, y=["Gold", "Silver", "Bronze"],
                             title=f"Medal Trend in {sport}")
    st.plotly_chart(fig_sport_trend, use_container_width=True)
    
    # Top countries in this sport
    sport_countries = df[df['sport'] == sport].groupby('country')['medal_name'].count().nlargest(10)
    fig_sport_countries = px.bar(sport_countries, x=sport_countries.index, y=sport_countries.values,
                                color=sport_countries.index,
                                title=f"Top Countries in {sport}")
    st.plotly_chart(fig_sport_countries, use_container_width=True)

with tab3:
    st.subheader("📈 Historical Trends")
    
    # Overall medal trend
    overall_trend = df.groupby(['year', 'medal_name']).size().unstack().fillna(0)
    fig_overall_trend = px.line(overall_trend, x=overall_trend.index, y=["Gold", "Silver", "Bronze"],
                               title="Overall Olympic Medal Trend")
    st.plotly_chart(fig_overall_trend, use_container_width=True)
    
    # Top countries of all time
    top_countries = df.groupby('country')['medal_points'].sum().nlargest(10).reset_index()
    fig_top_countries = px.bar(top_countries, x='country', y='medal_points', color='country',
                              title="🏆 Top Countries by Total Medal Points")
    st.plotly_chart(fig_top_countries, use_container_width=True)

# Data explorer section
st.subheader("🔍 Data Explorer")
with st.expander("View raw data"):
    st.dataframe(df.head(100))

# Add footer
st.markdown("---")
st.markdown("""
    **Olympic Medal Predictor**  
    *Using historical data to predict future Olympic success*  
    Data source: Olympic history dataset
""")