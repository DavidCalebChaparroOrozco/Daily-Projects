# Import necessary libraries
import os
import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
API_KEY = os.getenv('SOCCER_API')  # Read API key from .env
COMPETITION_CODE = 'CL'  # UEFA Champions League
SEASON = 2023  # Current season for training data
FUTURE_SEASON = 2025  # Future season for prediction (simulated)

# Fetch match data for a competition and season
def fetch_matches(competition_code, season, api_key):
    url = f'https://api.football-data.org/v4/competitions/{competition_code}/matches?season={season}'
    headers = {'X-Auth-Token': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    
    matches = response.json()['matches']
    return matches

# Fetch teams participating in a competition for a specific season
def fetch_teams(competition_code, season, api_key):
    url = f'https://api.football-data.org/v4/competitions/{competition_code}/teams?season={season}'
    headers = {'X-Auth-Token': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        # If the future season data is not available, use the current season's teams as a placeholder
        print(f"Failed to fetch teams for {season}. Using {SEASON} teams as a placeholder.")
        return fetch_teams(competition_code, SEASON, api_key)
    
    teams = response.json()['teams']
    return teams

# Preprocess the match data
def preprocess_matches(matches):
    # Convert to DataFrame
    df_matches = pd.DataFrame(matches)
    
    # Select relevant features
    df_matches = df_matches[['homeTeam', 'awayTeam', 'score']]
    
    # Extract team names from nested dictionaries
    df_matches['homeTeam'] = df_matches['homeTeam'].apply(lambda x: x['name'] if isinstance(x, dict) else None)
    df_matches['awayTeam'] = df_matches['awayTeam'].apply(lambda x: x['name'] if isinstance(x, dict) else None)
    
    # Extract full-time home and away goals
    df_matches['homeGoals'] = df_matches['score'].apply(lambda x: x['fullTime']['home'] if x['fullTime'] else None)
    df_matches['awayGoals'] = df_matches['score'].apply(lambda x: x['fullTime']['away'] if x['fullTime'] else None)
    
    # Drop rows with missing values
    df_matches.dropna(inplace=True)
    
    # Determine match outcome (1: Home Win, 0: Draw, -1: Away Win)
    df_matches['outcome'] = df_matches.apply(lambda row: 1 if row['homeGoals'] > row['awayGoals'] else (0 if row['homeGoals'] == row['awayGoals'] else -1), axis=1)
    
    # Encode team names
    label_encoder = LabelEncoder()
    df_matches['homeTeam'] = label_encoder.fit_transform(df_matches['homeTeam'])
    df_matches['awayTeam'] = label_encoder.transform(df_matches['awayTeam'])
    
    return df_matches[['homeTeam', 'awayTeam', 'outcome']], label_encoder

# Predict match outcome for user-selected teams
def predict_match_outcome(model, label_encoder, team1, team2):
    try:
        # Encode the team names
        team1_encoded = label_encoder.transform([team1])[0]
        team2_encoded = label_encoder.transform([team2])[0]
        
        # Create a DataFrame for the input
        input_data = pd.DataFrame({'homeTeam': [team1_encoded], 'awayTeam': [team2_encoded]})
        
        # Predict probabilities
        probabilities = model.predict_proba(input_data)[0]
        
        # Map probabilities to outcomes
        outcome_mapping = {0: 'Away Win', 1: 'Draw', 2: 'Home Win'}
        results = {outcome_mapping[i]: prob for i, prob in enumerate(probabilities)}
        
        return results
    except ValueError as e:
        print(f"Error: {e}. Please ensure the team names are correct.")
        return None

# Main execution
if __name__ == '__main__':
    try:
        # Fetch match data for UEFA Champions League 2023
        print(f"Fetching match data for UEFA Champions League {SEASON}...")
        matches = fetch_matches(COMPETITION_CODE, SEASON, API_KEY)
        
        # Preprocess the data
        print("Preprocessing match data...")
        df_matches, label_encoder = preprocess_matches(matches)
        
        # Split the data into features (X) and target (y)
        X = df_matches[['homeTeam', 'awayTeam']]
        y = df_matches['outcome']
        
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train a Random Forest Classifier
        print("Training the model...")
        model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')  # Use class weighting to handle imbalance
        model.fit(X_train, y_train)
        
        # Evaluate the model
        print("Evaluating the model...")
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy:.2f}")
        print("Classification Report:")
        print(classification_report(y_test, y_pred))
        
        # Fetch teams for the 2025 season (or use 2023 as a placeholder)
        print(f"Fetching teams for UEFA Champions League {FUTURE_SEASON}...")
        teams = fetch_teams(COMPETITION_CODE, FUTURE_SEASON, API_KEY)
        
        # Display participating teams with numbers
        print("\nParticipating Teams in 2025:")
        team_list = [team['name'] for team in teams]
        for i, team in enumerate(team_list, start=1):
            print(f"{i}. {team}")
        
        # Allow user to select teams for prediction
        while True:
            try:
                home_team_input = input("\nEnter the number or name of the home team: ")
                away_team_input = input("Enter the number or name of the away team: ")
                
                # If the input is a number, map it to the corresponding team name
                if home_team_input.isdigit():
                    home_team = team_list[int(home_team_input) - 1]
                else:
                    home_team = home_team_input
                
                if away_team_input.isdigit():
                    away_team = team_list[int(away_team_input) - 1]
                else:
                    away_team = away_team_input
                
                # Validate team names
                if home_team not in team_list or away_team not in team_list:
                    print("Invalid team name or number. Please try again.")
                    continue
                
                break
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid number or team name.")
        
        # Predict the outcome
        print(f"\nPredicting the outcome for {home_team} (Home) vs {away_team} (Away)...")
        results = predict_match_outcome(model, label_encoder, home_team, away_team)
        
        if results:
            # Display the results
            print("\nPredicted Probabilities:")
            for outcome, prob in results.items():
                print(f"{outcome}: {prob:.2%}")
    
    except Exception as e:
        print(f"An error occurred: {e}")