# Import necessary libraries
import random
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# Base class for Card Game AI
class CardGameAI:
    # Initialize the cards and score tracking
    def __init__(self):
        self.my_cards = list(range(9))
        self.my_used_cards = []
        self.opponent_used_cards = []
        self.score = 0
        self.opponent_score = 0
        self.possible_odd = {1, 3, 5, 7}
        self.possible_even = {0, 2, 4, 6, 8}

    # Choose an available card based on estimated win rate
    def choose_card(self, back_color):
        available_cards = [c for c in self.my_cards if c not in self.my_used_cards]
        if not available_cards:
            return None

        if back_color == 'red':
            possible_opponent_cards = list(self.possible_odd - set(self.opponent_used_cards))
        else:
            possible_opponent_cards = list(self.possible_even - set(self.opponent_used_cards))

        best_card = available_cards[0]
        best_score = -1

        for my_card in available_cards:
            win_count = 0
            for opp_card in possible_opponent_cards:
                if my_card > opp_card:
                    win_count += 1
            win_rate = win_count / len(possible_opponent_cards) if possible_opponent_cards else 0

            if win_rate > best_score:
                best_score = win_rate
                best_card = my_card

        return best_card

    # Update result and opponent's card guess
    def update_result(self, my_card, back_color, result):
        self.my_used_cards.append(my_card)
        if result == 'win':
            self.score += 1
        elif result == 'lose':
            self.opponent_score += 1

        if back_color == 'red':
            self.opponent_used_cards.append(self.guess_opponent_card('odd', my_card, result))
        else:
            self.opponent_used_cards.append(self.guess_opponent_card('even', my_card, result))

    # Estimate the opponent's card based on result
    def guess_opponent_card(self, parity, my_card, result):
        if parity == 'odd':
            candidates = sorted(self.possible_odd - set(self.opponent_used_cards))
        else:
            candidates = sorted(self.possible_even - set(self.opponent_used_cards))

        if not candidates:
            return my_card

        if result == 'win':
            lower = [c for c in candidates if c < my_card]
            return max(lower) if lower else random.choice(candidates)
        elif result == 'lose':
            higher = [c for c in candidates if c > my_card]
            return min(higher) if higher else random.choice(candidates)
        else:
            return my_card

# Advanced AI class with Machine Learning using KNN
class CardGameAI_ML(CardGameAI):
    def __init__(self, data_file='game_data.csv'):
        super().__init__()
        self.X = []
        self.y = []
        self.knn = KNeighborsClassifier(n_neighbors=3)
        self.data_file = data_file
        self.load_training_data()

    # Encode color for model input (0 for red, 1 for blue)
    def encode_color(self, color):
        return 0 if color == 'red' else 1

    # Load historical game data if available
    def load_training_data(self):
        if os.path.exists(self.data_file):
            df = pd.read_csv(self.data_file)
            self.X = df[['my_card', 'color']].values.tolist()
            self.y = df['result'].tolist()
            if len(self.X) >= 5:
                self.knn.fit(self.X, self.y)
                print(f"[INFO] Loaded {len(self.X)} past training examples.")
        else:
            print("[INFO] No past training data found.")

    # Save new training example after each round
    def save_training_example(self, my_card, back_color, result):
        color_code = self.encode_color(back_color)
        label = {'lose': 0, 'win': 1, 'draw': 2}[result]

        self.X.append([my_card, color_code])
        self.y.append(label)

        df = pd.DataFrame([[my_card, color_code, label]], columns=["my_card", "color", "result"])
        if os.path.exists(self.data_file):
            df.to_csv(self.data_file, mode='a', header=False, index=False)
        else:
            df.to_csv(self.data_file, mode='w', header=True, index=False)

        if len(self.X) >= 5:
            self.knn.fit(self.X, self.y)

    # Choose a card based on ML predictions if enough training data is available
    def choose_card(self, back_color):
        available_cards = [c for c in self.my_cards if c not in self.my_used_cards]
        if not available_cards:
            return None

        color_code = self.encode_color(back_color)

        if len(self.X) < 5:
            return super().choose_card(back_color)

        best_card = available_cards[0]
        best_prob = 0

        for card in available_cards:
            prob = self.knn.predict_proba([[card, color_code]])[0]
            win_prob = prob[1]
            if win_prob > best_prob:
                best_prob = win_prob
                best_card = card

        return best_card

    # Update result and training dataset
    def update_result(self, my_card, back_color, result):
        self.my_used_cards.append(my_card)
        if result == 'win':
            self.score += 1
        elif result == 'lose':
            self.opponent_score += 1
        self.save_training_example(my_card, back_color, result)

        if back_color == 'red':
            self.opponent_used_cards.append(self.guess_opponent_card('odd', my_card, result))
        else:
            self.opponent_used_cards.append(self.guess_opponent_card('even', my_card, result))

# Save match result to CSV file
def save_match_result(winner, file_path="match_results.csv"):
    df = pd.DataFrame([[winner]], columns=["winner"])
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, mode='w', header=True, index=False)

# Plot historical match outcomes
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

# Main game loop
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

    ai = CardGameAI_ML()
    used_player_cards = []
    all_cards = list(range(9))

    for round_num in range(1, 10):
        print(f"\nRound {round_num}")
        print(f"Score: Player {ai.score} - AI {ai.opponent_score}")

        back_color = random.choice(['red', 'blue'])
        print(f"Opponent's card back color: {back_color.upper()} ({'odd' if back_color == 'red' else 'even'})")

        if player_first:
            while True:
                try:
                    player_card = int(input("Choose your card (0-8): "))
                    if player_card in all_cards and player_card not in used_player_cards:
                        break
                    print("Card already used or invalid. Try again.")
                except:
                    print("Please enter a valid number.")
        else:
            ai_card = ai.choose_card(back_color)
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
            ai_card = ai.choose_card(back_color)
            print(f"AI played card: {ai_card}")

        used_player_cards.append(player_card)

        # Determine round result
        if player_card > ai_card:
            result = 'win'
            print("You win this round!")
        elif player_card < ai_card:
            result = 'lose'
            print("AI wins this round!")
        else:
            result = 'draw'
            print("This round is a draw.")

        ai.update_result(ai_card, back_color, result)
        player_first = not player_first

    # Game summary
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

if __name__ == "__main__":
    main()