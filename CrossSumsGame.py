# Import necessary libraries
import pygame
import random
import sys
from typing import List, Tuple, Dict, Set

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

# Colors
GRID_COLOR = (60, 60, 60)  
BACKGROUND_COLOR = (30, 30, 30)  
CELL_COLOR = (45, 45, 45)  
SELECTED_COLOR = (100, 100, 100)  
TEXT_COLOR = (230, 230, 230)  
SUM_COLOR = (255, 85, 85)  

# Button colors
BUTTON_COLOR = (70, 70, 70)
BUTTON_HOVER_COLOR = (90, 90, 90)

# Eliminated cell color
ELIMINATED_COLOR = (80, 80, 80)


# Game settings
class Difficulty:
    # 3x3 grid
    EASY = (3, 3)  
    # 5x5 grid
    NORMAL = (5, 5)  
    # 6x6 grid
    HARD = (6, 6)  

class CrossSumsGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Cross Sums Game by David Caleb")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 24)
        self.small_font = pygame.font.SysFont('Arial', 18)
        self.large_font = pygame.font.SysFont('Arial', 32)
        
        # Game state
        self.difficulty = Difficulty.NORMAL
        self.rows, self.cols = self.difficulty
        self.cell_size = 60
        self.grid_offset_x = 150
        self.grid_offset_y = 150
        # Stores (row, col) of eliminated cells
        self.eliminated_cells = set()  
        self.grid = []
        self.row_sums = []
        self.col_sums = []
        # Cells that should remain (not be eliminated)
        self.solution = set()  
        self.lives = 3
        self.game_over = False
        self.win = False
        
        # UI elements
        self.difficulty_buttons = [
            {"rect": pygame.Rect(50, 50, 100, 40), "text": "Easy", "difficulty": Difficulty.EASY},
            {"rect": pygame.Rect(160, 50, 100, 40), "text": "Normal", "difficulty": Difficulty.NORMAL},
            {"rect": pygame.Rect(270, 50, 100, 40), "text": "Hard", "difficulty": Difficulty.HARD}
        ]
        self.new_game_button = {"rect": pygame.Rect(400, 50, 120, 40), "text": "New Game"}
        self.retry_button = {"rect": pygame.Rect(300, 500, 200, 50), "text": "Try Again"}
        self.quit_button = {"rect": pygame.Rect(300, 570, 200, 50), "text": "Quit"}
        
        self.generate_new_puzzle()
    
    # Generate a new puzzle based on current difficulty
    def generate_new_puzzle(self):
        self.rows, self.cols = self.difficulty
        self.eliminated_cells = set()
        self.lives = 3
        self.game_over = False
        self.win = False
        
        # Generate a grid with random numbers (1-9)
        self.grid = [[random.randint(1, 9) for _ in range(self.cols)] for _ in range(self.rows)]
        
        # Create a valid solution by selecting cells to keep
        self.create_valid_solution()
        
        # Calculate row sums (sum of kept cells in each row)
        self.row_sums = [0] * self.rows
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) in self.solution:
                    self.row_sums[i] += self.grid[i][j]
        
        # Calculate column sums (sum of kept cells in each column)
        self.col_sums = [0] * self.cols
        for j in range(self.cols):
            for i in range(self.rows):
                if (i, j) in self.solution:
                    self.col_sums[j] += self.grid[i][j]
    
    # Create a valid solution by selecting cells to keep
    def create_valid_solution(self):
        self.solution = set()
        
        # Start with some random cells
        for i in range(self.rows):
            for j in range(self.cols):
                # 40% chance to include cell
                if random.random() < 0.4:  
                    self.solution.add((i, j))
        
        # Ensure at least one cell per row and column is kept
        for i in range(self.rows):
            if not any((i, j) in self.solution for j in range(self.cols)):
                j = random.randint(0, self.cols-1)
                self.solution.add((i, j))
        
        for j in range(self.cols):
            if not any((i, j) in self.solution for i in range(self.rows)):
                i = random.randint(0, self.rows-1)
                self.solution.add((i, j))
    
    # Draw the game interface
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        
        # Draw title
        title = self.font.render("Cross Sums Game", True, TEXT_COLOR)
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 10))
        
        # Draw lives
        lives_text = self.font.render(f"Lives: {self.lives}", True, TEXT_COLOR)
        self.screen.blit(lives_text, (600, 30))
        
        # Draw buttons (only if game not over)
        if not self.game_over:
            for button in self.difficulty_buttons:
                color = BUTTON_HOVER_COLOR if button["rect"].collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR
                pygame.draw.rect(self.screen, color, button["rect"])
                pygame.draw.rect(self.screen, GRID_COLOR, button["rect"], 2)
                text = self.small_font.render(button["text"], True, TEXT_COLOR)
                self.screen.blit(text, (
                    button["rect"].x + button["rect"].width // 2 - text.get_width() // 2,
                    button["rect"].y + button["rect"].height // 2 - text.get_height() // 2
                ))
            
            # New game button
            new_game_button = self.new_game_button
            color = BUTTON_HOVER_COLOR if new_game_button["rect"].collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR
            pygame.draw.rect(self.screen, color, new_game_button["rect"])
            pygame.draw.rect(self.screen, GRID_COLOR, new_game_button["rect"], 2)
            text = self.small_font.render(new_game_button["text"], True, TEXT_COLOR)
            self.screen.blit(text, (
                new_game_button["rect"].x + new_game_button["rect"].width // 2 - text.get_width() // 2,
                new_game_button["rect"].y + new_game_button["rect"].height // 2 - text.get_height() // 2
            ))
        
        # Draw the grid
        for i in range(self.rows):
            for j in range(self.cols):
                rect = pygame.Rect(
                    self.grid_offset_x + j * self.cell_size,
                    self.grid_offset_y + i * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                
                # Draw cell background
                if (i, j) in self.eliminated_cells:
                    pygame.draw.rect(self.screen, ELIMINATED_COLOR, rect)
                else:
                    pygame.draw.rect(self.screen, CELL_COLOR, rect)
                
                # Draw cell border
                pygame.draw.rect(self.screen, GRID_COLOR, rect, 2)
                
                # Draw cell value (if not eliminated)
                if (i, j) not in self.eliminated_cells:
                    value = self.grid[i][j]
                    text = self.font.render(str(value), True, TEXT_COLOR)
                    self.screen.blit(text, (
                        rect.x + rect.width // 2 - text.get_width() // 2,
                        rect.y + rect.height // 2 - text.get_height() // 2
                    ))
        
        # Draw row sums (right side)
        for i in range(self.rows):
            text = self.font.render(str(self.row_sums[i]), True, SUM_COLOR)
            self.screen.blit(text, (
                self.grid_offset_x + self.cols * self.cell_size + 20,
                self.grid_offset_y + i * self.cell_size + self.cell_size // 2 - text.get_height() // 2
            ))
        
        # Draw column sums (bottom)
        for j in range(self.cols):
            text = self.font.render(str(self.col_sums[j]), True, SUM_COLOR)
            self.screen.blit(text, (
                self.grid_offset_x + j * self.cell_size + self.cell_size // 2 - text.get_width() // 2,
                self.grid_offset_y + self.rows * self.cell_size + 20
            ))
        
        # Draw instructions
        instructions = [
            "Instructions:",
            "1. Click numbers to eliminate them (gray them out)",
            "2. The remaining numbers in each row must sum to the number on the right",
            "3. The remaining numbers in each column must sum to the number below",
            "4. You have 3 lives - wrong eliminations cost 1 life"
        ]
        for idx, line in enumerate(instructions):
            text = self.small_font.render(line, True, TEXT_COLOR)
            self.screen.blit(text, (50, 550 + idx * 25))
        
        # Game over or win screen
        if self.game_over:
            # Dark overlay
            s = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            s.fill((0, 0, 0, 180))
            self.screen.blit(s, (0, 0))
            
            if self.win:
                message = "Congratulations! You solved the puzzle!"
                color = (0, 255, 0)
            else:
                message = "Game Over! You ran out of lives!"
                color = (255, 0, 0)
            
            text = self.large_font.render(message, True, color)
            self.screen.blit(text, (
                SCREEN_WIDTH // 2 - text.get_width() // 2,
                SCREEN_HEIGHT // 2 - 100
            ))
            
            # Draw retry button
            retry_color = BUTTON_HOVER_COLOR if self.retry_button["rect"].collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR
            pygame.draw.rect(self.screen, retry_color, self.retry_button["rect"])
            pygame.draw.rect(self.screen, GRID_COLOR, self.retry_button["rect"], 2)
            retry_text = self.font.render(self.retry_button["text"], True, TEXT_COLOR)
            self.screen.blit(retry_text, (
                self.retry_button["rect"].x + self.retry_button["rect"].width // 2 - retry_text.get_width() // 2,
                self.retry_button["rect"].y + self.retry_button["rect"].height // 2 - retry_text.get_height() // 2
            ))
            
            # Draw quit button
            quit_color = BUTTON_HOVER_COLOR if self.quit_button["rect"].collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR
            pygame.draw.rect(self.screen, quit_color, self.quit_button["rect"])
            pygame.draw.rect(self.screen, GRID_COLOR, self.quit_button["rect"], 2)
            quit_text = self.font.render(self.quit_button["text"], True, TEXT_COLOR)
            self.screen.blit(quit_text, (
                self.quit_button["rect"].x + self.quit_button["rect"].width // 2 - quit_text.get_width() // 2,
                self.quit_button["rect"].y + self.quit_button["rect"].height // 2 - quit_text.get_height() // 2
            ))
        
        pygame.display.flip()
    
    # Check if current eliminations match the solution
    def check_solution(self):
        # The solution is correct if all eliminated cells are NOT in the solution set
        # and all non-eliminated cells ARE in the solution set
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) in self.eliminated_cells and (i, j) in self.solution:
                    return False
                if (i, j) not in self.eliminated_cells and (i, j) not in self.solution:
                    return False
        return True
    
    # Check if the player has won
    def check_win(self):
        if self.check_solution():
            self.win = True
            self.game_over = True
        return self.win
    
    # Handle mouse click
    def handle_click(self, pos):
        if self.game_over:
            if self.retry_button["rect"].collidepoint(pos):
                self.generate_new_puzzle()
                return
            elif self.quit_button["rect"].collidepoint(pos):
                pygame.quit()
                sys.exit()
        
        # Check difficulty buttons
        for button in self.difficulty_buttons:
            if button["rect"].collidepoint(pos):
                self.difficulty = button["difficulty"]
                self.generate_new_puzzle()
                return
        
        # Check new game button
        if self.new_game_button["rect"].collidepoint(pos):
            self.generate_new_puzzle()
            return
        
        # Check grid cells (only if game is active)
        if not self.game_over:
            for i in range(self.rows):
                for j in range(self.cols):
                    cell_rect = pygame.Rect(
                        self.grid_offset_x + j * self.cell_size,
                        self.grid_offset_y + i * self.cell_size,
                        self.cell_size,
                        self.cell_size
                    )
                    if cell_rect.collidepoint(pos):
                        if (i, j) in self.eliminated_cells:
                            self.eliminated_cells.remove((i, j))  # Undo elimination
                        else:
                            self.eliminated_cells.add((i, j))
                            # Check if this was a wrong elimination
                            if (i, j) in self.solution:
                                self.lives -= 1
                                if self.lives <= 0:
                                    self.game_over = True
                        
                        # Check for win after each change
                        self.check_win()
                        return
    
    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Left mouse button
                    if event.button == 1:  
                        self.handle_click(event.pos)
            
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = CrossSumsGame()
    game.main()