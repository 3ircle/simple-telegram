import simple_telegram





bot = simple_telegram.bot.Bot("api_key")

def Message_handler(update):
    if update.message.text == 'hi':
        return update.message.reply('hello')
    

bot.message_handler = Message_handler

bot.run()



