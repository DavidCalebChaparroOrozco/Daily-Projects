# Importing necessary libraries
import streamlit as st
import pandas as pd

# Function to load the dataset (using st.cache_data for caching)
@st.cache_data
def load_data():
    # Load the CSV file into a DataFrame
    data = pd.read_csv("data/movies.csv")
    return data

# Streamlit app starts here
def main():
    # Load the movie dataset
    df = load_data()

    # App title
    st.title("Movie Recommendation App by David Caleb")

    # Subtitle
    st.subheader("Find movies based on your preferred genre!")

    # Display dataset info in the app
    st.write("Here is a preview of the movie dataset:")
    st.dataframe(df[['title', 'genres', 'release_date', 'vote_average', 'vote_count']].head(10))

    # Let the user select a genre from the available genres
    genre_list = df['genres'].str.split('|').explode().unique()  # Split genres and get unique values
    selected_genre = st.selectbox("Select a genre to get movie recommendations:", genre_list)

    # Filter the movies by the selected genre
    filtered_movies = df[df['genres'].str.contains(selected_genre, na=False)]

    # Check if there are any movies in the selected genre
    if not filtered_movies.empty:
        st.write(f"Here are some popular {selected_genre} movies we recommend for you:")
        for index, row in filtered_movies.iterrows():
            st.write(f"- {row['title']} ({row['release_date'][:4]}) - Rating: {row['vote_average']}/10 (Votes: {row['vote_count']})")
            st.write(f"  Overview: {row['overview']}")
            st.image(f"https://image.tmdb.org/t/p/w500{row['poster_path']}", width=150)  # Display poster image
    else:
        st.write(f"Sorry, no {selected_genre} movies found in our database.")

    # Sidebar with additional info
    st.sidebar.header("About")
    st.sidebar.write("This is a simple movie recommendation app using Streamlit. You can select your preferred movie genre to get a list of recommended movies. The app uses a dataset containing various details about movies.")

    # Display more information in the sidebar
    st.sidebar.write("Total movies in the dataset:", df.shape[0])
    st.sidebar.write("Top 5 highest-rated movies in the dataset:")
    top_movies = df[['title', 'vote_average']].sort_values(by='vote_average', ascending=False).head(5)
    st.sidebar.table(top_movies)

# Run the app
if __name__ == "__main__":
    main()