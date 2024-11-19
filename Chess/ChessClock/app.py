# Importing necessary libraries
import time
import threading

class ChessClock:
    def __init__(self, player1_time, player2_time):
        # Initialize the clock with the given time for both players
        self.player1_time = player1_time
        self.player2_time = player2_time
        # Start with player 1
        self.current_player = 1  
        # Flag to control the timer
        self.running = False  
        # Lock for thread safety
        self.lock = threading.Lock()  

    def start_timer(self):
        # Start the timer for the current player
        self.running = True
        while self.running:
            # Wait for one second
            time.sleep(1)  
            with self.lock:
                if self.current_player == 1:
                    # Decrease time for player 1
                    self.player1_time -= 1  
                else:
                    # Decrease time for player 2
                    self.player2_time -= 1  

                # Check if any player's time has run out
                if self.player1_time <= 0 or self.player2_time <= 0:
                    self.running = False

    def switch_player(self):
        # Switch to the other player and restart their timer
        with self.lock:
            self.current_player = 2 if self.current_player == 1 else 1

    def get_times(self):
        # Return the remaining times for both players
        with self.lock:
            return self.player1_time, self.player2_time

def display_time(player1_time, player2_time):
    # Display the remaining time for both players in a formatted way
    print(f"Player 1 Time: {player1_time // 60}:{player1_time % 60:02d} | Player 2 Time: {player2_time // 60}:{player2_time % 60:02d}")

def main():
    # Define the initial time settings (in seconds)
    modes = {
        "5+0": (5 * 60, 0),
        "3+2": (3 * 60, 2),
    }

    print("Select a mode:")
    for mode in modes.keys():
        print(f"- {mode}")

    selected_mode = input("Enter mode (e.g., '5+0'): ")
    
    if selected_mode not in modes:
        print("Invalid mode selected. Exiting.")
        return

    initial_player1_time, increment = modes[selected_mode]
    initial_player2_time = initial_player1_time + increment
    
    clock = ChessClock(initial_player1_time, initial_player2_time)

    timer_thread = threading.Thread(target=clock.start_timer)
    timer_thread.start()

    try:
        while clock.running:
            display_time(*clock.get_times())
            action = input("Press 's' to switch players or 'q' to quit: ").strip().lower()
            
            if action == 's':
                clock.switch_player()
            elif action == 'q':
                clock.running = False
                print("Game ended by user.")
                break

    finally:
        # Ensure the timer thread finishes before exiting
        timer_thread.join()  
        display_time(*clock.get_times())
        print("Final Times:")
        print(f"Player 1: {clock.player1_time // 60}:{clock.player1_time % 60:02d}")
        print(f"Player 2: {clock.player2_time // 60}:{clock.player2_time % 60:02d}")

if __name__ == "__main__":
    main()