# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from random import choice
from collections import defaultdict
import pickle
import os

# GLOBAL TRACKERS
# Results storage for both modes: Human vs AI and AI vs Dealer
results_all = {
    "Human": {"WIN": 0, "LOSE": 0, "TIE": 0},
    "AI": {"WIN": 0, "LOSE": 0, "TIE": 0}
}
results_ai_only = {"AI": {"WIN": 0, "LOSE": 0, "TIE": 0}}

save_file = "blackjack_game_log.txt"

# LOAD POLICY
# Load trained policy from file
def load_policy(filename='blackjack.pkl'):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    else:
        print("Trained policy not found.")
        return {}

# CARD UTILITIES
# Generate a random card with suit and value
def generate_card():
    suits = ['♥', '♦', '♣', '♠']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return choice(suits) + choice(values)

# Calculate the total value of a hand of cards
def evaluate_total(cards):
    total = 0
    ace_count = 0
    for card in cards:
        value = card[1:]
        if value in ['J', 'Q', 'K']:
            total += 10
        elif value == 'A':
            total += 11
            ace_count += 1
        else:
            total += int(value)
    # Adjust for aces if total is over 21
    while total > 21 and ace_count:
        total -= 10
        ace_count -= 1
    return total

# Check if the hand has a usable ace (counted as 11)
def has_usable_ace(cards):
    total = evaluate_total(cards)
    for card in cards:
        if card[1:] == 'A' and total <= 21:
            return True
    return False

# Determine game outcome
def get_result(player_total, dealer_total):
    if player_total > 21:
        return "LOSE"
    elif dealer_total > 21 or player_total > dealer_total:
        return "WIN"
    elif player_total == dealer_total:
        return "TIE"
    else:
        return "LOSE"

# DISPLAY CARDS
# Show cards visually using ASCII-style layout
def show_cards(cards, owner="Player"):
    dic = defaultdict(list)
    for card in cards:
        suit = card[0]
        value = card[1:]
        for i in range(9):
            if i == 0:
                dic[i].append('┌─────────┐')
            elif i == 1:
                dic[i].append(f'│{value:<2}       │')
            elif i == 4:
                dic[i].append(f'│    {suit}    │')
            elif i == 7:
                dic[i].append(f'│       {value:<2}│')
            elif i == 8:
                dic[i].append('└─────────┘')
            else:
                dic[i].append('│         │')
    print(f"{owner}'s cards:")
    for i in range(9):
        for card in dic[i]:
            print(card, end=" ")
        print()

# HUMAN vs AI vs DEALER
def play_blackjack_all_vs_all():
    policy = load_policy()
    playing = True

    while playing:
        # Initial hands
        player_cards = [generate_card(), generate_card()]
        ai_cards = [generate_card(), generate_card()]
        dealer_cards = [generate_card(), generate_card()]

        print("\n🃏 NEW GAME 🃏\n")

        # Human Turn
        player_total = evaluate_total(player_cards)
        print("Your Turn:")
        show_cards(player_cards, owner="You")
        show_cards([dealer_cards[0]], owner="Dealer (Showing)")

        while player_total < 21:
            choice_input = input("Draw another card? (y/n): ").strip().lower()
            if choice_input == 'y':
                player_cards.append(generate_card())
                player_total = evaluate_total(player_cards)
                show_cards(player_cards, owner="You")
                print("Your total:", player_total)
            else:
                break
        if player_total > 21:
            print("You busted!")

        # AI Turn
        print("\nAI Agent Turn:")
        ai_total = evaluate_total(ai_cards)
        show_cards(ai_cards, owner="AI")
        while True:
            psum = max(12, min(evaluate_total(ai_cards), 21))
            dshow = int(dealer_cards[0][1:]) if dealer_cards[0][1:].isdigit() else 10
            state = (psum, dshow, has_usable_ace(ai_cards))
            action = policy.get(state, 1)
            if action == 1:
                print("AI chooses to HIT.")
                ai_cards.append(generate_card())
                ai_total = evaluate_total(ai_cards)
                show_cards(ai_cards, owner="AI")
                print("AI total:", ai_total)
                if ai_total > 21:
                    print("AI busted!")
                    break
            else:
                print("AI chooses to STICK.")
                break

        # Dealer Turn
        print("\nDealer Turn:")
        dealer_total = evaluate_total(dealer_cards)
        show_cards(dealer_cards, owner="Dealer")
        while dealer_total < 17:
            dealer_cards.append(generate_card())
            dealer_total = evaluate_total(dealer_cards)
            show_cards(dealer_cards, owner="Dealer")
            print("Dealer total:", dealer_total)
        if dealer_total > 21:
            print("Dealer busted!")

        # Final Results
        print("\n🎯 FINAL REVEAL 🎯")
        show_cards(player_cards, owner="You")
        print("Your total:", player_total)
        show_cards(ai_cards, owner="AI Agent")
        print("AI total:", ai_total)
        show_cards(dealer_cards, owner="Dealer")
        print("Dealer total:", dealer_total)

        # Get result
        human_result = get_result(player_total, dealer_total)
        ai_result = get_result(ai_total, dealer_total)

        print("\n🏁 RESULTS 🏁")
        print(f"You:     {human_result}")
        print(f"AI:      {ai_result}")
        print("=".center(50, "="))

        # Update stats
        results_all["Human"][human_result] += 1
        results_all["AI"][ai_result] += 1

        # Log game
        with open(save_file, "a", encoding="utf-8") as file:
            file.write("\nNew Game (All vs All)\n")
            file.write(f"You cards   : {player_cards}, total: {player_total}, result: {human_result}\n")
            file.write(f"AI cards    : {ai_cards}, total: {ai_total}, result: {ai_result}\n")
            file.write(f"Dealer cards: {dealer_cards}, total: {dealer_total}\n\n")

        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            playing = False

