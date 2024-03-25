import pygame as pg
from random import randrange

# Initializing pygame
pg.init()

# Definition of window size and size of each cell
WINDOW = 1000
TILE_SIZE = 50

# Definition of the range of random positions for the snake, food, and obstacles
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]

def get_random_position_except_food(food_pos):
    while True:
        pos = [randrange(*RANGE), randrange(*RANGE)]
        if pos != food_pos:
            return pos

# Function to display the main menu
def show_main_menu():
    menu_options = ["Start Game", "Instructions", "Settings", "Quit"]
    selected_option = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pg.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pg.K_RETURN:
                    return selected_option

        screen.fill((0, 0, 0))
        font = pg.font.Font(None, 36)

        for index, option in enumerate(menu_options):
            text_color = (255, 255, 255) if index == selected_option else (128, 128, 128)
            text = font.render(option, True, text_color)
            screen.blit(text, (WINDOW // 2 - text.get_width() // 2, 200 + index * 50))

        pg.display.flip()

# Function to display instructions
# Function to display instructions
def show_instructions():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN:
                return

        screen.fill((0, 0, 0))
        font = pg.font.Font(None, 36)
        
        # Text lines for instructions
        instructions = [
            "Instructions:",
            "Use A, W, S, D keys to control the snake:",
            "- A: Move left",
            "- D: Move right",
            "- W: Move up",
            "- S: Move down",
            "Try to eat the food to grow longer.",
            "Avoid crashing into the walls or yourself!",
            "Press any key to return to the main menu."
        ]

        # Render and display each instruction line
        for index, line in enumerate(instructions):
            text = font.render(line, True, (255, 255, 255))
            screen.blit(text, (50, 50 + index * 40))
        
        pg.display.flip()


# Function to display settings
def show_settings():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN:
                return
        screen.fill((0, 0, 0))
        font = pg.font.Font(None, 36)
        
        # Text lines for settings
        settings = [
            "Settings: Customization Controls",
            "- Press 'C' to change snake color",
            "- Press 'F' to change food color",
            "- Press 'B' to change background color",
            "Press any key to return to the main menu."
        ]

        # Render and display each setting line
        for index, line in enumerate(settings):
            text = font.render(line, True, (255, 255, 255))
            screen.blit(text, (10, 10 + index * 40))
        
        pg.display.flip()


# Screen configuration
screen = pg.display.set_mode([WINDOW] * 2)
pg.display.set_caption("Snake by David Caleb")
clock = pg.time.Clock()

# Main game loop
while True:
    menu_choice = show_main_menu()
    if menu_choice == 0:  # Start Game

        # Initialization of the snake at a random position
        snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
        snake.center = get_random_position()

        # Possible directions of snake movement
        dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

        # Initialization of variables
        length = 1
        segments = [snake.copy()]
        snake_dir = (0, 0)

        # Time setup and waiting time between movements
        time, time_sleep = 0, 110

        # Initial positioning of the food
        food = snake.copy()
        food.center = get_random_position()

        # Initialize obstacles
        num_obstacles = 3
        obstacles = [pg.rect.Rect(get_random_position_except_food(food.center) + [TILE_SIZE, TILE_SIZE]) for _ in range(num_obstacles)]

        # Font initialization for displaying score
        font = pg.font.Font(None, 36)

        # Colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        GRAY = (128, 128, 128)

        # Default settings
        snake_color = GREEN
        food_color = RED
        background_color = BLACK
        obstacle_color = GRAY

        def game_over_screen():
            screen.fill('black')
            game_over_text = font.render("Game Over!", True, (255, 255, 255))
            continue_text = font.render("Play Again?", True, (255, 255, 255))
            screen.blit(game_over_text, (WINDOW // 2 - 100, WINDOW // 2 - 50))
            screen.blit(continue_text, (WINDOW // 2 - 100, WINDOW // 2 - 25))

            yes_button = pg.Rect(WINDOW // 2 - 100, WINDOW // 2 + 20, 80, 40)
            no_button = pg.Rect(WINDOW // 2 + 20, WINDOW // 2 + 20, 80, 40)

            pg.draw.rect(screen, 'green', yes_button)
            pg.draw.rect(screen, 'red', no_button)

            yes_text = font.render("Yes", True, (255, 255, 255))
            no_text = font.render("No", True, (255, 255, 255))
            screen.blit(yes_text, (yes_button.x + 10, yes_button.y + 10))
            screen.blit(no_text, (no_button.x + 10, no_button.y + 10))

            pg.display.flip()

            while True:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        exit()
                    elif event.type == pg.MOUSEBUTTONDOWN:
                        x, y = pg.mouse.get_pos()
                        if yes_button.collidepoint(x, y):
                            # Restart the game
                            global snake, food, length, segments, snake_dir, score
                            snake.center, food.center = get_random_position(), get_random_position()
                            length, snake_dir = 1, (0, 0)
                            segments = [snake.copy()]
                            score = 0
                            return  # Exit the function to continue the game
                        elif no_button.collidepoint(x, y):
                            exit()

        # Main game loop
        score = 0
        while True:
            # Event handling
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.KEYDOWN:
                    # Changing snake direction
                    if event.key == pg.K_a:
                        snake_dir = (-TILE_SIZE, 0)
                        dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
                    if event.key == pg.K_d:
                        snake_dir = (TILE_SIZE, 0)
                        dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}
                    if event.key == pg.K_w and dirs[pg.K_w]:
                        snake_dir = (0, -TILE_SIZE)
                        dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
                    if event.key == pg.K_s:
                        snake_dir = (0, TILE_SIZE)
                        dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
                    # Customization controls
                    if event.key == pg.K_c:
                        snake_color = pg.Color(randrange(256), randrange(256), randrange(256))
                    if event.key == pg.K_f:
                        food_color = pg.Color(randrange(256), randrange(256), randrange(256))
                    if event.key == pg.K_b:
                        background_color = pg.Color(randrange(256), randrange(256), randrange(256))

            screen.fill(background_color)  # Clear the screen

            # Checking borders and if the snake eats itself
            self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
            if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
                game_over_screen()

            # Checking if the snake reaches the food
            if snake.center == food.center:
                food.center = get_random_position()
                length += 1
                score += 1

            # Draw the food
            pg.draw.rect(screen, food_color, food)

            # Draw the obstacles
            for obstacle in obstacles:
                pg.draw.rect(screen, obstacle_color, obstacle)

            # Draw the snake
            [pg.draw.rect(screen, snake_color, segment) for segment in segments]

            # Move the snake
            time_now = pg.time.get_ticks()
            if time_now - time > time_sleep:
                time = time_now
                snake.move_ip(snake_dir)
                segments.append(snake.copy())
                segments = segments[-length:]
            # Check if the snake collides with any obstacle
            if any(snake.colliderect(obstacle) for obstacle in obstacles):
                game_over_screen()

            # Display score
            score_text = font.render("Score: {}".format(score), True, WHITE)
            screen.blit(score_text, (10, 10))

            pg.display.flip()  # Update the screen
            clock.tick(60)  # Limit the frame rate

        # print("Start Game")
    elif menu_choice == 1:  # Instructions
        print("Instructions")
        show_instructions()
    elif menu_choice == 2:  # Settings
        print("Settings")
        show_settings()
    elif menu_choice == 3:  # Quit
        print("Quit")
        exit()
pg.quit()