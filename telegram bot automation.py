from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace with your actual Telegram bot token
TOKEN = "YOUR_BOT_TOKEN"

# Define a function to handle incoming messages
def handle_message(update, context):
  text = update.message.text
  # You can add logic here to handle different messages
  # For now, just echo back the message
  context.bot.send_message(chat_id=update.message.chat_id, text=text)

# Define a function to handle the /start command
def handle_start(update, context):
  context.bot.send_message(chat_id=update.message.chat_id, text="Hello! I'm a basic Telegram bot.")

def main():
  updater = Updater(token=TOKEN, use_context=True)
  dispatcher = updater.dispatcher

  # Add handlers for messages and /start command
  dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
  dispatcher.add_handler(CommandHandler("start", handle_start))

  updater.start_polling()
  updater.idle()

if __name__ == "__main__":
  main()
