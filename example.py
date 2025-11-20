import simple_telegram

bot = simple_telegram.bot.Bot('8272608766:AAHNWSeQ88o6ALppQiY_4U_DwPe9zw28rEo')

def message_handler(update):
    if update.message and update.message.text == 'hi':
        update.message.reply('hello')

bot.message_handler = message_handler

bot.run(0)