# AI vs DEALER ONLY
def simulate_ai_vs_dealer(n_games=1000):
    policy = load_policy()

    # Reset stats before simulation
    results_ai_only["AI"] = {"WIN": 0, "TIE": 0, "LOSE": 0}

    for _ in range(n_games):
        ai_cards = [generate_card(), generate_card()]
        dealer_cards = [generate_card(), generate_card()]

        ai_total = evaluate_total(ai_cards)
        while True:
            psum = max(12, min(evaluate_total(ai_cards), 21))
            dshow = int(dealer_cards[0][1:]) if dealer_cards[0][1:].isdigit() else 10
            state = (psum, dshow, has_usable_ace(ai_cards))
            action = policy.get(state, 1)
            if action == 1:
                ai_cards.append(generate_card())
                ai_total = evaluate_total(ai_cards)
                if ai_total > 21:
                    break
            else:
                break

        dealer_total = evaluate_total(dealer_cards)
        while dealer_total < 17:
            dealer_cards.append(generate_card())
            dealer_total = evaluate_total(dealer_cards)

        result = get_result(ai_total, dealer_total)
        results_ai_only["AI"][result] += 1

        # Log results
        with open(save_file, "a", encoding="utf-8") as file:
            file.write("New Game (AI vs Dealer)\n")
            file.write(f"AI cards    : {ai_cards}, total: {ai_total}, result: {result}\n")
            file.write(f"Dealer cards: {dealer_cards}, total: {dealer_total}\n\n")

# PLOTTING STATS

# Bar chart for AI vs Dealer results
def plot_stats(stats, title):
    labels = ['WIN', 'TIE', 'LOSE']
    ai_stats = [stats['AI'][k] for k in labels]
    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(x, ai_stats, width, label='AI', color='darkorange')
    ax.set_ylabel('Number of Games')
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    for i, v in enumerate(ai_stats):
        ax.text(i, v + 0.5, str(v), ha='center')

    plt.tight_layout()
    plt.show()

# Bar chart comparing Human vs AI
def plot_all_vs_all():
    labels = ['WIN', 'TIE', 'LOSE']
    human = [results_all['Human'][k] for k in labels]
    ai = [results_all['AI'][k] for k in labels]
    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(x - width/2, human, width, label='You', color='royalblue')
    ax.bar(x + width/2, ai, width, label='AI', color='darkorange')
    ax.set_ylabel('Number of Games')
    ax.set_title('Game Outcomes: You vs AI')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()

# MAIN MENU
def main_menu():
    while True:
        print("\n🎮 Blackjack Menu 🎮")
        print("1. Play Human vs AI vs Dealer")
        print("2. Simulate 1000 games: AI vs Dealer")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            play_blackjack_all_vs_all()
            plot_all_vs_all()
        elif choice == '2':
            simulate_ai_vs_dealer()
            plot_stats(results_ai_only, "AI vs Dealer - 1000 Game Simulation")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

# START APPLICATION
if __name__ == "__main__":
    main_menu()