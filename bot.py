from functions import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def main():
    updater = Updater("308945204:AAHNGKBhhgl_LH1vlKOJill08lTWSuz2adg")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()

main()

# answer = print_string_uc('тест 001')
# print(answer.lower())