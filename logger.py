from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def log(update: Update, context: CallbackContext, text):
    file = open('/home/pablo/Documents/Python GB/webinar_9/log_file.csv', 'a')
    file.write(f'{update.effective_user.first_name},{update._effective_user.id}, {text}\n')
    file.close()