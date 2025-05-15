# Import necessary libraries
import time
import random
import win10toast
from datetime import datetime

# A class to deliver motivational Kobe Bryant quotes (Mamba Mentality) 
# as Windows notifications at random, unexpected intervals.
class MambaSurpriseMotivator:
    # Initialize with random interval range in minutes.
    def __init__(self, min_wait=30, max_wait=240):
        """    
        Args:
            min_wait: Minimum wait time in minutes (default 30)
            max_wait: Maximum wait time in minutes (default 240/4 hours)
        """
        # Convert to seconds
        self.min_wait = min_wait * 60  
        self.max_wait = max_wait * 60
        self.toaster = win10toast.ToastNotifier()
        self.quotes = [
            "The moment you give up is the moment you let someone else win.",
            "Hard work outweighs talent — every time.",
            "I can't relate to lazy people. We don't speak the same language.",
            "If you're afraid to fail, then you're probably going to fail.",
            "Everything negative - pressure, challenges - is all an opportunity for me to rise.",
            "The most important thing is to try and inspire people so that they can be great in whatever they want to do.",
            "Once you know what failure feels like, determination chases success.",
            "I don't want to be the next Michael Jordan, I only want to be Kobe Bryant.",
            "Use your success, wealth and influence to put them in the best position to realize their own dreams and find their true purpose.",
            "The topic of leadership is a touchy one. A lot of leaders fail because they don't have the bravery to touch that nerve or strike that chord.",
            "I create my own path. It was straight and narrow. I looked at it this way: you were either in my way, or out of it.",
            "I have self-doubt. I have insecurity. I have fear of failure... We all have self-doubt. You don't deny it, but you also don't capitulate to it. You embrace it.",
            "The beauty in being blessed with talent is rising above doubters to create a beautiful moment.",
            "If you do not believe in yourself no one will do it for you.",
            "Great things come from hard work and perseverance. No excuses.",
            "Doubters don't get to write your story. You do.",
            "The mindset isn't about seeking a result—it's more about the process of getting to that result."
        ]
        
        # Track when notifications are sent to avoid clustering
        self.last_notification_time = None
    
    # Generate a random interval between notifications
    def get_random_interval(self):
        return random.randint(self.min_wait, self.max_wait)
    
    # Return a random Kobe Bryant quote from the collection
    def get_random_quote(self):
        return random.choice(self.quotes)
    
    # Check if current time is appropriate for notification (avoid late night)
    def is_appropriate_time(self):
        hour = datetime.now().hour
        # Only between 8AM and 10PM
        return 8 <= hour < 22  
    
    # Display a Windows notification with a random Mamba Mentality quote
    def show_notification(self):
        if not self.is_appropriate_time():
            return False
            
        quote = self.get_random_quote()
        self.toaster.show_toast(
            # Title
            "Mamba Mentality 💜💛",  
            # Message
            quote,                   
            # Notification stays for 10 seconds
            duration=10,             
            threaded=True
        )
        self.last_notification_time = datetime.now()
        return True
    
    # Run the motivator with random, unexpected notifications
    def run(self):
        print("Mamba Surprise Motivator is running. Press Ctrl+C to stop.")
        print(f"Notifications will come randomly between {self.min_wait//60}-{self.max_wait//60} minutes.")
        
        try:
            while True:
                # Wait random time before next notification
                wait_time = self.get_random_interval()
                print(f"\nNext notification in ~{wait_time//60} minutes...")
                time.sleep(wait_time)
                
                # Try to show notification (might skip if inappropriate time)
                if self.show_notification():
                    print(f"Notification sent at {datetime.now().strftime('%H:%M')}")
                else:
                    print("Skipped notification (outside preferred hours)")
                
        except KeyboardInterrupt:
            print("\nMamba Surprise Motivator stopped. Keep that Mamba Mentality going!")

if __name__ == "__main__":
    # Create instance with random intervals between 30 min and 4 hours
    # Adjust these values to make notifications more or less frequent
    motivator = MambaSurpriseMotivator(min_wait=30, max_wait=240)
    
    # Start the surprise motivator
    motivator.run()