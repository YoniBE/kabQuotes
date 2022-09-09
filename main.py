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
    update_data()
    data = QuoteData.load_json_data("database.json")
    quote_number = len(data["quote"])
    random_index = random.sample(list(range(quote_number)), 1)[0]
    msg = data["quote"][random_index] + "\n" + "<b><i>" + data["ref"][random_index] + "</i></b>"
    bot.send_message(chat_id=chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)
    #bot.send_message(chat_id=test_chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)

def update_data():
    quote_obj = QuoteData.InitData("EinOdMilvado_20.csv")
    QuoteData.SaveData(quote_obj.data, "database.json")


schedule.every().day.at("06:00").do(send_msg)
schedule.every().day.at("09:00").do(send_msg)
schedule.every().day.at("14:00").do(send_msg)
schedule.every().day.at("17:00").do(send_msg)

#schedule.every().day.at("04:00").do(update_data)

# ----- For Debugging -------#

#schedule.every(10).seconds.do(send_msg)

# ----------------------------#

while True:
    schedule.run_pending()
    time.sleep(1)
