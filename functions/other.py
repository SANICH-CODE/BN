from testf import loggingf, adminloggingf, banloggingf
import time
from email import message
import requests
import shutil
import ru
from functions import user, admin, flog
import vass_private
import pytz
PROXY_API_KEY = 'sk-04QYlQmpbMQFmMJMhB6o4Z9N0sqMcrBy'
from threading import Thread
from telebot import *
from vass_private import TOKEN
import random
import os
import json
bot = telebot.TeleBot(TOKEN)

import datetime
from flask import Flask
app = Flask(__name__)
current_date = datetime.date.today()
current_date_time = datetime.datetime.now()
current_time = current_date_time.time()

def generate_password():
    return ''.join(random.choices('0123456789', k=6))


# Функция для загрузки пользователей из файла JSON
def load_users():
    with open('../users.json', 'r') as f:
        return json.load(f)

# Функция для сохранения пользователей в файл JSON
def save_users(users):
    with open('../users.json', 'w') as f:
        json.dump(users, f, indent=4)