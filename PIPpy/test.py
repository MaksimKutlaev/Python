import telebot
from telebot import types
import logging
from random import randint

bot = telebot.TeleBot("5952862933:AAHGZn1Yzf77nbtjCC6txGlXdCoJ6do7UB0")

storage = dict()

def init_storage(user_id):
    storage[user_id] = dict(attempt=None, random_digit=None)

def set_data_storage(user_id, key, value):
    storage[user_id][key] = value

def get_data_storage(user_id):
    return storage[user_id]
    
def del_abv(text):
    text=text.split()
    return' '.join([i for i in text if 'абв' not in i])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"{message.from_user.first_name}, how are you doing?")
    
@bot.message_handler(func=lambda message: message.text.lower() == "игра")
def digitgame(message):
    # init_storage(message.chat.id)
    candys=117
    bot.send_message(message.chat.id, f'Начало игры -> Конфеты')
    bot.send_message(message.chat.id, f'На столе {candys} конфет')
    bot.send_message(message.chat.id, f'Тащите по очереди конфеты не более 28 штук')
    bot.send_message(message.chat.id, f'Кто последний берет конфеты, тот проиграл!')
    player1=message.from_user.first_name
    player2="Bot"
    flag = randint(0,2)
    if flag:
        bot.send_message(message.chat.id, f'Первым ходит {player1}')
    else:
        bot.send_message(message.chat.id, f'Первым ходит {player2}')
    counter1 = 0 
    counter2 = 0
    while candys > 28:
        if flag:
            k = input_dat(player1)
            counter1 += k
            candys -= k
            flag = False
            p_print(player1, k, counter1, candys)
        else:
            k = bot_calc(candys)
            counter2 += k
            candys -= k
            flag = True
            p_print(player2, k, counter2, candys, message)

    if flag:
        bot.send_message(message.chat.id, f"Выиграл {player1}")
    else:
        bot.send_message(message.chat.id, f"Выиграл {player2}")

def p_print(name, k, counter, value, message):
    bot.send_message(message.chat.id, f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

def input_dat(message):

    # user_digit = message.text
    # if not user_digit.isdigit():
    #         msg = bot.reply_to(message, 'Вы ввели не цифры, введите пожалуйста цифры')
    #         bot.register_next_step_handler(msg, input_dat)
    #         return
    # int(message.text)
    bot.reply_to(message,f"{message.from_user.first_name}, введите количество конфет, которое возьмете от 1 до 28: ")
    bot.register_next_step_handler(msg,input_dat)
    while message < 1 or message > 28:
        msg=bot.send_message(message, f"{message.from_user.first_name}, введите корректное количество конфет: ")
        bot.register_next_step_handler(msg,input_dat)
        return message
    
        
        
@bot.message_handler(func=lambda message: message.text.lower() == "привет")
def command_text_hi(message):
    bot.send_message(message.chat.id, "Ну привет)")

@bot.message_handler(func=lambda message: message.text.lower() == "как дела?")
def command_text_dela(m):
    bot.send_message(m.chat.id, "хорошо")

    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, del_abv(message.text))
   






bot.infinity_polling()