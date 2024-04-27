# Importing necessary libraries
import time
from win10toast import ToastNotifier 
import pyjokes
import win10toast
import schedule 
import time 

# # # Test
# # toaster = win10toast.ToastNotifier()
# # toaster.show_toast("python","success ! This is working!", duration=10)
# while 1:
#     notify = ToastNotifier()
#     notify.show_toast("Time to laugh!", pyjokes.get_joke(), duration = 20)
#     time.sleep(1800)

# Initialize toast notifier
noti = ToastNotifier()

# Function definitions for the activities
def show_notification(message, duration=10):
    noti.show_toast(message, duration=duration)

def take_short_break():
    show_notification('Take a short break!')

def joke():
    noti.show_toast("Time to Joke!", pyjokes.get_joke(), duration=10)

# Schedule the activities in the routine
schedule.every().day.at("09:00").do(lambda: show_notification('Time to study English!'))
schedule.every().day.at("10:00").do(lambda: show_notification('Time to work on your Python project!'))
schedule.every().day.at("14:00").do(lambda: show_notification('Take a break and listen to some music!'))
schedule.every().day.at("11:30").do(take_short_break)
schedule.every().day.at("12:00").do(take_short_break)
schedule.every().day.at("15:30").do(take_short_break)
schedule.every().day.at("17:30").do(take_short_break)
schedule.every().day.at("20:00").do(take_short_break)
schedule.every().day.at("23:59").do(lambda: show_notification('Time to go to bed'))
schedule.every().hour.do(lambda: show_notification('Time to drink water!'))
schedule.every().hour.do(lambda: show_notification('You have been working for an hour. Time to take a break', duration=15))
schedule.every(10).to(15).minutes.do(lambda: show_notification('Restart your work'))
schedule.every(2).hours.do(joke)

# Main loop to run the schedule
while True:
    schedule.run_pending()
    time.sleep(1)