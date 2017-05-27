def print_string_uc(input_string: str):
    input_string = input_string.upper()
    return input_string

def show_error(bot, update, error):
    print(error)

def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)

def greet_user(bot, update):
    print('Вызван /start')
    print(update)
    bot.sendMessage(update.message.chat_id, text=print_string_uc('Давай общаться!'))