import telebot

TOKEN = '6261451109:AAEt3IUlWpFmUfnVRl0s-pxJm_cAQ132p-k'
bot=telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.infinity_polling() #



