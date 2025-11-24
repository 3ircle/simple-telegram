import simple_telegram

bot = simple_telegram.bot.Bot('YOUR_API_KEY')

def message_handler(update):
    if update.message and update.message.text == 'hi':
        update.message.reply('hello')

bot.message_handler = message_handler

bot.run(0)
