# Importing necessary libraries
import time
from plyer import notification
from datetime import datetime, timedelta
import schedule

# Function to send a study notification
def send_study_notification(subject, time_str, tip):
    # Create the notification message
    message = f'Review {subject} at {time_str}. Tip: {tip}'
    
    # Send the notification using plyer
    notification.notify(
        # Title of the notification
        title='Study Reminder',  
        # Message containing the subject and tip
        message=message,  
        # Name of the application
        app_name='Study Notification System',  
        # Duration in seconds for which the notification will be visible
        timeout=10  
    )

# Function to schedule notifications for different subjects
def schedule_notifications():
    # Define subjects, times, and tips for notifications
    notifications = [
        {"subject": "Data Analysis", "time": "17:00", "tip": "Focus on understanding data visualization techniques."},
        {"subject": "Machine Learning", "time": "18:00", "tip": "Remember to practice model evaluation metrics."},
        {"subject": "Statistics", "time": "19:00", "tip": "Review hypothesis testing concepts."},
        {"subject": "Deep Learning", "time": "20:00", "tip": "Don't forget to check out regularization techniques."}
    ]
    
    # Schedule each notification
    for item in notifications:
        # Schedule the notification using the specified time
        schedule.every().day.at(item["time"]).do(send_study_notification, item["subject"], item["time"], item["tip"])

# Main function to run the scheduler
def main():
    # Set up notifications
    schedule_notifications()  
    
    # Inform user that the system is active
    print("Study Notification System is running...")  
    
    while True:
        # Run scheduled tasks
        schedule.run_pending()  
        # Wait for a second before checking again
        time.sleep(1)  

# Entry point of the script
if __name__ == "__main__":
    main()