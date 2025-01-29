import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import pymongo
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB setup
client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = client["telegram_bot_db"]
users_collection = db["users"]

# OpenAI API setup
openai.api_key = os.getenv("OPENAI_API_KEY")

# Register user
def register_user(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    first_name = update.message.from_user.first_name
    username = update.message.from_user.username

    if not users_collection.find_one({"chat_id": chat_id}):
        users_collection.insert_one({
            "chat_id": chat_id,
            "first_name": first_name,
            "username": username
        })
        update.message.reply_text("You are now registered! Please share your phone number.")
    else:
        update.message.reply_text("You are already registered.")

# Collecting phone number
def collect_phone_number(update: Update, context: CallbackContext):
    phone_number = update.message.contact.phone_number
    chat_id = update.message.chat_id
    users_collection.update_one({"chat_id": chat_id}, {"$set": {"phone_number": phone_number}})
    update.message.reply_text("Phone number saved successfully!")

# Chat with Gemini (AI powered)
def chat_with_gemini(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=150
    )
    update.message.reply_text(response.choices[0].text.strip())

# Main entry point
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am your AI-powered assistant. Type /register to get started.")

def main():
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("register", register_user))
    dp.add_handler(MessageHandler(Filters.contact, collect_phone_number))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat_with_gemini))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
