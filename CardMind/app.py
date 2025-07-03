# Importing required libraries
import random
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

# Advanced AI class using Random Forest for card prediction
class AdvancedCardGameAI:
    def __init__(self, data_file='advanced_game_data.csv'):
        # Initialize game variables
        self.my_cards = list(range(9))
        self.my_used_cards = []
        self.opponent_used_cards = []
        self.score = 0
        self.opponent_score = 0
        self.data_file = data_file

        # Initialize ML data structures
        self.X = []
        self.y = []
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.load_training_data()

    # Encode card back color: 0 for red, 1 for blue
    def encode_color(self, color):
        return 0 if color == 'red' else 1

    # Load historical training data if available
    def load_training_data(self):
        if os.path.exists(self.data_file):
            df = pd.read_csv(self.data_file)
            self.X = df[['my_card', 'back_color', 'round_number']].values.tolist()
            self.y = df['result'].tolist()
            if len(self.X) >= 10:
                self.model.fit(self.X, self.y)

    # Save result of a game round for model training
    def save_training_example(self, my_card, back_color, round_number, result):
        color_code = self.encode_color(back_color)
        label = {'lose': 0, 'win': 1, 'draw': 2}[result]
        new_data = pd.DataFrame([[my_card, color_code, round_number, label]],
                                columns=['my_card', 'back_color', 'round_number', 'result'])
        if os.path.exists(self.data_file):
            new_data.to_csv(self.data_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(self.data_file, mode='w', header=True, index=False)

        # Append data and refit model if sufficient samples
        self.X.append([my_card, color_code, round_number])
        self.y.append(label)
        if len(self.X) >= 10:
            self.model.fit(self.X, self.y)

    # Choose best card based on model prediction or fallback logic
    def choose_card(self, back_color, round_number):
        available_cards = [c for c in self.my_cards if c not in self.my_used_cards]
        if not available_cards:
            return None

        color_code = self.encode_color(back_color)

        if len(self.X) < 10:
            # Fallback: play the highest available card
            return sorted(available_cards)[-1]

        best_card = available_cards[0]
        best_prob = -1

        for card in available_cards:
            prob = self.model.predict_proba([[card, color_code, round_number]])[0]
            win_prob = prob[1]  # Probability of winning
            if win_prob > best_prob:
                best_prob = win_prob
                best_card = card

        return best_card

    # Update the used cards and model training data
    def update_result(self, my_card, back_color, round_number, result):
        self.my_used_cards.append(my_card)
        if result == 'win':
            self.opponent_score += 1  # AI wins
        elif result == 'lose':
            self.score += 1  # Player wins

        self.save_training_example(my_card, back_color, round_number, result)

# Save the final result of the match to CSV
def save_match_result(winner, file_path="match_results.csv"):
    df = pd.DataFrame([[winner]], columns=["winner"])
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, mode='w', header=True, index=False)

# Display a bar chart of historical match results
def plot_match_history(file_path="match_results.csv"):
    if not os.path.exists(file_path):
        print("No match history to display.")
        return

    df = pd.read_csv(file_path)
    counts = df["winner"].value_counts()
    labels = ['Player', 'AI', 'Draw']
    values = [counts.get('player', 0), counts.get('ai', 0), counts.get('draw', 0)]

    plt.figure(figsize=(6, 4))
    bars = plt.bar(labels, values, color=['green', 'red', 'gray'])
    plt.title("Historical Match Outcomes")
    plt.ylabel("Number of Wins")

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.3,
                    '%d' % int(height), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

# Main game loop for player vs AI interaction
def main():
    print(" Strategic Card Game (0-8) ".center(50, "="))
    print("Who should start first?")
    print("1. You start")
    print("2. AI starts")
    print("3. Random")

    while True:
        choice = input("Enter your choice (1-3): ")
        if choice in ['1', '2', '3']:
            break
        print("Invalid choice, try again.")

    if choice == '1':
        player_first = True
    elif choice == '2':
        player_first = False
    else:
        player_first = random.choice([True, False])

    print(f"\nGame starts! {'You' if player_first else 'AI'} will begin.\n")

    ai = AdvancedCardGameAI()
    used_player_cards = []
    all_cards = list(range(9))

    for round_num in range(1, 10):
        print(f"\nRound {round_num}")
        print(f"Score: Player {ai.score} - AI {ai.opponent_score}")

        back_color = random.choice(['red', 'blue'])
        print(f"Opponent's card back color: {back_color.upper()} ({'odd' if back_color == 'red' else 'even'})")

        if player_first:
            # Player selects a card first
            while True:
                try:
                    player_card = int(input("Choose your card (0-8): "))
                    if player_card in all_cards and player_card not in used_player_cards:
                        break
                    print("Card already used or invalid. Try again.")
                except:
                    print("Please enter a valid number.")
        else:
            # AI selects card first
            ai_card = ai.choose_card(back_color, round_num)
            print("AI has chosen its card. Your turn.")
            while True:
                try:
                    player_card = int(input("Choose your card (0-8): "))
                    if player_card in all_cards and player_card not in used_player_cards:
                        break
                    print("Card already used or invalid. Try again.")
                except:
                    print("Please enter a valid number.")

        if not player_first:
            print(f"AI played card: {ai_card}")
        else:
            ai_card = ai.choose_card(back_color, round_num)
            print(f"AI played card: {ai_card}")

        used_player_cards.append(player_card)

        # Determine round outcome
        if player_card > ai_card:
            result = 'lose'
            print("You win this round!")
        elif player_card < ai_card:
            result = 'win'
            print("AI wins this round!")
        else:
            result = 'draw'
            print("This round is a draw.")

        ai.update_result(ai_card, back_color, round_num, result)
        player_first = not player_first  # Alternate turn

    # End game summary
    print(" Game Over ".center(50, "="))
    print(f"Final Score: Player {ai.score} - AI {ai.opponent_score}")

    if ai.score > ai.opponent_score:
        print("Congratulations! You win!")
        save_match_result("player")
    elif ai.score < ai.opponent_score:
        print("AI wins the game!")
        save_match_result("ai")
    else:
        print("It's a tie!")
        save_match_result("draw")

    plot_match_history()

# Entry point
if __name__ == "__main__":
    main()