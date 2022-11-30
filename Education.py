import requests
from bs4 import BeautifulSoup as b, BeautifulSoup
import telebot
import random

from urllib3.util import url

URL = 'https://www.anekdot.ru/'
API_KEY = '5347946611:AAFfqpsuqXzzOtlLPiSAsHkcoBiX9PAQuCE'


def parcer(URL):
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]


list_of_jokers = parcer(URL)
random.shuffle(list_of_jokers)

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Начать'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет, нажми цифру от 1 до 9')


@bot.message_handler(content_types=['text'])
def joker(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_jokers[0])
        del list_of_jokers[0]
    else:
        bot.send_message(message.chat.id, 'Цифру !!!')


bot.polling()
