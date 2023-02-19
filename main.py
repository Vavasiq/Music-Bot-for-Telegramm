import telebot
import re
from pytube import YouTube
import shutil
import os

TOKEN = '6261451109:AAEt3IUlWpFmUfnVRl0s-pxJm_cAQ132p-k'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello")


# Игорь
@bot.message_handler(func=lambda message: True)
def answer(user_message):
  if is_youtube_link(user_message.text):
    bot.send_message(user_message.chat.id, 'Качаю')
    get_music(user_message.text)
    send_music(user_message.text, user_message)
  else:
        bot.send_message(user_message.chat.id, 'It is not a youtube link')

# Игорь
def is_youtube_link(user_message):
    pattern = re.compile('^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$')
    if pattern.match(user_message) == None:
        return False
    else:
        return True

# Вова
def get_music(link):
    yt = YouTube(link)
    streams = yt.streams
    audio = streams.filter(only_audio=True).desc().first()
    audio.download("Music")

def send_music(link, user_message):
    yt = YouTube(link)
    audio = open(f'Music/{yt.title}.webm', 'rb')
    bot.send_audio(user_message.chat.id, audio)

# Вова
def delete_music(path):
    shutil.rmtree(path)

bot.infinity_polling()
