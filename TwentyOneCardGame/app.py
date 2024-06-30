# Import necessary libraries
from random import choice
from collections import defaultdict

# Function to display the cards
def show_cards(cards, owner="Player"):
    dic = defaultdict(list)
    
    for card in cards:
        suit = card[0]
        value = card[1:]
        
        for i in range(0, 9):
            if i == 0:
                dic[i].append('┌─────────┐')
            elif i == 1:
                dic[i].append('│{}       │'.format(format(value, ' <2')))
            elif i == 4:
                dic[i].append('│    {}    │'.format(suit))
            elif i == 7:
                dic[i].append('│       {}│'.format(format(value, ' <2')))
            elif i == 8:
                dic[i].append('└─────────┘')
            else:
                dic[i].append('│         │')
                
    print(f"{owner}'s cards:")
    for i in range(0, 9):
        for a in range(0, len(cards)):
            print(dic[i][a], end=" ")
        print("")

# Function to generate a random card
def generate_card():
    suits = ['♥', '♦', '♣', '♠']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card = choice(suits) + choice(values)
    return card

# Function to get the value of a card
def get_value(card, current_total):
    value = card[1:]
    if value in ['J', 'Q', 'K']:
        return 10
    elif value == 'A':
        if current_total + 11 <= 21:
            return 11
        else:
            return 1
    else:
        return int(value)

# Main function for the game
def play_twenty_one():
    playing = True
    while playing:
        player_cards = []
        dealer_cards = []
        player_total = 0
        dealer_total = 0
        continue_playing = True
        
        while continue_playing and player_total < 21:
            card = generate_card()
            player_cards.append(card)
            value = get_value(card, player_total)
            player_total += value
            
            show_cards(player_cards, owner="Player")
            print("Player's current total:", player_total)
            
            if player_total < 21:
                option = input("Do you want to continue playing (y/n)? ").strip().lower()
                if option != 'y':
                    continue_playing = False
            elif player_total == 21:
                print("You win!")
                continue_playing = False
            else:
                print("You exceeded 21. You lose!")
                continue_playing = False
        
        # Dealer's turn
        if player_total <= 21:
            while dealer_total < 17:
                card = generate_card()
                dealer_cards.append(card)
                value = get_value(card, dealer_total)
                dealer_total += value
            
            show_cards(dealer_cards, owner="Dealer")
            print("Dealer's total:", dealer_total)
            
            if dealer_total > 21 or player_total > dealer_total:
                print("You win!")
            elif dealer_total == player_total:
                print("It's a tie!")
            else:
                print("Dealer wins!")
        
        retry_option = input("Do you want to try again (y/n)? ").strip().lower()
        if retry_option != 'y':
            playing = False

# Run the game
play_twenty_one()