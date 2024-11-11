from testf import loggingf, adminloggingf, banloggingf
import requests
import ru
from functions import user, admin
from functions.other import generate_password
import vass_private
import os
PROXY_API_KEY = 'sk-04QYlQmpbMQFmMJMhB6o4Z9N0sqMcrBy'
from threading import Thread
from telebot import *
from vass_private import TOKEN
import json
bot = telebot.TeleBot(TOKEN)

import datetime
from flask import Flask
app = Flask(__name__)
current_date = datetime.date.today()
current_date_time = datetime.datetime.now()
current_time = current_date_time.time()
#TODO Сократить
def register_commands(bot):
    @bot.message_handler(commands=['getlogs'])
    def get_logs_command(message):
        if vass_private.is_admin(message.from_user.id):
            adminloggingf("System", "Запрос истории действий", message.from_user.id, message.from_user.username)
            if os.path.exists('../logs.json'):
                with open('../logs.json', 'rb') as file:
                    bot.send_document(message.chat.id, file, caption="Содержимое файла строго конфиденциально")
                    adminloggingf("System", "Выдача истории действий", message.from_user.id, message.from_user.username)

            else:
                bot.send_message(message.chat.id, "Логи отсутствуют.")
        else:
            bot.send_message(message.chat.id, "У вас нет доступа к этой команде")

    @bot.message_handler(commands=['getoldlogs'])
    def get_logs_command(message):
        if vass_private.is_admin(message.from_user.id):
            adminloggingf("System", "Запрос истории действий", message.from_user.id, message.from_user.username)
            if os.path.exists('../old-logs.json'):
                with open('../old-logs.json', 'rb') as file:
                    bot.send_document(message.chat.id, file, caption="Содержимое файла строго конфиденциально")
                    adminloggingf("System", "Выдача истории действий", message.from_user.id, message.from_user.username)

            else:
                bot.send_message(message.chat.id, "Логи отсутствуют.")
        else:
            bot.send_message(message.chat.id, "У вас нет доступа к этой команде")