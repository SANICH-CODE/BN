from testf import loggingf, adminloggingf, banloggingf
import time
from email import message
import requests
import shutil
import ru
from functions import user, flog
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


def register_commands(bot):
    @bot.message_handler(commands=['set_admin'])
    def ban_command(message):
        if vass_private.is_admin(message.from_user.id):
            if len(message.text.split()) != 2:
                bot.send_message(message.chat.id, "Использование: /set_admin [user_id]")
                return

            user_id = message.text.split()[1]
            result = vass_private.set_admin(user_id)
            adminloggingf(user_id, "Выдача прав администратора", message.from_user.id, message.from_user.username)
            bot.send_message(message.chat.id, result)
        else:
            bot.send_message(message.chat.id, "У вас нет доступа к этой команде")

    @bot.message_handler(commands=['set_user'])
    def ban_command(message):

        if vass_private.is_admin(message.from_user.id):
            if len(message.text.split()) != 2:
                bot.send_message(message.chat.id, "Использование: /set_user [user_id]")
                return

            user_id = message.text.split()[1]
            result = vass_private.set_user(user_id)
            log = f'CONSOLE LOG | SETUSER | {message.from_user.id} | {user_id}'
            url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=6978792645&text={log}'
            adminloggingf(user_id, "Снятие прав администратора", message.from_user.id, message.from_user.username)
            requests.get(url)
            bot.send_message(message.chat.id, result)
        else:
            bot.send_message(message.chat.id, "У вас нет доступа к этой команде")

    @bot.message_handler(commands=['ban'])
    def ban_command(message):
        if vass_private.is_admin(message.from_user.id):
            args = message.text.split(maxsplit=2)  # Ограничиваем количество разбиений на 2
            if len(args) != 3:
                bot.send_message(message.chat.id, "Использование: /to [user_id] MSG")
                return

            user_id = args[1]
            reason = args[2]
            result = vass_private.ban_user(user_id, message.from_user.id, message.from_user.username, reason)
            banloggingf(user_id, "Блокировка", message.from_user.id, message.from_user.username, reason)
            bot.send_message(message.chat.id, result)
        else:
            bot.send_message(message.chat.id, "У вас нет доступа к этой команде")






    @bot.message_handler(commands=['unban'])
    def ban_command(message):
        if vass_private.is_admin(message.from_user.id):
            args = message.text.split(maxsplit=2)  # Ограничиваем количество разбиений на 2
            if len(args) != 3:
                bot.send_message(message.chat.id, "Использование: /to [user_id] MSG")
                return

            user_id = args[1]
            reason = args[2]
            banloggingf(user_id, "Разблокировка", message.from_user.id, message.from_user.username, reason)
            result = vass_private.unban_user(user_id, message.from_user.id, message.from_user.username, reason)
            bot.send_message(message.chat.id, result)
        else:
            bot.send_message(message.chat.id, "У вас нет доступа к этой команде")

    @bot.message_handler(commands=['set_premium'])
    def set_premium(message):
        if vass_private.is_admin(message.from_user.id):
            if len(message.text.split()) != 2:
                bot.send_message(message.chat.id, "Использование: /set_premium [user_id]")
                return

            user_id = message.text.split()[1]
            result = vass_private.set_premium(user_id)
            adminloggingf(user_id, "Выдача BN Plus", message.from_user.id, message.from_user.username)
            bot.send_message(message.chat.id, result)
        else:
            bot.send_message(message.chat.id, "У вас нет доступа к этой команде")

    @bot.message_handler(commands=['block_premium'])
    def set_premium(message):
        if vass_private.is_admin(message.from_user.id):
            if len(message.text.split()) != 2:
                bot.send_message(message.chat.id, "Использование: /block_premium [user_id]")
                return

            user_id = message.text.split()[1]
            result = vass_private.den_premium(user_id)
            adminloggingf(user_id, "Снятие BN Plus", message.from_user.id, message.from_user.username)
            bot.send_message(message.chat.id, result)
        else:
            bot.send_message(message.chat.id, "У вас нет доступа к этой команде")