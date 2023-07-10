import os
from telebot import types
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot('6394570120:AAHwDpG6jMy0pUMmVr-C3oR2zKpBZQmhUWg')

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Download movie","Download playlist")
    keyboard.row("Share phone number")
    bot.send_message(message.chat.id,"Hello  {0.first_name} {0.last_name}. I am {1.first_name}".format(message.from_user,bot.get_me()),reply_markup=keyboard)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()