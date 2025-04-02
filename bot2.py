import telebot
from telebot import types # для указание типов
import config

bot = telebot.TeleBot(config.API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Расписание уроков")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    btn3 = types.KeyboardButton("вопрос")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я телеграмм-бот онлайн-школы, который обеспечит тебя и других учеников удобными и эффективными инструментами для обучения.".format(message.from_user), reply_markup=markup)
    
# @bot.message_handler(content_types=['text'])
# def func(message):
#     if(message.text == "Расписание уроков"):
#         bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
              
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Расписание уроков"):
        file = open("54.png", 'rb')
        bot.send_photo(message.chat.id, file) 
        bot.register_next_step_handler(message, start) 

    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif(message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")
    
    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Расписание уроков")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        button3 = types.KeyboardButton("вопрос")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)