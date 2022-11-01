import telebot
from telebot import types
from datetime import datetime

token = "5109635135:AAFQ1zCIZ8-Xs34LnPLiS5V9yN-VdkbXZ34"
bot = telebot.TeleBot("5109635135:AAFQ1zCIZ8-Xs34LnPLiS5V9yN-VdkbXZ34")

@bot.message_handler(content_types=["text"])
def main(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,"И тебе привет")

bot.polling(non_stop=True)