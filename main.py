import telebot
import numpy as np
import re


BOT_TOKEN = '7977898546:AAEvj45VnuaOBknLwHmgvQhcoU2daXlTnGY'
bot = telebot.TeleBot(BOT_TOKEN)

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except (SyntaxError, TypeError, NameError):
        return "Ошибка: Некорректное математическое выражение."
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль!"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """
Привет! Я бот-калькулятор.
Просто отправьте мне математическое выражение, и я его вычислю.
Например: 2 + 2 * 2
Поддерживаются операции: +, -, *, /, ()
    """)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    expression = message.text
    result = evaluate_expression(expression)
    bot.reply_to(message, result)

if __name__ == '__main__':
    print("Бот запущен!")
    bot.infinity_polling()