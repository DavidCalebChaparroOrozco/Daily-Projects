# Importing necessary libraries
from transformers import pipeline
import numpy as np

# Load a pre-trained BERT model for text classification
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define the possible intents
intents = [
    "book_flight",
    "book_hotel",
    "cancel_reservation",
    "check_weather",
    "tell_joke",
    "find_restaurant",
    "order_food",
    "check_time",
    "set_alarm",
    "play_music",
    "control_lights",
    "navigate_location",
    "set_reminder",
    "currency_conversion",
    "check_news",
    "recipe_lookup",
    "schedule_meeting",
    "translate_text",
    "check_distance",
    "restart_device",
    "call_contact",
    "send_text",
    "toggle_bluetooth",
    "adjust_volume",
    "mute_notifications",
    "find_movies",
    "recommend_book",
    "track_package",
    "find_directions",
    "check_bank_balance",
    "find_doctor"
]

# Function to predict the intent of a user input
def predict_intent(user_input):
    result = classifier(user_input, intents)
    return result["labels"][0]  # Return the most likely intent

# Interactive loop for user input
print("\nWelcome to the Intent Recognition System by David Caleb!")
print("You can type phrases like 'book a flight', 'what's the weather?', or 'play music'.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("Enter a phrase: ").strip().lower()
    if user_input == "exit":
        print("Goodbye!")
        break
    if user_input:
        intent = predict_intent(user_input)
        print(f"Predicted Intent: {intent}\n")
    else:
        print("Please enter a valid phrase.\n")