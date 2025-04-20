import telebot
from telebot import types # для указание типов
from config import *
from random import choice
from logic_ai import Text2ImageAPI
import base64
import random
import pyjokes

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("❓ Задать вопрос")
    btn2 = types.KeyboardButton("📚 Учёба")
    btn3 = types.KeyboardButton("🎮 Играть")
    btn4 = types.KeyboardButton("😂 Генератор шуток")
    btn5 = types.KeyboardButton("⭐️ Оценить")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я телеграмм-бот онлайн-школы, который обеспечит тебя и других учеников удобными и эффективными инструментами для обучения.".format(message.from_user), reply_markup=markup)
    
              
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "📚 Учёба"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Расписание уроков")
        btn2 = types.KeyboardButton("Расписание звонков")
        back = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выбери интересующее", reply_markup=markup)

    elif(message.text == "Расписание уроков"):
        file = open("rasp.jpeg", 'rb')
        bot.send_photo(message.chat.id, file) 
        bot.register_next_step_handler(message, func)

    elif(message.text == "Расписание звонков"):
        file = open("zv.jpg", 'rb')
        bot.send_photo(message.chat.id, file) 
        bot.register_next_step_handler(message, func) 

    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.add (btn2, back) #btn1
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="""\
    1)Прислать расписание уров или расписание звонков 
2)Поиграть в игру Орёл или Решка 
3)Сгенерировать шутку на английском 
4)Оценить бота\
""")
    
    elif (message.text == "🔙 Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("❓ Задать вопрос")
        button2 = types.KeyboardButton("📚 Учёба")
        button3 = types.KeyboardButton("🎮 Играть")
        button4 = types.KeyboardButton("😂 Генератор шуток")
        button5 = types.KeyboardButton("⭐️ Оценить")
        markup.add(button1, button2, button3, button4, button5)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif (message.text == "🎮 Играть"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butt1 = types.KeyboardButton("Орёл или Решка?")
        butt2 = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.add(butt1, butt2)
        bot.send_message(message.chat.id, text="Нажми на кнопку", reply_markup=markup)
    
    elif (message.text == "Орёл или Решка?"):
        coin = choice(["Орёл", "Решка"])
        bot.reply_to(message, coin)

    elif (message.text == "⭐️ Оценить"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buton1 = types.KeyboardButton("5 звезд ⭐️")
        buton2 = types.KeyboardButton("4 звезды ⭐️")
        buton3 = types.KeyboardButton("3 звезды ⭐️")
        buton4 = types.KeyboardButton("2 звезды ⭐️")
        buton5 = types.KeyboardButton("1 звезда ⭐️")
        back = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.add(buton1, buton2, buton3, buton4, buton5, back)
        bot.send_message(message.chat.id, text="Оцени бота по 5-ти бальной шкале", reply_markup=markup)

    elif (message.text == "5 звезд ⭐️"):
        bot.send_message(message.chat.id, text="Спасибо за оценку!")

    elif (message.text == "4 звезды ⭐️"):
        bot.send_message(message.chat.id, text="Спасибо за оценку!")

    elif (message.text == "3 звезды ⭐️"):
        bot.send_message(message.chat.id, text="Спасибо за оценку!")

    elif (message.text == "2 звезды ⭐️"):
        bot.send_message(message.chat.id, text="Что нам следует исправить?")

    elif (message.text == "1 звезда ⭐️"):
        bot.send_message(message.chat.id, text="Что нам следует исправить?")

    elif(message.text == "😂 Генератор шуток"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttn1 = types.KeyboardButton("Сгенерировать шутку")
        buttn2 = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.add(buttn1, buttn2)
        bot.send_message(message.chat.id, text="Нажми на кнопку", reply_markup=markup)

    elif (message.text == "Сгенерировать шутку"):
        joke = pyjokes.get_joke(language="en", category="all")
        bot.send_message(message.chat.id, joke)

bot.polling(none_stop=True)
