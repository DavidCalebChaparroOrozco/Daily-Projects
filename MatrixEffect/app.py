# Import necessary libraries
import curses
import random
import signal
import sys
import time

# A signal handler function to handle interrupts
def signal_handler(sig, frame):
    curses.endwin()
    sys.exit(0)

# Main function
def main(stdscr):
    # Hide the cursor
    curses.curs_set(0)
    
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    # Get the maximum y and x coordinates of the screen
    max_y, max_x = stdscr.getmaxyx()
    
    # Initialize a list to keep track of the current position of characters in each column
    columns = [0] * max_x
    
    # Main loop for the matrix rain effect
    while True:
        # Clear the screen
        stdscr.clear()
        
        # Iterate through each column
        for x in range(max_x):
            # Check if the column is not full and randomly decide whether to add a new character
            if columns[x] < max_y - 1 and random.randint(0, 10) > 5:
                y = columns[x]
                stdscr.addstr(y, x, chr(random.randint(33, 126)), curses.color_pair(1))
                columns[x] += 1
            # If the column is full, wrap the character to the top of the screen
            elif columns[x] >= max_y - 1:
                stdscr.addstr(0, x, chr(random.randint(33, 126)), curses.color_pair(1))
                columns[x] = 0
        
        # Refresh the screen to display the changes
        stdscr.refresh()
        
        # Introduce a small delay to control the speed of the falling characters
        time.sleep(0.05)

# Entry point of the program
if __name__ == "__main__":
    # Set up a signal handler to handle interrupts
    signal.signal(signal.SIGINT, signal_handler)
    curses.wrapper(main)