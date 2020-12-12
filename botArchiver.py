import telebot

import os
import os.path as op


TOKEN_PATH = 'config'


def get_token():
    path = op.join(os.getcwd(), TOKEN_PATH)
    try:
        with open(path, 'r') as f:
            token = f.readline()
    except FileNotFoundError:
        print("File not found")
    return token


bot = telebot.TeleBot(get_token(), parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Ты Какашка!")


@bot.message_handler(content_types=['text'])
def echo_all(message):
    bot.send_message(message.chat.id, 'Ты какашка!')


bot.polling()
