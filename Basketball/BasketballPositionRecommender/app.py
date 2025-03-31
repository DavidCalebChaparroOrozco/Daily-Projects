# Collects player information from user input.
def get_player_info():
    print("Welcome to the Basketball Position Recommender!")
    print("Please enter the following information about the player:\n")
    
    while True:
        try:
            height = float(input("Height (in cm): "))
            if height < 150 or height > 250:
                print("Please enter a realistic height between 150cm and 250cm.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for height.")
    
    while True:
        try:
            weight = float(input("Weight (in kg): "))
            if weight < 40 or weight > 150:
                print("Please enter a realistic weight between 40kg and 150kg.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for weight.")
    
    print("\nPlease rate the player's skills on a scale from 1 (poor) to 10 (excellent):")
    skills = {
        'ball_handling': get_skill_rating("Ball handling/dribbling"),
        'shooting': get_skill_rating("Shooting (mid-range and 3-point)"),
        'passing': get_skill_rating("Passing and court vision"),
        'rebounding': get_skill_rating("Rebounding"),
        'defense': get_skill_rating("Defense"),
        'post_play': get_skill_rating("Post play and inside scoring"),
        'athleticism': get_skill_rating("Athleticism and speed")
    }
    
    return {
        'height': height,
        'weight': weight,
        'skills': skills
    }

# Gets a valid skill rating from user input.
def get_skill_rating(skill_name):
    while True:
        try:
            rating = int(input(f"{skill_name}: "))
            if 1 <= rating <= 10:
                return rating
            print("Please enter a rating between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")

# Calculates suitability scores for each basketball position based on player data.
def calculate_position_scores(player_data):
    height = player_data['height']
    weight = player_data['weight']
    skills = player_data['skills']
    
    # Position weights for different attributes
    position_weights = {
        'PG': {  # Point Guard
            'height': 0.1,
            'weight': 0.05,
            'ball_handling': 0.25,
            'shooting': 0.2,
            'passing': 0.25,
            'rebounding': 0.05,
            'defense': 0.1,
            'post_play': 0.0,
            'athleticism': 0.15
        },
        'SG': {  # Shooting Guard
            'height': 0.15,
            'weight': 0.1,
            'ball_handling': 0.2,
            'shooting': 0.3,
            'passing': 0.1,
            'rebounding': 0.05,
            'defense': 0.15,
            'post_play': 0.0,
            'athleticism': 0.15
        },
        'SF': {  # Small Forward
            'height': 0.2,
            'weight': 0.15,
            'ball_handling': 0.15,
            'shooting': 0.2,
            'passing': 0.1,
            'rebounding': 0.1,
            'defense': 0.15,
            'post_play': 0.05,
            'athleticism': 0.2
        },
        'PF': {  # Power Forward
            'height': 0.25,
            'weight': 0.2,
            'ball_handling': 0.05,
            'shooting': 0.1,
            'passing': 0.05,
            'rebounding': 0.25,
            'defense': 0.15,
            'post_play': 0.25,
            'athleticism': 0.1
        },
        'C': {  # Center
            'height': 0.3,
            'weight': 0.25,
            'ball_handling': 0.0,
            'shooting': 0.05,
            'passing': 0.05,
            'rebounding': 0.3,
            'defense': 0.2,
            'post_play': 0.3,
            'athleticism': 0.05
        }
    }
    
    # Normalize height and weight to 1-10 scale
    normalized_height = (height - 150) / (250 - 150) * 9 + 1
    normalized_weight = (weight - 40) / (150 - 40) * 9 + 1
    
    # Calculate scores for each position
    position_scores = {}
    
    for position, weights in position_weights.items():
        score = 0
        # Add height and weight contributions
        score += weights['height'] * normalized_height
        score += weights['weight'] * normalized_weight
        
        # Add skill contributions
        for skill, value in skills.items():
            score += weights[skill] * value
        
        position_scores[position] = score
    
    return position_scores

# Determines the best position based on calculated scores.
def recommend_position(position_scores):
    best_position = max(position_scores, key=position_scores.get)
    return best_position, position_scores

# Displays the recommendation and detailed scores to the user.
def display_results(recommendation, scores):
    print("\nPosition Recommendation")
    print(f"Recommended position: {get_position_full_name(recommendation)}")
    
    print("\nDetailed Position Scores")
    for position, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        print(f"{get_position_full_name(position)}: {score:.2f}")

# Converts position abbreviation to full name.
def get_position_full_name(abbreviation):
    position_names = {
        'PG': 'Point Guard',
        'SG': 'Shooting Guard',
        'SF': 'Small Forward',
        'PF': 'Power Forward',
        'C': 'Center'
    }
    return position_names.get(abbreviation, abbreviation)

def main():
    # Get player information
    player_data = get_player_info()
    
    # Calculate position scores
    position_scores = calculate_position_scores(player_data)
    
    # Determine recommendation
    recommendation, all_scores = recommend_position(position_scores)
    
    # Display results
    display_results(recommendation, all_scores)

if __name__ == "__main__":
    main()