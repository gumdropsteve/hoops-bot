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


def socials(update, context):
    # return social accounts of Hoops Onchain
    update.message.reply_text("https://x.com/HoopsOnchain/")


# def todays_games(update, context):
#     """
#     Return today's games
#     """


# def pick(update, context):
#     """
#     User can pick which team they think will win a game
#     """


# def scores(update, context):
#     """
#     Check the scores of the live games
#     """


# def points(update, context):
#     """
#     Check how many points a user has scored
#     """


def help(update, context):
    update.message.reply_text(
        """
        Hi there! I'm Hoops Onchain Bot created by Hoops DAO. Please follow these commands:

        /start - to start the conversation
        /content - Information about Madness Onchain Challenge
        /contact - Information about contact of Hoops DAO
        /socials - Hoops Onchain Twitter
        """
        )


# standard telegram bot start
updater = tg.Updater(token, use_context=True)
dispatch = updater.dispatcher

# initialize messages
dispatch.add_handler(tg.CommandHandler('start', start))
dispatch.add_handler(tg.CommandHandler('socials', socials))
dispatch.add_handler(tg.CommandHandler('help', help))

# make connection with telegram bot
updater.start_polling()
updater.idle()


