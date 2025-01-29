import requests
from telegram import Update
from telegram.ext import CallbackContext

def web_search(update: Update, context: CallbackContext):
    query = ' '.join(context.args)
    search_url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(search_url).json()
    summary = response['Abstract']
    update.message.reply_text(f"Here’s a summary of your search: {summary}")
