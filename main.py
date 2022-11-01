import telebot
from telebot import types
from datetime import datetime
from text import Text

token = "5398483352:AAE572M-khWSlhb63v5u8Qcg4hM-XW2FNcw"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("Привет")
    button2 = types.KeyboardButton("Создать деревню")
    markup.add(button1, button2)

    bot.send_message(message.from_user.id, Text.start, reply_markup=markup)


@bot.message_handler(content_types=["text"])
def main(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "И тебе привет")
    elif message.text == "Создать деревню":
        """ LOG:: Добавить проверку на уже созданную деревню из БД"""
        bot.send_message(message.from_user.id,Text.new_village)
    else:
        bot.send_message(message.from_user.id, "Моя твоя не понимать")


bot.polling(non_stop=True)
