from testf import loggingf, adminloggingf, banloggingf
import requests
import ru
from functions import admin, flog
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


def register_commands(bot):
    @bot.message_handler(commands=['search'])
    def search_command(message):
        if vass_private.is_admin(message.from_user.id):
            global banned
            if len(message.text.split()) != 2:
                bot.send_message(message.chat.id, "Использование: /search [user_id]")
                return

            user_id = message.text.split()[1]
            username = vass_private.search_user(user_id, keys_to_return=['username'])
            if vass_private.search_user(user_id, keys_to_return=['status']) == 'admin':
                rank = "Administrator"
            else:
                rank = "User"
            datareg = vass_private.search_user(user_id, keys_to_return=['RegDate', 'RegTime'])
            ban = vass_private.search_user(user_id, keys_to_return=['ban'])
            adminloggingf(user_id, "Поиск", message.from_user.id, message.from_user.username)
            if ban == "False":
                if rank == 'Administrator':
                    markup = telebot.types.InlineKeyboardMarkup()
                    banb = telebot.types.InlineKeyboardButton(f"Заблокировать {username}",
                                                              callback_data=f'ban_{user_id}')
                    user = telebot.types.InlineKeyboardButton(f"Понизить {username} до User",
                                                              callback_data=f'setuser_{user_id}')
                    markup.row(banb)
                    markup.row(user)
                    bot.send_message(message.chat.id,
                                     f"Пользователь найден\n\nUser id: {user_id}\nUsername: {username}\n\nДата регистрации: {datareg}\nРанг: {rank}\nBN Plus: {vass_private.is_premium(user_id)}\nБлокировка: Нет\n\nДля блокировки используйте /ban",
                                     reply_markup=markup)
                else:
                    markup = telebot.types.InlineKeyboardMarkup()
                    banb = telebot.types.InlineKeyboardButton(f"Заблокировать {username}",
                                                              callback_data=f'ban_{user_id}')
                    user = telebot.types.InlineKeyboardButton(f"Повысить {username}",
                                                              callback_data=f'setadmin_{user_id}')
                    markup.row(banb)
                    markup.row(user)
                    bot.send_message(message.chat.id,
                                     f"Пользователь найден\n\nUser id: {user_id}\nUsername: {username}\n\nДата регистрации: {datareg}\nРанг: {rank}\nBN Plus: {vass_private.is_premium(user_id)}\nБлокировка: Нет\n\nДля блокировки используйте /ban",
                                     reply_markup=markup)
            elif ban == "True":
                if rank == 'Administrator':
                    markup = telebot.types.InlineKeyboardMarkup()
                    banb = telebot.types.InlineKeyboardButton(f"Разблокировать {username}",
                                                              callback_data=f'unban_{user_id}')
                    user = telebot.types.InlineKeyboardButton(f"Понизить {username} до User",
                                                              callback_data=f'setuser_{user_id}')
                    markup.row(banb)
                    markup.row(user)
                    bot.send_message(message.chat.id,
                                     f"Пользователь найден\n\nUser id: {user_id}\nUsername: {username}\n\nДата регистрации: {datareg}\nРанг: {rank}\nBN Plus: {vass_private.is_premium(user_id)}\nБлокировка: Есть\n\nДля блокировки используйте /ban",
                                     reply_markup=markup)
                else:
                    markup = telebot.types.InlineKeyboardMarkup()
                    banb = telebot.types.InlineKeyboardButton(f"Разблокировать {username}",
                                                              callback_data=f'unban_{user_id}')
                    user = telebot.types.InlineKeyboardButton(f"Повысить {username}",
                                                              callback_data=f'setadmin_{user_id}')
                    markup.row(banb)
                    markup.row(user)
                    bot.send_message(message.chat.id,
                                     f"Пользователь найден\n\nUser id: {user_id}\nUsername: {username}\n\nДата регистрации: {datareg}\nРанг: {rank}\nBN Plus: {vass_private.is_premium(user_id)}\nБлокировка: Есть\n\nДля блокировки используйте /ban",
                                     reply_markup=markup)
            else:
                bot.send_message(message.chat.id, f"НЕ НАЙДЕНО")
        else:
            bot.send_message(message.chat.id, "У вас нет доступа к этой команде")

    @bot.message_handler(commands=['to'])
    def to_command(message):
        if vass_private.is_admin(message.from_user.id):
            args = message.text.split(maxsplit=2)  # Ограничиваем количество разбиений на 2
            if len(args) != 3:
                bot.send_message(message.chat.id, "Использование: /to [user_id] MSG")
                return

            user_id = args[1]
            text = args[2]  # Текст может содержать пробелы
            result = vass_private.to_msg(user_id, text, message.from_user.id, message.from_user.username)

            bot.send_message(message.chat.id, f"Отправлено {result}")
            banloggingf(user_id, message.from_user.id, message.from_user.username, text)
        else:
            bot.send_message(message.chat.id, "У вас нет доступа к этой команде")

    @bot.message_handler(commands=['getusers'])
    def get_logs_command(message):
        if vass_private.is_admin(message.from_user.id):
            adminloggingf("System", "Запрос данных пользоватеелей", message.from_user.id, message.from_user.username)
            # Проверка существования файла logs.json
            if os.path.exists('../users.json'):
                with open('../users.json', 'rb') as file:
                    bot.send_document(message.chat.id, file, caption="Содержимое файла строго конфиденциально")
                    adminloggingf("System", "Выдача данных пользоватеелей", message.from_user.id,
                                  message.from_user.username)

            else:
                bot.send_message(message.chat.id, "Логи отсутствуют.")
        else:
            bot.send_message(message.chat.id, "У вас нет доступа к этой команде")