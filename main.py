import telebot
from telebot import types
from datetime import datetime
from text import Text

token = "5398483352:AAE572M-khWSlhb63v5u8Qcg4hM-XW2FNcw"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.KeyboardButton("Привет")
    markup.add(button)

    bot.send_message(message.from_user.id, Text.start, reply_markup=markup)


@bot.message_handler(content_types=["text"])
def main(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "И тебе привет")


bot.polling(non_stop=True)
