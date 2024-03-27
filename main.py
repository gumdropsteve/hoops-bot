import telegram.ext as tg
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")


def start(update, context):
    """
    function to start the bot, requires some update and context related to that update
    """
    update.message.reply_text("Sup.")


def help(update, context):
    update.message.reply_text(
        """
        Hi there! I'm Hoops Onchain Bot created by Hoops DAO. Please follow these commands:

        /start - to start the conversation
        /content - Information about Madness Onchain Challenge
        /contact - Information about contact of Hoops DAO
        """
        )


# standard telegram bot start
updater = tg.Updater(token, use_context=True)
dispatch = updater.dispatcher

# initialize messages
dispatch.add_handler(tg.CommandHandler('start', start))
dispatch.add_handler(tg.CommandHandler('help', help))

# make connection with telegram bot
updater.start_polling()
updater.idle()


