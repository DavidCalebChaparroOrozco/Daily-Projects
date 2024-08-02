# Importing necessary libraries
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 550
SCREEN_HEIGHT = 600
CARD_SIZE = 125
GRID_SIZE = 4
MARGIN = 10
BACKGROUND_COLOR = (0, 0, 0)
CARD_BACK_COLOR = (150, 150, 150)
CARD_FRONT_COLOR = (255, 255, 255)
FONT_SIZE = 36

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Game by David Caleb")
font = pygame.font.Font(None, FONT_SIZE)

# Load images (using colors for simplicity)
colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
    (0, 255, 255), (255, 0, 255), (255, 165, 0), (128, 0, 128)
]

# Double the colors list to have pairs
color_pairs = colors * 2
random.shuffle(color_pairs)

# Create a grid of cards
cards = []
for row in range(GRID_SIZE):
    card_row = []
    for col in range(GRID_SIZE):
        card = {
            'color': color_pairs.pop(),
            'rect': pygame.Rect(
                MARGIN + col * (CARD_SIZE + MARGIN),
                MARGIN + row * (CARD_SIZE + MARGIN),
                CARD_SIZE,
                CARD_SIZE
            ),
            'flipped': False,
            'matched': False
        }
        card_row.append(card)
    cards.append(card_row)

# Game variables
first_selection = None
second_selection = None
matches_found = 0
total_pairs = GRID_SIZE * GRID_SIZE // 2

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for row in cards:
                for card in row:
                    if card['rect'].collidepoint(pos) and not card['flipped'] and not card['matched']:
                        card['flipped'] = True
                        if not first_selection:
                            first_selection = card
                        elif not second_selection:
                            second_selection = card
                            # Check for a match
                            if first_selection['color'] == second_selection['color']:
                                first_selection['matched'] = True
                                second_selection['matched'] = True
                                matches_found += 1
                                first_selection = None
                                second_selection = None
                            else:
                                pygame.time.wait(500)
                                first_selection['flipped'] = False
                                second_selection['flipped'] = False
                                first_selection = None
                                second_selection = None

    # Drawing
    screen.fill(BACKGROUND_COLOR)
    for row in cards:
        for card in row:
            if card['flipped'] or card['matched']:
                pygame.draw.rect(screen, card['color'], card['rect'])
            else:
                pygame.draw.rect(screen, CARD_BACK_COLOR, card['rect'])
            pygame.draw.rect(screen, BACKGROUND_COLOR, card['rect'], 2)

    if matches_found == total_pairs:
        text = font.render("You Win!", True, (255, 255, 255))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

    pygame.display.flip()

pygame.quit()