import streamlit as st
import pandas as pd
import joblib
import os
import plotly.express as px
from sklearn.exceptions import ConvergenceWarning
import warnings

warnings.filterwarnings("ignore", category=ConvergenceWarning)


# Obtener rutas absolutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "model", "stacked_model.pkl")
data_path = os.path.join(BASE_DIR, "data", "enhanced_data.csv")

# Cargar modelo y datos
model = joblib.load(model_path)
df = pd.read_csv(data_path)

# Asegurar tipos correctos
df['is_team_event'] = df['is_team_event'].astype(bool)

# Columnas del modelo
features = ['country', 'sport', 'event_gender', 'event_name', 'year', 'decade',
            'host_city', 'is_team_event', 'medal_count_country', 'medal_count_sport',
            'avg_medal_event']

# Título principal
st.set_page_config(page_title="Olympic Medal Predictor", layout="wide")
st.title("🏅 Olympic Medal Predictor Dashboard by David Caleb")

# Sidebar de filtros
st.sidebar.header("🔍 Filters")

country = st.sidebar.selectbox("🌍 Country", sorted(df['country'].unique()))
sport = st.sidebar.selectbox("🏃 Sport", sorted(df['sport'].unique()))
year = st.sidebar.slider("📅 Year", int(df['year'].min()), int(df['year'].max()), 2000)

filtered = df[
    (df['country'] == country) &
    (df['sport'] == sport) &
    (df['year'] == year)
]

# 🧠 Predicción
st.subheader("🔮 Medal Prediction")

if filtered.empty:
    st.warning("No data found for this combination.")
else:
    input_data = filtered.head(1)[features]

    if st.button("Predict Medal"):
        prediction = model.predict(input_data)
        medal_map = {0: "Bronze", 1: "Gold", 2: "Silver"}
        predicted_medal = medal_map.get(prediction[0], "Unknown")
        st.success(f"🎖️ Predicted Medal: {predicted_medal}")

# 📊 Métricas Clave
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Medals", df.shape[0])
with col2:
    st.metric("Countries", df['country'].nunique())
with col3:
    st.metric("Sports", df['sport'].nunique())

# 📈 Visualización por País
st.subheader("📍 Top Countries by Total Medals")
top_countries = df.groupby('country')['medal_points'].sum().nlargest(10).reset_index()
fig_country = px.bar(top_countries, x='country', y='medal_points', color='country',
                     title="🏅 Top 10 Countries by Medal Points")
st.plotly_chart(fig_country, use_container_width=True)

# 🏅 Evolución por Año
st.subheader("📅 Medal Trend Over Years")
trend = df.groupby('year')['medal_points'].sum().reset_index()
fig_trend = px.line(trend, x='year', y='medal_points', title="📈 Total Medal Points Over Time")
st.plotly_chart(fig_trend, use_container_width=True)

# 🏆 Deporte más exitoso
st.subheader("🏆 Top Sports by Medal Count")
top_sports = df.groupby('sport')['medal_points'].sum().nlargest(10).reset_index()
fig_sport = px.bar(top_sports, x='sport', y='medal_points', color='sport',
                   title="🎽 Top 10 Sports by Medal Points")
st.plotly_chart(fig_sport, use_container_width=True)

# 🎯 Detalles por país
st.subheader(f"🔎 Medal Breakdown for {country}")
breakdown = df[df['country'] == country].groupby('medal')['athletes'].count().reset_index()
fig_breakdown = px.pie(breakdown, values='athletes', names='medal', title=f"🥇🥈🥉 Medal Distribution - {country}")
st.plotly_chart(fig_breakdown, use_container_width=True)
