import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

API_BASE_URL = "flightservice:8080"
BOT_TOKEN = ""
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """
        Welcome
        Commands:
        /get_flights
        /add_flight
    """
    await update.message.reply_text(message)

async def get_flights(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return

async def add_flight(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start",start))
    application.add_handler(CommandHandler("get_flights",get_flights))
    application.add_handler(CommandHandler("add_flight",add_flight))

    application.run_polling()

if __name__ == '__main__':
    main()