import simple_telegram
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv('api_key')

bot = simple_telegram.bot.Bot(api_key)


print(bot._get_update()._update_json)

