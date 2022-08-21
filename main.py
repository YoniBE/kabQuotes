import random
import schedule
import telegram
import QuoteData
import time
from credentials import bot_chat_id, bot_token, bot_test_chat_id

TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)
chat_id = bot_chat_id
test_chat_id = bot_test_chat_id

def send_msg():
    data = QuoteData.load_json_data("database.json")
    quote_number = len(data["quote"])
    random_index = random.randint(0, quote_number)
    msg = data["quote"][random_index] + "\n" + "<b><i>" + data["ref"][random_index] + "</i></b>"
    bot.send_message(chat_id=chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)
    #bot.send_message(chat_id=test_chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)


schedule.every().day.at("06:00").do(send_msg)
schedule.every().day.at("09:00").do(send_msg)
schedule.every().day.at("14:00").do(send_msg)
schedule.every().day.at("17:00").do(send_msg)

# ----- For Debugging -------#

#schedule.every(10).seconds.do(send_msg)

# ----------------------------#

while True:
    schedule.run_pending()
    time.sleep(1)
