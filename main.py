import telebot
import re
from pytube import YouTube
import shutil

TOKEN = '6261451109:AAEt3IUlWpFmUfnVRl0s-pxJm_cAQ132p-k'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id, "Hello")
#Вова
def get_music(link): 
  yt = YouTube(link) 
  streams = yt.streams
  audio = streams.filter(only_audio=True).desc().first()
  audio.download("Music") 
  
def delete_music(path):
  shutil.rmtree(path)
  
get_music('https://youtu.be/fNFzfwLM72c')



#Игорь
@bot.message_handler(func=lambda message: True)
def answer(message_link):
    if match_regex(message_link.text):
	    bot.send_message(message_link.chat.id, 'Вызываю метод Вовы')
    else:
      bot.send_message(message_link.chat.id, 'It is not a youtube link')
      
#Игорь
def match_regex(message_text):
    p = re.compile('^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$')
    if p.match(message_text) == None:
        return False
    else:
        return True
  

bot.infinity_polling()
