from telegram import Update
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackContext
from bot_commands import *

updater = Updater('5652757204:AAFwnJeMlMTrW-Ommj8Aawd7YYP2t0Uk240')

updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('sub', sub_command))
updater.dispatcher.add_handler(CommandHandler('mul', mul_command))
updater.dispatcher.add_handler(CommandHandler('div', div_command))

updater.dispatcher.add_handler(MessageHandler(Filters.text, analize_command))

updater.start_polling()
updater.idle()
