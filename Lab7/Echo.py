import telebot
import os
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.environ['TOKEN'])


@bot.message_handler(func=lambda message: True )
def echo(message):
    bot.send_message(message.chat.id, message.text)

if name == 'main':
    bot.polling()
