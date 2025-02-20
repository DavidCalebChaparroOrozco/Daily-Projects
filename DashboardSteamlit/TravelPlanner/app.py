# Import necessary libraries
import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

# Set up the title of the app
st.title("🌍 Travel Planner App by David Caleb")
st.write("Plan your trip with ease! Create itineraries, estimate budgets, and get recommendations for places to visit.")

# Initialize session state for itinerary if it doesn't exist
if "itinerary" not in st.session_state:
    st.session_state.itinerary = pd.DataFrame(columns=["Activity", "Date", "Cost", "Category", "Priority"])

# Sidebar for user inputs
st.sidebar.header("User Preferences")
destination = st.sidebar.text_input("Enter your destination:")
start_date = st.sidebar.date_input("Start date", datetime.date.today())
end_date = st.sidebar.date_input("End date", datetime.date.today() + datetime.timedelta(days=7))
budget = st.sidebar.number_input("Estimated budget (in USD):", min_value=0, value=1000)

# Main content
st.header("✈️ Itinerary Planner")

# Create a form for itinerary input
with st.form("itinerary_form"):
    st.write("Add activities to your itinerary:")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        activity = st.text_input("Activity:")
    with col2:
        activity_date = st.date_input("Date:", datetime.date.today())
    with col3:
        activity_cost = st.number_input("Estimated cost (in USD):", min_value=0, value=0)
    with col4:
        activity_category = st.selectbox("Category:", ["Transport", "Accommodation", "Food", "Entertainment", "Other"])
    priority = st.select_slider("Priority:", options=["Low", "Medium", "High"])
    submitted = st.form_submit_button("Add Activity")

# Add activity to itinerary if form is submitted
if submitted:
    new_activity = pd.DataFrame({
        "Activity": [activity],
        "Date": [activity_date],
        "Cost": [activity_cost],
        "Category": [activity_category],
        "Priority": [priority]
    })
    st.session_state.itinerary = pd.concat([st.session_state.itinerary, new_activity], ignore_index=True)
    st.success("Activity added!")

# Display the itinerary
st.subheader("Your Itinerary")
if not st.session_state.itinerary.empty:
    st.dataframe(st.session_state.itinerary)
    total_cost = st.session_state.itinerary["Cost"].sum()
    st.write(f"**Total estimated cost: ${total_cost}**")
else:
    st.write("No activities added yet.")

# Budget tracker
st.header("💰 Budget Tracker")
st.write(f"Your estimated budget: **${budget}**")
if not st.session_state.itinerary.empty:
    remaining_budget = budget - total_cost
    if remaining_budget >= 0:
        st.success(f"Remaining budget: **${remaining_budget}**")
    else:
        st.error(f"⚠️ You are over budget by **${-remaining_budget}**")

# Visualize budget and expenses
if not st.session_state.itinerary.empty:
    st.subheader("Budget vs Expenses")
    budget_data = pd.DataFrame({
        "Type": ["Budget", "Expenses"],
        "Amount": [budget, total_cost]
    })
    fig = px.bar(budget_data, x="Type", y="Amount", text="Amount", color="Type")
    st.plotly_chart(fig)

# Expense distribution by category
if not st.session_state.itinerary.empty:
    st.subheader("Expense Distribution by Category")
    category_data = st.session_state.itinerary.groupby("Category")["Cost"].sum().reset_index()
    fig = px.pie(category_data, values="Cost", names="Category", title="Expenses by Category")
    st.plotly_chart(fig)

# Cumulative expenses over time
if not st.session_state.itinerary.empty:
    st.subheader("Cumulative Expenses Over Time")
    st.session_state.itinerary["Cumulative Cost"] = st.session_state.itinerary["Cost"].cumsum()
    fig = px.line(st.session_state.itinerary, x="Date", y="Cumulative Cost", title="Cumulative Expenses")
    st.plotly_chart(fig)

# Filter itinerary by priority
if not st.session_state.itinerary.empty:
    st.subheader("Filter Itinerary by Priority")
    priority_filter = st.selectbox("Select priority:", ["All", "Low", "Medium", "High"])
    if priority_filter != "All":
        filtered_itinerary = st.session_state.itinerary[st.session_state.itinerary["Priority"] == priority_filter]
        st.dataframe(filtered_itinerary)
    else:
        st.dataframe(st.session_state.itinerary)

# Recommendations based on destination
st.header("📍 Travel Recommendations")
if destination:
    st.write(f"Here are some popular places to visit in **{destination}**:")
    # Example recommendations (can be replaced with a local database)
    recommendations = {
        "Paris": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"],
        "Tokyo": ["Shibuya Crossing", "Tokyo Tower", "Senso-ji Temple"],
        "New York": ["Statue of Liberty", "Central Park", "Times Square"],
    }
    if destination in recommendations:
        for place in recommendations[destination]:
            st.write(f"- {place}")
    else:
        st.write("No specific recommendations available for this destination. Try searching for popular tourist spots!")
else:
    st.write("Enter a destination to get recommendations.")

# Export itinerary as CSV
if not st.session_state.itinerary.empty:
    st.subheader("Export Itinerary")
    csv = st.session_state.itinerary.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download Itinerary as CSV",
        data=csv,
        file_name="travel_itinerary.csv",
        mime="text/csv"
    )

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit")