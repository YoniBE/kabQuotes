from credentials import bot_user_name, bot_token
import QuoteData
from telegram.ext import Updater, CommandHandler
import logging

global bot
global TOKEN
TOKEN = bot_token

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
#logging.basicConfig(format="%(asctime)s -%(levelname)s -%(messages", level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id="755735701", text="hi")


dispatcher.add_handler(CommandHandler("start", start))

# data = QuoteData.load_json_data("t.json")
# msg = data["quote"][5] + "\n" + "<b><i>" + data["ref"][5] + "</i></b>"
# context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
#
# start_handler = CommandHandler('start',start)
# dispatcher.add_handler(start_handler)
#
# updater.start_polling()


# import QuoteData
# import telegram
# import datetime
# from credentials import bot_user_name, bot_token
# from telegram.ext import Updater, CommandHandler
#
# import apscheduler
#
# global bot
# global TOKEN
# TOKEN = bot_token
# bot = telegram.Bot(token=TOKEN)
#
# def schedule():
#     t = datetime.time(8,25, tzinfo="Jerusalem")
#
# def send_msg():
#     data = QuoteData.load_json_data("t.json")
#     msg = data["quote"][5] + "\n" + "<b><i>" + data["ref"][5] + "</i></b>"
#     bot.send_message(chat_id="-1001611107723", text=msg, parse_mode=telegram.ParseMode.HTML)
#
# send_msg()

# t = datetime.time(4, 45, 00, 000000)
# updater = Updater(TOKEN)
# job = updater.job_queue
# updater.job_queue.run_daily(send_msg, t, days=tuple(range(5)), context=None, name=None)

# quote_obj = QuoteData.InitData("test.csv")
# QuoteData.SaveData(quote_obj.data, "t.json")
# data = QuoteData.load_json_data("t.json")
