# Import necessary libraries
import pygame
import random
import sys
from pygame import gfxdraw

# Initialize pygame
pygame.init()
pygame.font.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BOARD_SIZE = 20
TILE_SIZE = 40
TILE_MARGIN = 5
PLAYER_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # Red, Green, Blue, Yellow

class LostLinkGame:
    def __init__(self):
        # Screen setup
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Lost Link - Network Dice Game")
        
        # Fonts
        self.font_large = pygame.font.SysFont('Arial', 32)
        self.font_medium = pygame.font.SysFont('Arial', 24)
        self.font_small = pygame.font.SysFont('Arial', 16)
        
        # Game state
        self.state = "menu"  # menu, playing, game_over
        self.players = []
        self.current_player = 0
        self.dice_value = 1
        self.rolling = False
        self.roll_animation_frames = 0
        self.message = ""
        self.message_timer = 0
        
        # Game board
        self.board = []
        self.generate_board()
        
        # UI positions
        self.board_x = 100
        self.board_y = 200
        self.dice_x = 650
        self.dice_y = 300
        
    # Generate a random game board with different tile types
    def generate_board(self):
        self.board = []
        
        # Tile types: normal, trap, powerup, start, finish
        self.board.append({"type": "start", "special": None})
        
        for i in range(1, BOARD_SIZE - 1):
            rand = random.random()
            if rand < 0.2:  # 20% chance for trap
                self.board.append({"type": "trap", "special": "go_back_3"})
            elif rand < 0.3:  # 10% chance for powerup
                self.board.append({"type": "powerup", "special": "extra_roll"})
            else:
                self.board.append({"type": "normal", "special": None})
                
        self.board.append({"type": "finish", "special": None})
    
    # Add a player to the game
    def add_player(self, name):
        if len(self.players) < 4:
            self.players.append({
                "name": name,
                "position": 0,
                "color": PLAYER_COLORS[len(self.players)],
                "powerups": 0,
                "skip_turn": False
            })
            return True
        return False
    
    # Start the dice rolling animation
    def roll_dice(self):
        if not self.rolling:
            self.rolling = True
            self.roll_animation_frames = 20
            self.dice_value = random.randint(1, 6)
            return True
        return False
    
    # Update the dice rolling animation
    def update_dice_animation(self):
        if self.rolling:
            self.roll_animation_frames -= 1
            if self.roll_animation_frames <= 0:
                self.rolling = False
                self.move_player(self.dice_value)
    
    # Move the current player
    def move_player(self, steps):
        player = self.players[self.current_player]
        player["position"] += steps
        
        # Check if player reached or passed the finish
        if player["position"] >= len(self.board) - 1:
            player["position"] = len(self.board) - 1
            self.message = f"{player['name']} wins!"
            self.message_timer = 180  # 3 seconds at 60 FPS
            self.state = "game_over"
            return
        
        # Handle tile effects
        tile = self.board[player["position"]]
        if tile["type"] == "trap":
            player["position"] = max(0, player["position"] - 3)
            self.message = f"404 Error! {player['name']} was sent back!"
            self.message_timer = 120
        elif tile["type"] == "powerup":
            player["powerups"] += 1
            self.message = f"{player['name']} got a powerup!"
            self.message_timer = 120
        
        # Next player's turn
        self.current_player = (self.current_player + 1) % len(self.players)
    
    # Draw everything on the screen
    def draw(self):
        # Dark background
        self.screen.fill((20, 20, 40))
        
        if self.state == "menu":
            self.draw_menu()
        elif self.state == "playing":
            self.draw_game()
        elif self.state == "game_over":
            self.draw_game()
            self.draw_game_over()
        
        pygame.display.flip()
    
    # Draw the main menu
    def draw_menu(self):
        title = self.font_large.render("LOST LINK by David Caleb", True, (255, 255, 255))
        subtitle = self.font_medium.render("Network Dice Game", True, (200, 200, 255))
        instruction = self.font_small.render("Press SPACE to start with 2 players", True, (180, 180, 180))
        
        self.screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 150))
        self.screen.blit(subtitle, (SCREEN_WIDTH//2 - subtitle.get_width()//2, 200))
        self.screen.blit(instruction, (SCREEN_WIDTH//2 - instruction.get_width()//2, 300))
        
        # Draw sample board preview
        for i, tile in enumerate(self.board[:10]):  # Only show first 10 tiles for preview
            x = 200 + i * (TILE_SIZE + TILE_MARGIN)
            y = 400
            self.draw_tile(x, y, tile["type"], False)
    
    # Draw the game board and UI
    def draw_game(self):
        # Draw title
        title = self.font_medium.render("Network Path", True, (255, 255, 255))
        self.screen.blit(title, (self.board_x, self.board_y - 40))
        
        # Draw board
        visible_tiles = 10  # Number of tiles to show at once
        start_index = max(0, self.players[self.current_player]["position"] - visible_tiles//2)
        start_index = min(start_index, len(self.board) - visible_tiles)
        
        for i in range(visible_tiles):
            if start_index + i >= len(self.board):
                break
                
            x = self.board_x + i * (TILE_SIZE + TILE_MARGIN)
            y = self.board_y
            tile = self.board[start_index + i]
            self.draw_tile(x, y, tile["type"], start_index + i == self.players[self.current_player]["position"])
        
        # Draw players
        for i, player in enumerate(self.players):
            player_x = self.board_x + (player["position"] - start_index) * (TILE_SIZE + TILE_MARGIN)
            player_y = self.board_y - 30 - i * 10  # Offset players vertically
            
            if 0 <= (player["position"] - start_index) < visible_tiles:
                pygame.draw.circle(self.screen, player["color"], 
                                    (player_x + TILE_SIZE//2, player_y), 10)
            
            # Player info
            info_text = self.font_small.render(f"{player['name']}: Pos {player['position']}", True, player["color"])
            self.screen.blit(info_text, (600, 100 + i * 30))
        
        # Draw dice
        self.draw_dice()
        
        # Draw current player indicator
        current_text = self.font_medium.render(
            f"Current: {self.players[self.current_player]['name']}", 
            True, (255, 255, 255))
        self.screen.blit(current_text, (600, 50))
        
        # Draw message
        if self.message_timer > 0:
            msg_text = self.font_small.render(self.message, True, (255, 255, 0))
            self.screen.blit(msg_text, (SCREEN_WIDTH//2 - msg_text.get_width()//2, 150))
            self.message_timer -= 1
    
    # Draw a single tile
    def draw_tile(self, x, y, tile_type, highlight):
        colors = {
            "start": (100, 255, 100),
            "normal": (70, 70, 120),
            "trap": (255, 70, 70),
            "powerup": (255, 200, 0),
            "finish": (100, 255, 255)
        }
        
        # Draw tile base
        color = colors.get(tile_type, (70, 70, 120))
        if highlight:
            color = tuple(min(c + 50, 255) for c in color)  # Lighten color for highlight
        
        pygame.draw.rect(self.screen, color, (x, y, TILE_SIZE, TILE_SIZE))
        pygame.draw.rect(self.screen, (30, 30, 60), (x, y, TILE_SIZE, TILE_SIZE), 2)  # Border
        
        # Draw tile symbol
        symbols = {
            "start": "S",
            "normal": "",
            "trap": "404",
            "powerup": "P",
            "finish": "F"
        }
        
        symbol = symbols.get(tile_type, "")
        if symbol:
            text = self.font_small.render(symbol, True, (255, 255, 255))
            self.screen.blit(text, (x + TILE_SIZE//2 - text.get_width()//2, 
                                    y + TILE_SIZE//2 - text.get_height()//2))
    
    # Draw the dice with current value or animation
    def draw_dice(self):
        # Draw dice background
        pygame.draw.rect(self.screen, (50, 50, 80), (self.dice_x, self.dice_y, 80, 80))
        pygame.draw.rect(self.screen, (100, 100, 130), (self.dice_x, self.dice_y, 80, 80), 3)
        
        if self.rolling:
            # Animated rolling effect
            if self.roll_animation_frames % 3 == 0:  # Change every 3 frames
                value = random.randint(1, 6)
                self.draw_dice_dots(value)
        else:
            # Show actual value
            self.draw_dice_dots(self.dice_value)
        
        # Draw roll instruction if not rolling
        if not self.rolling and self.state == "playing":
            text = self.font_small.render("Press SPACE to roll", True, (200, 200, 255))
            self.screen.blit(text, (self.dice_x - 10, self.dice_y + 90))
    
    # Draw the dots on the dice for a given value
    def draw_dice_dots(self, value):
        dot_color = (240, 240, 240)
        center_x, center_y = self.dice_x + 40, self.dice_y + 40
        
        # Define dot positions for each face
        dot_positions = {
            1: [(center_x, center_y)],
            2: [(center_x - 15, center_y - 15), (center_x + 15, center_y + 15)],
            3: [(center_x - 15, center_y - 15), (center_x, center_y), (center_x + 15, center_y + 15)],
            4: [(center_x - 15, center_y - 15), (center_x + 15, center_y - 15),
                (center_x - 15, center_y + 15), (center_x + 15, center_y + 15)],
            5: [(center_x - 15, center_y - 15), (center_x + 15, center_y - 15), (center_x, center_y),
                (center_x - 15, center_y + 15), (center_x + 15, center_y + 15)],
            6: [(center_x - 15, center_y - 20), (center_x + 15, center_y - 20),
                (center_x - 15, center_y), (center_x + 15, center_y),
                (center_x - 15, center_y + 20), (center_x + 15, center_y + 20)]
        }
        
        for pos in dot_positions.get(value, []):
            pygame.gfxdraw.filled_circle(self.screen, int(pos[0]), int(pos[1]), 6, dot_color)
    
    # Draw the game over overlay
    def draw_game_over(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))
        
        # Game over text
        game_over = self.font_large.render("GAME OVER", True, (255, 100, 100))
        winner = self.font_medium.render(self.message, True, (255, 255, 255))
        restart = self.font_small.render("Press R to restart or Q to quit", True, (200, 200, 255))
        
        self.screen.blit(game_over, (SCREEN_WIDTH//2 - game_over.get_width()//2, 200))
        self.screen.blit(winner, (SCREEN_WIDTH//2 - winner.get_width()//2, 280))
        self.screen.blit(restart, (SCREEN_WIDTH//2 - restart.get_width()//2, 350))
    
    # Handle pygame events
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return False
                
                if self.state == "menu" and event.key == pygame.K_SPACE:
                    # Start game with 2 players
                    self.add_player("Player 1")
                    self.add_player("Player 2")
                    self.state = "playing"
                
                elif self.state == "playing" and event.key == pygame.K_SPACE and not self.rolling:
                    self.roll_dice()
                
                elif self.state == "game_over" and event.key == pygame.K_r:
                    # Reset game
                    self.__init__()
        
        return True
    
    # Update game state
    def update(self):
        if self.state == "playing":
            self.update_dice_animation()
    
    def app(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            clock.tick(60)
        
        pygame.quit()
        sys.exit()

# Start the game
if __name__ == "__main__":
    game = LostLinkGame()
    game.app()