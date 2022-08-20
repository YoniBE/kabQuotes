import random
import telegram
import QuoteData
from credentials import bot_user_name, bot_token

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

def send_msg():
    data = QuoteData.load_json_data("t.json")
    quote_number = len(data["quote"])
    random_index = random.randint(0, quote_number)
    msg = data["quote"][random_index] + "\n" + "<b><i>" + data["ref"][random_index] + "</i></b>"
    bot.send_message(chat_id="-1001611107723", text=msg, parse_mode=telegram.ParseMode.HTML)


send_msg()