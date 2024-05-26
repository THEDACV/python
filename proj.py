# Import Rasa libraries
import rasa
from rasa.nlu.model import Interpreter

# Load the pre-trained Rasa model
interpreter = Interpreter.load("models/nlu_model")

# Define a function to process user messages
def handle_message(message):
  # Use Rasa NLU to understand the user intent
  data = interpreter.parse(message)
  intent = data.get("intent", {"name": "None"})["name"]

  # Handle different intents with corresponding responses
  if intent == "greet":
    response = "Hi there! How can I help you today?"
  elif intent == "symptom_inquiry":
    response = "I can't diagnose illnesses, but I can provide general information.  Please describe your symptoms."
  elif intent == "goodbye":
    response = "Have a great day!"
  else:
    response = "Sorry, I don't understand."

  return response

# Main loop to interact with the user
while True:
  user_message = input("You: ")
  bot_response = handle_message(user_message)
  print("Bot:", bot_response)
  if bot_response == "Have a great day!":
    break
