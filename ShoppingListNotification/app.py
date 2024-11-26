# Import the necessary library for notifications
from plyer import notification

# Function to send a notification with the shopping list
def send_shopping_list_notification(shopping_list):
    # Join the items in the shopping list into a single string
    items = ', '.join(shopping_list)
    
    # Send a notification using plyer's notification module
    notification.notify(
        # Title of the notification
        title='Shopping List Alert',  
        # Message containing the shopping list
        message=f'Your shopping list: {items}',  
        # Name of the application sending the notification
        app_name='Shopping List App by David Caleb', 
        # Duration in seconds for which the notification will be visible
        timeout=10  
    )

# Example shopping list
shopping_list = ['Milk', 'Eggs', 'Bread', 'Butter', 'Fruits', 'Cat Food', 'Tomatoes']

# Call the function to send the notification
send_shopping_list_notification(shopping_list)