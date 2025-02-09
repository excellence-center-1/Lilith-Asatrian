from typing import Final
import telebot
TOKEN: Final = '8051931668:AAGrEmZ0l9acwcw66ArZDQ1KwX3rLMqLEKg'
BOT_USERNAME: Final = '@vsu_students_bot'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def greet_user(message):
    bot.reply_to(message, 'Ես ՎՊՀ բոտ եմ!!')

bot.polling()