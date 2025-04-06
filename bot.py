import telebot
from telebot import types # для указание типов
from config import *
from random import choice
from logic_ai import Text2ImageAPI
import base64
import random

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📚 Учёба")
    btn2 = types.KeyboardButton("🎮 Играть")
    btn3 = types.KeyboardButton("❓ Задать вопрос")
    btn4 = types.KeyboardButton("🌅 Генератор картинок")
    markup.add(btn1, btn2, btn3, btn4)
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
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif(message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")
    
    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")
    
    elif (message.text == "🔙 Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("📚 Учёба")
        button2 = types.KeyboardButton("🎮 Играть")
        button3 = types.KeyboardButton("❓ Задать вопрос")
        button4 = types.KeyboardButton("🌅 Генератор картинок")
        markup.add(button1, button2, button3, button4)
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

    elif(message.text == "🌅 Генератор картинок"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttn1 = types.KeyboardButton("Сгенерировать картинку")
        buttn2 = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.add(buttn1, buttn2)
        bot.send_message(message.chat.id, text="Нажми на кнопку", reply_markup=markup)

    elif (message.text == "Сгенерировать картинку"):
            promt = message.text

            send_message = bot.reply_to(message, "Генерирую картинку...")
            bot.send_chat_action(message.chat.id, "typing")

            api = Text2ImageAPI('https://api-key.fusionbrain.ai/', api_token, secret_key)
            model_id = api.get_model()
            uuid = api.generate(promt, model_id)
            images = api.check_generation(uuid)
            image_base64 = images[0]
            image_data = base64.b64decode(image_base64)
            file_name = "generated_image"+str(random.randint(0, 1000))+".jpg"
            with open(f"img/{file_name}", "wb") as file:
                file.write(image_data)
            with open(f"img/{file_name}", "rb") as file:
                bot.send_photo(message.chat.id, file)

            bot.delete_message(message.chat.id, send_message.message_id)

bot.polling(none_stop=True)
