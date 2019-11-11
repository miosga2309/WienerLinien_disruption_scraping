import telegram
from telegram.ext import Updater
import logging
from telegram.ext import (CommandHandler, MessageHandler, Filters)
#from telegram import ReplyKeyboardMarkup
from scraper import get_menu

# create updater
updater = Updater(token='681348503:AAHJ6vxVkvXsrY1sPFkjttqidBxhBgMcMwY',
use_context=True)
dispatcher = updater.dispatcher

# logging module
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Send menu
def sendmenu(update, context):
    menu = get_menu()
    form = []
    form.append("Date: {}".format(menu[0][0]))
    for i in range(0,len(menu)):
        form.append("{}: {}".format(menu[i][1], menu[i][2]))

    context.bot.send_message(chat_id=update.effective_chat.id,
    text=form)

sendmenu_handler = MessageHandler(Filters.text, sendmenu)
dispatcher.add_handler(sendmenu_handler)

# start the Bot
updater.start_polling()
