import telebot
from telebot import types
import config
import requests
import shutil
import random

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def bot_start(msg):
    bot.send_message(msg.chat.id, f'Привет, {msg.chat.first_name}! Тут нечего нет зря ты сюда пришёл')
    main_menu(msg)   
 
 
def main_menu(msg):
#     keyboard = types.ReplyKeyboardMarkup()
#     help_btn = types.KeyboardButton('Тимы нет!')
#     topic_btn = types.KeyboardButton('ТеаМ')
#     keyboard.row(topic_btn, help_btn)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add( *[types.KeyboardButton(name) for name in['Тимы нет!','ТеаМ','Тима есть но они как обычно!']])
    bot.send_message(msg.chat.id, 'Вы в Мейне,выбери то чего нет',reply_markup=keyboard)
    bot.register_next_step_handler(msg,choose_step_0)
        
def choose_step_0(msg):
    if 'Тимы нет!' in msg.text:
        bot.send_message(msg.chat.id, 'Тимы нет как обычно!')
        
        r = requests.get(f'https://picsum.photos/200/300', stream = True)
        
        with open('img.png','wb') as out_file:
           shutil.copyfileobj(r.raw,out_file)
        del r
        
        photo = open('img.png','rb')
        bot.send_photo(msg.chat.id, photo)
        
        main_menu(msg)
        
    elif msg.text=='ТеаМ':
        pass
    else:
        bot.send_message(msg.chat.id, 'Error 404')
        
    
if __name__=='__main__':
    bot.polling(none_stop=True)



