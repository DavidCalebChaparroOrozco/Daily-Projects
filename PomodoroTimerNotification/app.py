# Import necessary libraries
import time
from plyer import notification

class PomodoroTimer:
    # Initialize the Pomodoro Timer with specified durations.
    def __init__(self, work_duration=25, break_duration=5, sessions_to_complete=4):
        """    
        work_duration: Duration of work sessions in minutes
        break_duration: Duration of break sessions in minutes
        sessions_to_complete: Number of Pomodoro sessions to complete
        """

        # convert to seconds
        self.work_duration = work_duration * 60  
        # convert to seconds
        self.break_duration = break_duration * 60  
        self.sessions_to_complete = sessions_to_complete
        self.completed_sessions = 0

    # Send a desktop notification.
    def notify(self, title, message):
        """    
        title: Title of the notification
        message: Message body of the notification
        """
        notification.notify(
            title=title,
            message=message,
            # Notification will disappear after 10 seconds
            timeout=10
        )

    # Start the Pomodoro timer for the specified number of sessions.
    def start_timer(self):
        for session in range(self.sessions_to_complete):
            print(f"Starting session {session + 1}...")
            self.notify("Pomodoro Timer", "Time to work! 🚀")
            # Work session
            time.sleep(self.work_duration)  
            
            self.completed_sessions += 1
            print(f"Session {session + 1} completed!")

            # No break after last session
            if session < self.sessions_to_complete - 1:  
                self.notify("Pomodoro Timer", "Time for a break! 🛋️")
                # Break session
                time.sleep(self.break_duration)  

        print("All sessions completed! Great job! 🎉")

if __name__ == "__main__":
    # Create a Pomodoro timer with default settings
    timer = PomodoroTimer(work_duration=25, break_duration=5, sessions_to_complete=4)
    
    # Start the timer
    timer.start_timer()