# Import necessary libraries
import time

# Recursive countdown timer that prints the remaining time in minutes and seconds.
def recursive_timer(minutes, seconds):
    """    
    Parameters:
    minutes: Number of minutes to count down from.
    seconds: Number of seconds to count down from.
    """
    # Base case: if minutes and seconds are both zero, the timer is complete
    if minutes == 0 and seconds == 0:
        print("Time's up!")
        return

    # Print the current time in a formatted way (MM:SS)
    print(f"{minutes:02}:{seconds:02}")

    # Sleep for one second to simulate the passage of real time
    time.sleep(1)

    # Recursive case: update the seconds and, if necessary, the minutes
    if seconds == 0:
        # If seconds are zero, decrement minutes and reset seconds to 59
        recursive_timer(minutes - 1, 59)
    else:
        # Otherwise, simply decrement the seconds
        recursive_timer(minutes, seconds - 1)

# Example usage: Start a countdown from 2 minutes and 10 seconds
# recursive_timer(2, 10)
recursive_timer(0,10)