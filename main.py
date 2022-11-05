import telebot
from telebot import types

import data
from text import Text

token = "5398483352:AAE572M-khWSlhb63v5u8Qcg4hM-XW2FNcw"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("Привет")
    button2 = types.KeyboardButton("Создать деревню")
    button3 = types.KeyboardButton("Инфо")
    markup.add(button1, button2, button3)

    bot.send_message(message.from_user.id, Text.start, reply_markup=markup)


@bot.message_handler(content_types=["text"])
def main(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "И тебе привет")
    elif message.text == "Создать деревню":
        new_village(message)
    elif message.text == "Инфо":
        send_info(message)
    else:
        bot.send_message(message.from_user.id, "Моя твоя не понимать")


def new_village(message):
    """ LOG:: Добавить проверку на уже созданную деревню из БД"""
    data.generate_new_user(message.from_user.id)
    bot.send_message(message.from_user.id, Text.new_village)
    bot.register_next_step_handler(message, name_new_village)


def name_new_village(message):
    """ LOG:: name скачивать из БД"""
    name = message.text
    data.set_name(message.from_user.id, name)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("Да")
    button2 = types.KeyboardButton("Нет")
    markup.add(button1, button2)

    bot.send_message(message.from_user.id, "Ваша деревня называется: " + name + "\nПодходит данное название? (Да/Нет)",
                     reply_markup=markup)
    bot.register_next_step_handler(message, choice_name_village)


def choice_name_village(message):
    if message.text == "Да":
        bot.send_message(message.from_user.id,
                         "Отлично, поздравляем с созданием собственной деревни")
    else:
        bot.send_message(message.from_user.id,
                         "Введите название деревни: ")
        bot.register_next_step_handler(message, name_new_village)


def send_info(message):
    info = data.get_data_person(message.from_user.id)
    bot.send_message(message.from_user.id, Text.stat(Text,data = info))


bot.polling(non_stop=True)
