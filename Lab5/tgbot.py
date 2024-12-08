import telebot;
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler, MessageHandler, ConversationHandler, filters, CallbackContext, Updater

from config import Config

from telebot import types

token = '7770486510:AAFyqeYENAxuRbj6Vpaf73520Y_fm8gqXkg'
bot=telebot.TeleBot(token)

bot.delete_webhook()



@bot.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nxочешь расскажу немного об этом проекте?"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes')
  markup.add(button_yes)
  bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)




@bot.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     if function_call.data == "yes":
        second_mess = "это я rema, занимаюсь сведением треков, продакшеном битов и лупов \n узнать обо мне больше можно с помощью команд: \n   /price - узнать цены \n  /portfolio - оценить работы"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("мой тгк", url="https://t.me/remabeats"))
        bot.send_photo(function_call.message.chat.id, photo=open('D:/photo_2024-12-08_21-35-06.jpg', 'rb'), caption=second_mess ,reply_markup=markup)
        bot.answer_callback_query

@bot.message_handler(commands=['portfolio'])
def portfolioBot(message):
    bot.send_audio(message.chat.id, audio=open('D:/@rema_135(Gm)_yot3.mp3', 'rb'), caption="такие дела")

@bot.message_handler(commands=['price'])
def priceBot(message):
  price = "wav -  1500 \n trackout - 2500 \n exclusive - dm  @..."
  bot.send_message(message.chat.id, price)



bot.polling()