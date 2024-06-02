# Import necessary libraries
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
DARK_GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Screen configuration
TILE_SIZE = 30
MARGIN = 2

# Screen dimensions
def set_dimensions(rows, cols):
    width = cols * TILE_SIZE + (cols + 1) * MARGIN
    height = rows * TILE_SIZE + (rows + 1) * MARGIN
    return width, height

# Initialize font
font = pygame.font.SysFont('Arial', 20)

# Board class
class Board:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.flags = [[False for _ in range(cols)] for _ in range(rows)]
        self.game_over = False
        self.game_won = False
        self.generate_board()

    def generate_board(self):
        # Place mines
        mine_positions = random.sample(range(self.rows * self.cols), self.mines)
        for pos in mine_positions:
            row, col = divmod(pos, self.cols)
            self.board[row][col] = -1

        # Calculate numbers
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == -1:
                    continue
                self.board[row][col] = sum(self.board[r][c] == -1 for r in range(row-1, row+2) for c in range(col-1, col+2) if 0 <= r < self.rows and 0 <= c < self.cols)

    def reveal(self, row, col):
        # Check if the cell is already revealed or flagged
        if self.revealed[row][col] or self.flags[row][col]:
            return
        # Reveal the cell
        self.revealed[row][col] = True
        # If the cell contains a mine, set the game over flag
        if self.board[row][col] == -1:
            self.game_over = True
        # If the cell is empty (0), reveal all surrounding cells recursively
        elif self.board[row][col] == 0:
            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    if 0 <= r < self.rows and 0 <= c < self.cols:
                        self.reveal(r, c)
        # Check if the player has won the game
        self.check_win()

    def toggle_flag(self, row, col):
        # Toggle the flag on the cell if it is not already revealed
        if not self.revealed[row][col]:
            self.flags[row][col] = not self.flags[row][col]
        # Check if the player has won the game
        self.check_win()

    def check_win(self):
        # Iterate through the board to check if all non-mine cells are revealed
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.revealed[row][col] and self.board[row][col] != -1:
                    return
        # If all non-mine cells are revealed, set the game won flag
        self.game_won = True

    def draw(self, screen):
        # Draw each cell on the board
        for row in range(self.rows):
            for col in range(self.cols):
                # Set the color based on whether the cell is revealed
                color = DARK_GRAY if self.revealed[row][col] else GRAY
                # Draw the cell
                pygame.draw.rect(screen, color, [(MARGIN + TILE_SIZE) * col + MARGIN, (MARGIN + TILE_SIZE) * row + MARGIN, TILE_SIZE, TILE_SIZE])
                if self.revealed[row][col]:
                    # Draw a mine if the cell contains a mine
                    if self.board[row][col] == -1:
                        pygame.draw.circle(screen, BLACK, [(MARGIN + TILE_SIZE) * col + MARGIN + TILE_SIZE // 2, (MARGIN + TILE_SIZE) * row + MARGIN + TILE_SIZE // 2], TILE_SIZE // 3)
                    # Draw the number of surrounding mines if the cell contains a number
                    elif self.board[row][col] > 0:
                        text = font.render(str(self.board[row][col]), True, BLACK)
                        screen.blit(text, [(MARGIN + TILE_SIZE) * col + MARGIN + 10, (MARGIN + TILE_SIZE) * row + MARGIN + 5])
                elif self.flags[row][col]:
                    # Draw a flag if the cell is flagged
                    pygame.draw.circle(screen, RED, [(MARGIN + TILE_SIZE) * col + MARGIN + TILE_SIZE // 2, (MARGIN + TILE_SIZE) * row + MARGIN + TILE_SIZE // 2], TILE_SIZE // 3)

        # Draw the restart button if the game is over or won
        if self.game_over or self.game_won:
            pygame.draw.rect(screen, WHITE, [(screen.get_width() // 2) - 50, (screen.get_height() // 2) - 25, 100, 50])
            text = font.render('Restart', True, BLACK)
            screen.blit(text, [(screen.get_width() // 2) - 35, (screen.get_height() // 2) - 15])


def choose_difficulty():
    print("Choose difficulty:")
    print("1. Easy (10x10, 10 mines)")
    print("2. Intermediate (16x16, 40 mines)")
    print("3. Hard (16x30, 99 mines)")
    print("4. Custom")
    choice = input("Select 1, 2, 3, or 4: ")

    if choice == '1':
        return 10, 10, 10
    elif choice == '2':
        return 16, 16, 40
    elif choice == '3':
        return 16, 30, 99
    elif choice == '4':
        rows = int(input("Number of rows: "))
        cols = int(input("Number of columns: "))
        mines = int(input("Number of mines: "))
        return rows, cols, mines
    else:
        print("Invalid option. Defaulting to easy.")
        return 10, 10, 10

def main():
    rows, cols, mines = choose_difficulty()
    width, height = set_dimensions(rows, cols)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Minesweeper')

    board = Board(rows, cols, mines)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = x // (TILE_SIZE + MARGIN)
                row = y // (TILE_SIZE + MARGIN)
                if board.game_over or board.game_won:
                    if (screen.get_width() // 2) - 50 <= x <= (screen.get_width() // 2) + 50 and (screen.get_height() // 2) - 25 <= y <= (screen.get_height() // 2) + 25:
                        # Restart the game
                        main()  
                else:
                    # Left click
                    if event.button == 1:  
                        board.reveal(row, col)
                    # Right click
                    elif event.button == 3:  
                        board.toggle_flag(row, col)

        screen.fill(WHITE)
        board.draw(screen)
        pygame.display.flip()

        if board.game_over:
            print("Game Over!")
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

        clock.tick(30)

if __name__ == "__main__":
    main()
