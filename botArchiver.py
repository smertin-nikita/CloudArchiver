import config
import telebot
from telebot import types
from VkRequester import VkUser

bot = telebot.TeleBot(config.telegram_token, parse_mode=None)


def generate_markup():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Да')
    itembtn2 = types.KeyboardButton('Нет')
    markup.add(itembtn1, itembtn2)
    return markup


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Ваш id или screen name в Вконтакте?")


@bot.message_handler(commands=['vk'])
def vk_auth(message):
    command = message.text.split(maxsplit=1)
    if len(command) < 1:
        check_answer(message)
    else:
        uid = command[1].rsplit()
        vk_user = VkUser(uid)


@bot.message_handler(content_types=['text'])
def check_answer(message):
    text = """Привет,
    Введи /vk <страница vk>;
    Введи /disk 
    """
    bot.reply_to(message, text)


bot.polling()
