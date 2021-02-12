import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.telegram_token, parse_mode=None)


def generate_markup():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Да')
    itembtn2 = types.KeyboardButton('Нет')
    markup.add(itembtn1, itembtn2)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Ваш id или screen name в Вконтакте?")


@bot.message_handler(content_types=['text'])
def check_answer(message):
    text = """Привет,
    Введи /vk <страница vk>;
    Введи /disk 
    """
    bot.reply_to(message, text)


bot.polling()
