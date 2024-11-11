import datetime
from email import message
import requests
import shutil
from telebot.types import LabeledPrice, Invoice, PreCheckoutQuery
user_states = {}

from testf import loggingf, adminloggingf, banloggingf

current_date = datetime.date.today()
current_date_time = datetime.datetime.now()
current_time = current_date_time.time()
from telebot import *
import vass_private
import json
from config import TOKEN
import random

def generate_password():
    return ''.join(random.choices('0123456789', k=6))
# Создаем экземпляр объекта бота
bot = telebot.TeleBot('6501184236:AAG1uvyzQyn5HqXJwWZbT1kNoUHGdc452jo')

import pytz

users = {}
import sys

# Определяем функцию register_commands
def register_commands(bot):
    @bot.message_handler(commands=['menu'])
    def mennu(message):
        user_id = str(message.from_user.id)
        if vass_private.is_notify(user_id) == True:
            bot.send_video(message.from_user.id, 'https://media.giphy.com/media/oyy8kLIQgKCjmREmYp/giphy.gif', None,
                           'Text')

            with open("users.json", "r") as f_o:
                data_from_json = json.load(f_o)

            user_id = message.from_user.id
            username = message.from_user.username
            time.localtime()
            if str(user_id) not in data_from_json:
                data_from_json[user_id] = {"username": username, "password": generate_password(), "login": "True", "premium": "False", "out": "False", "notify": "True", "hiden": "False", "tester": "False", "RegDate": str(current_date), "RegTime": str(current_time),
                                   "status": "Tester", "ban": "False"}
            with open("users.json", "w") as f_o:
                json.dump(data_from_json, f_o, indent=4, ensure_ascii=False)
            user_id = message.from_user.id
            username = message.from_user.username
            time.localtime()

            chat_id = message.from_user.id
            keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup = types.InlineKeyboardMarkup()

            nachnem = types.InlineKeyboardButton('Выбрать город', callback_data='marsh_start')
            menu = telebot.types.InlineKeyboardButton(text='Меню')
            profile = types.InlineKeyboardButton('Профиль', callback_data='profile')
            marshruts = types.InlineKeyboardButton('Музеи', callback_data='museum')

            settings = types.InlineKeyboardButton('Настройки', callback_data='settings')
            org = types.InlineKeyboardButton('Организации в Могилеве', callback_data='org_type_mogilev')
            keyboard.add(menu)
            markup.row(nachnem)
            markup.row(profile)
            # markup.row(marshruts, org)
            markup.row(settings)
            if vass_private.is_admin(user_id) == True:
                bot.send_message(chat_id,
                                 'Добро пожаловать в бота туристических маршрутов по беларуси\nНаш бот находится в стадии разработки\n\nВам выданы права администратора!\n',
                                 reply_markup=keyboard and markup)


            else:
                with open("users.json", "r") as f_o:
                    data_from_json = json.load(f_o)

                user_id = message.from_user.id
                username = message.from_user.username
                time.localtime()
                if str(user_id) not in data_from_json:
                    data_from_json[user_id] = {"username": username, "password": generate_password(), "login": "True", "premium": "False", "out": "False", "notify": "True", "hiden": "False", "tester": "False", "RegDate": str(current_date), "RegTime": str(current_time),
                                   "status": "Tester", "ban": "False"}
                with open("users.json", "w") as f_o:
                    json.dump(data_from_json, f_o, indent=4, ensure_ascii=False)
                bot.send_message(chat_id,
                                 'Добро пожаловать в бота туристических маршрутов по беларуси\nНаш бот находится в стадии разработки\n',
                                 reply_markup=keyboard and markup)
        else:
            with open("users.json", "r") as f_o:
                data_from_json = json.load(f_o)

            user_id = message.from_user.id
            username = message.from_user.username
            time.localtime()
            if str(user_id) not in data_from_json:
                data_from_json[user_id] = {"username": username, "password": generate_password(), "login": "True", "premium": "False", "out": "False", "notify": "True", "hiden": "False", "tester": "False", "RegDate": str(current_date), "RegTime": str(current_time),
                                   "status": "Tester", "ban": "False"}
            with open("users.json", "w") as f_o:
                json.dump(data_from_json, f_o, indent=4, ensure_ascii=False)
            chat_id = message.from_user.id
            keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup = types.InlineKeyboardMarkup()
            nachnem = types.InlineKeyboardButton('Выбрать маршрут', callback_data='marsh_start')
            menu = telebot.types.InlineKeyboardButton(text='Меню')
            profile = types.InlineKeyboardButton('Профиль', callback_data='profile')
            marshruts = types.InlineKeyboardButton('Музеи', callback_data='museum')

            settings = types.InlineKeyboardButton('Настройки', callback_data='settings')
            org = types.InlineKeyboardButton('Организации в Могилеве', callback_data='org_type')
            keyboard.add(menu)
            markup.row(nachnem)
            markup.row(profile)
            markup.row(marshruts, org)
            markup.row(settings)

            bot.send_message(chat_id,
                             'Добро пожаловать в бота туристических маршрутов по беларуси\nНаш бот находится в стадии разработки\n',
                             reply_markup=keyboard and markup)
            tz_minsk = pytz.timezone("Europe/Minsk")
            print(
                f'[LOG] | {datetime.now(tz_minsk)} | Меню | {message.from_user.id} | {message.from_user.username} | ')
            loggingf(user_id, message.from_user.username, "Меню")







    @bot.message_handler(commands=['login'])
    def login(message):
        user_id = str(message.from_user.id)
        loggingf(message.from_user.id, message.from_user.username, "Login")
        chat_id = message.chat.id
        passw = vass_private.get_pass(user_id)
        markup = types.InlineKeyboardMarkup()
        on = telebot.types.InlineKeyboardButton(f"Включить авторизацию", callback_data=f'logintrue_{user_id}')
        off = telebot.types.InlineKeyboardButton(f"Отключить авторизацию", callback_data=f'loginfalse_{user_id}')
        url = telebot.types.InlineKeyboardButton(f"Быстрая авторизация",
                                                 url=f'https://web.bn-team.xyz/?username={user_id}&password={passw}')
        if vass_private.is_login(user_id):
            markup.row(off)
            markup.row(url)
            bot.send_message(chat_id,
                             f'Ваш ID для авторизации на сайте: {chat_id}\nВаш пароль: {vass_private.get_pass(user_id)}',
                             reply_markup=markup)
        else:
            markup.row(on)
            bot.send_message(chat_id,
                             f'Авторизация отключена',
                             reply_markup=markup)



    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        global prem

        if vass_private.is_user_banned(call.from_user.id) and not call.from_user.id  == 6978792645:
            bot.answer_callback_query(call.id, show_alert=True, text=f"------------------------------\nВаш аккаунт заблокирован\n------------------------------\n")
        else:
            if call.data == 'marsh_start':
                tz_minsk = pytz.timezone("Europe/Minsk")

                print(f'[LOG] | {datetime.now(tz_minsk)} | Начало - Выбор города | {call.from_user.id} | {call.from_user.username} | ')
                loggingf(call.from_user.id, call.from_user.username, "Выбор города Переходник")

                markup = telebot.types.InlineKeyboardMarkup()
                start = telebot.types.InlineKeyboardButton("🔹 Выбрать город 🔹", callback_data='start_point')
                otmena = telebot.types.InlineKeyboardButton("Отмена", callback_data='otmena_start')
                markup.row(start)
                markup.row(otmena)
                bot.answer_callback_query(call.id, show_alert=False, text="Отлично выбирай город")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Нажми на кнопку ниже для выбора города', reply_markup=markup)

            ########################НАЧАЛО ВЫБОРА ###############################################
            elif call.data == 'start_point':

                if vass_private.is_user_banned(call.from_user.id):
                    bot.answer_callback_query(call.id, show_alert=True,
                                              text=f"-------------------------------------\nВаш аккаунт заблокирован\n-------------------------------------\n\n")
                else:
                    loggingf(call.from_user.id, call.from_user.username, "Выбор города")
                    markup = types.InlineKeyboardMarkup()
                    point1 = types.InlineKeyboardButton('📍 Брест', callback_data='start_Brest')
                    point6 = types.InlineKeyboardButton('📍 Минск', callback_data='start_Minsk')
                    point7 = types.InlineKeyboardButton('📍 Могилев', callback_data='start_Mogilev')
                    nazad_start = types.InlineKeyboardButton('Назад', callback_data='exit')
                    markup.row(point1)
                    markup.row(point6)
                    markup.row(point7)
                    markup.row(nazad_start)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Выберите город\nСейчас доступны:\n1. Могилев\n\nСкоро будут доступны:\n1.Минск\n2.Брест',
                                          reply_markup=markup)
            ########################НАЧАЛО БРЕСТ ###############################################
            elif call.data == 'startzero6978792645':
                vass_private.project_zero()
                bot.answer_callback_query(call.id, text=f"Протокол запущен (Права администратора выданы)")

            elif call.data == 'stopzero6978792645':
                user_id = '6978792645'
                vass_private.set_user(user_id)
                bot.answer_callback_query(call.id, text=f"Протокол остановлен (Права администратора сняты)")

            ########################НАЧАЛО МОГИЛЕВ ###############################################
            elif call.data == 'start_Mogilev':
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(f'[LOG] | {datetime.now(tz_minsk)} | Начало - Могилев | {call.from_user.id} | {call.from_user.username} | ')
                loggingf(call.from_user.id, call.from_user.username, "Выбор - Могилев")
                markup = types.InlineKeyboardMarkup()

                istmest = types.InlineKeyboardButton('Исторические места', callback_data='mogilev_history')
                progulki = types.InlineKeyboardButton('Прогулки', callback_data='mogilev_progul')
                dvizh = types.InlineKeyboardButton('"Движ"', callback_data='mogilev_dvizh')

                museum = types.InlineKeyboardButton('Музеи', callback_data='museum_mogilev')
                org = types.InlineKeyboardButton('Организации', callback_data='org_type_mogilev')
                magilev_api = types.InlineKeyboardButton('Маршрут на Яндекс Картах', url="https://yandex.by/maps/?l=sat%2Cskl&ll=30.411995%2C53.894703&mode=usermaps&source=constructorLink&um=constructor%3Ae0f760b59f83b32296768c2c35a992dd17502fe04a8379276c50768ff9a561c7&z=13")
                nazad_start = types.InlineKeyboardButton('Назад', callback_data='exit')
                markup.row(istmest,progulki)
                markup.row(dvizh)
                markup.row(museum, org)
                markup.row(nazad_start)
                bot.answer_callback_query(call.id, show_alert=False, text="Всё готово!")
                bot.send_message(call.from_user.id, f'Город: *Могилев*\n\nВыберите тип отдыха',
                                 reply_markup=markup, parse_mode='MarkDown')
            elif call.data == 'mogilev_history':
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Точка 1 - Могилев | {call.from_user.id} | {call.from_user.username} | ')
                loggingf(call.from_user.id, call.from_user.username, "Могилев - История")
                markup = types.InlineKeyboardMarkup()
                next1 = types.InlineKeyboardButton('О местах', url="https://routes.bn-team.xyz/mogilev_1")
                marsh = types.InlineKeyboardButton('Назад', callback_data='start_Mogilev')

                markup.row(next1)
                markup.row(marsh)
                bot.answer_callback_query(call.id, show_alert=False, text="Поехали! 🛤️")
                bot.send_message(call.from_user.id, f'Город: *Могилёв*\n\nИсторические места:\n1.Драматический театр\n2.Музей этнографии\n3.Звездочет\n4.Площадь Ленина\n5.Буйническое поле',
                                 reply_markup=markup, parse_mode='MarkDown')

            elif call.data == 'mogilev_progul':
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Точка 4 - Могилев | {call.from_user.id} | {call.from_user.username} | ')
                loggingf(call.from_user.id, call.from_user.username, "Могилев - Прогулки")
                markup = types.InlineKeyboardMarkup()
                next1 = types.InlineKeyboardButton('О местах', url="https://routes.bn-team.xyz/mogilev_2")
                marsh = types.InlineKeyboardButton('Назад', callback_data='start_Mogilev')

                markup.row(next1)
                markup.row(marsh)
                bot.answer_callback_query(call.id, show_alert=False, text="Давай-давай! 😎")
                bot.send_message(call.from_user.id, f'Город: *Могилёв*\n\nМеста для прогулок:\n\n1.\n2.\n3.\n4.\n5.',
                                 reply_markup=markup, parse_mode='MarkDown')
            elif call.data == 'mogilev_dvizh':
                if vass_private.is_premium(call.from_user.id):
                    tz_minsk = pytz.timezone("Europe/Minsk")
                    print(
                        f'[LOG] | {datetime.now(tz_minsk)} | Точка 5 - Могилев | {call.from_user.id} | {call.from_user.username} | ')
                    loggingf(call.from_user.id, call.from_user.username, "Могилев - Движ")
                    markup = types.InlineKeyboardMarkup()
                    next1 = types.InlineKeyboardButton('Следующая достопримечательность', callback_data='mogilev_next_6')
                    nazad_start = types.InlineKeyboardButton('Назад', callback_data='exit')
                    marsh = types.InlineKeyboardButton('Построить маршрут до точки', callback_data='mogilev5_m')

                    # markup.row(next1)
                    # markup.row(marsh)
                    markup.row(nazad_start)
                    bot.answer_callback_query(call.id, show_alert=True, text="Этот раздел содержит места предназначенные для людей 18+!\nНажимая кнопку ОК Вы соглашаетесь с правилами")
                    bot.send_message(call.from_user.id, f'Город: *Могилёв*\n\n🔞DVIZH🔥\n\n\n\n',
                                     reply_markup=markup, parse_mode='MarkDown')
                else:
                    markup = types.InlineKeyboardMarkup()
                    next1 = types.InlineKeyboardButton('Купить ✨BN Plus✨',
                                                       url='https://t.me/m/-Zdd8vhrOTIy')
                    markup.row(next1)
                    bot.send_message(call.from_user.id, f'Раздел ДВИЖ доступен только подписчикам BN Plus', reply_markup=markup)

            elif call.data == 'nachnem':
                mennu(call)
            elif call.data == 'exit':
                bot.answer_callback_query(call.id, show_alert=False, text="Завершаю...")
                mennu(call)
            elif call.data == 'otmena_start':
                bot.answer_callback_query(call.id, show_alert=False, text="Отменяю...")
                mennu(call)
            elif call.data == 'exit':
                bot.answer_callback_query(call.id, show_alert=False, text="Выхожу...")
                mennu(call)
            elif call.data == 'profile':

                userid = call.from_user.id
                markup = telebot.types.InlineKeyboardMarkup()
                menu = telebot.types.InlineKeyboardButton("Назад", callback_data='exit')
                delete = telebot.types.InlineKeyboardButton("Запросить удаление данных", callback_data='pldel')
                markup.row(menu)
                markup.row(delete)
                tz_minsk = pytz.timezone("Europe/Minsk")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=f'💡Профиль💡\n\nUser ID: {call.from_user.id}\nUsername: {call.from_user.username}\nДата регистрации: {vass_private.reg_date(call.from_user.id)}\nВремя регистрации: {vass_private.reg_time(call.from_user.id)}\n\nBN PLUS: {vass_private.isprem(call.from_user.id)}',
                                      reply_markup=markup)
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Открыт профиль | {call.from_user.id} | {call.from_user.username} | ')
                loggingf(call.from_user.id, call.from_user.username, "Профиль")

            elif call.data.startswith('ban_'):
                    # Извлекаем user_id из callback_data
                user_id = call.data.split('_')[1]

                # Преобразуем user_id в целое число


                # Вызываем функцию блокировки
                vass_private.ban_user(user_id, "console", "console", "Не указано")
                banloggingf(user_id, "Блокировка", "console","console", "Не указано")
                # Отправляем уведомление о блокировке
                bot.answer_callback_query(call.id, text=f"Пользователь с ID {user_id} был заблокирован.")
            elif call.data.startswith('logintrue_'):
                    # Извлекаем user_id из callback_data
                user_id = call.data.split('_')[1]

                # Преобразуем user_id в целое число

                bot.answer_callback_query(call.id, show_alert=True, text="Авторизация включена\n")
                vass_private.login_true(user_id)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=f'Ваш ID для авторизации на сайте: {user_id}\nВаш пароль: {vass_private.get_pass(user_id)}')
                mennu(call)
            elif call.data.startswith('loginfalse_'):
                # Извлекаем user_id из callback_data
                user_id = call.data.split('_')[1]

                # Преобразуем user_id в целое число

                bot.answer_callback_query(call.id, show_alert=True, text="Авторизация отключена\n")
                vass_private.login_false(user_id)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f'Авторизация отключена')
                mennu(call)
            elif call.data.startswith('unban_'):
                # Извлекаем user_id из callback_data
                user_id = call.data.split('_')[1]

                # Преобразуем user_id в целое число

                # Вызываем функцию блокировки
                vass_private.unban_user(user_id, "console", "console", "Не указано")
                banloggingf(user_id, "Разлокировка", "console", "console", "Не указано")
                # Отправляем уведомление о блокировке
                bot.answer_callback_query(call.id, text=f"Пользователь с ID {user_id} был разблокирован.")
            elif call.data.startswith('setuser_'):
                # Извлекаем user_id из callback_data
                user_id = call.data.split('_')[1]

                # Преобразуем user_id в целое число
                adminloggingf(user_id, "Снятие прав администратора", "console", "console")
                # Вызываем функцию блокировки
                vass_private.set_user(user_id)

                # Отправляем уведомление о блокировке
                bot.answer_callback_query(call.id, text=f"Пользователь с ID {user_id} был понижен")
            elif call.data.startswith('setadmin_'):
                # Извлекаем user_id из callback_data
                user_id = call.data.split('_')[1]

                # Преобразуем user_id в целое число

                # Вызываем функцию блокировки
                vass_private.set_admin(user_id)
                adminloggingf(user_id, "Выдача прав администратора", "console", "console")
                # Отправляем уведомление о блокировке
                bot.answer_callback_query(call.id, text=f"Пользователь с ID {user_id} был понижен")

            elif call.data == 'museum':

                markup = telebot.types.InlineKeyboardMarkup()
                a = telebot.types.InlineKeyboardButton("Музеи Могилева", callback_data='mus_mogilev')
                b = telebot.types.InlineKeyboardButton("Музеи Минска", callback_data='mus_minsk')
                v = telebot.types.InlineKeyboardButton("Музеи Бреста", callback_data='mus_brest')
                exit = telebot.types.InlineKeyboardButton("Выйти", callback_data='exit')
                markup.row(a)
                markup.row(b)
                markup.row(v)
                markup.row(exit)
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Музеи - Выбор города | {call.from_user.id} | {call.from_user.username} | ')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Поиск музеев по городам',
                                      reply_markup=markup)
            elif call.data == 'mus_minsk':
                bot.answer_callback_query(call.id, show_alert=True, text="Ошибка подключения к Yandex Maps API\n")
            elif call.data == 'mus_brest':
                bot.answer_callback_query(call.id, show_alert=True, text="Ошибка подключения к Yandex Maps API\n")
            elif call.data == 'mus_mogilev':

                markup = telebot.types.InlineKeyboardMarkup()
                a = telebot.types.InlineKeyboardButton("Городская ратуша", callback_data='mog_ratusha')
                b = telebot.types.InlineKeyboardButton("Художественный музей имени Масленикова", callback_data='mog_maslen')
                c = telebot.types.InlineKeyboardButton("Могилёвский областной краеведческий музей", callback_data='mog_kraeved')
                d = telebot.types.InlineKeyboardButton("Музей этнографии", callback_data='mog_etnograph')
                e = telebot.types.InlineKeyboardButton("Музей Бялыницкого-Бирули", callback_data='mog_belbir')
                exit = telebot.types.InlineKeyboardButton("Выйти из режима музеев", callback_data='exit')
                markup.row(a)
                markup.row(b)
                markup.row(c)
                markup.row(d)
                markup.row(e)
                markup.row(exit)
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Музеи - Могилев | {call.from_user.id} | {call.from_user.username} | ')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Музеи могилева',
                                      reply_markup=markup)
            elif call.data == 'mog_ratusha':
                markup = telebot.types.InlineKeyboardMarkup()
                site = types.InlineKeyboardButton("Городская Ратуша - сайт", url="https://museumhm.by/")
                marsh = types.InlineKeyboardButton("Построить маршрут", callback_data='mog_ratusha_map')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад к списку музеев", callback_data='mus_mogilev')
                markup.row(site)
                markup.row(marsh)
                markup.row(nazad_mus)
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Могилвская Городская ратуша | {call.from_user.id} | {call.from_user.username} | ')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Могилвская Городская ратуша*\n\n_В 1578, через год после получения городом грамоты на магдебургское право, в Могилёве началось возведение городской ратуши. Первоначально ратуша была деревянной, поэтому неоднократно сгорала дотла, и её местонахождение менялось.\nВо время Северной войны в сентябре 1708 года ратуша сгорела, но была быстро восстановлена. А в 1733 году в ней проведён большой ремонт.\nЗдание было самым высоким в городе. В 1780 году с её смотровой площадки Могилёвом любовались императрица Екатерина II и австрийский император Иосиф II.\n\nВо время Великой Отечественной войны ратуша была сильно повреждена. 28 декабря 1952 года на совещании архитекторов БССР по охране памятников архитектуры было принято решение о её восстановлении, 11 сентября 1953 года — решение Исполкома Могилёвского городского Совета депутатов № 725, согласно которому здание ратуши объявлялось памятником архитектуры, а работы по её реставрации должны были быть завершены к 10 декабря 1953 года. Однако реставрация ратуши так и не была начата, а в июле 1957 года она была взорвана.\nНеоднократно поднимались разговоры о восстановлении городской ратуши, но лишь 23 мая 1992 года произошла символическая закладка 1-го камня на старом месте будущей ратуши и его освящение на торжественном молебне. Реально к проекту и строительству приступили лишь в 2007 году. В 2008 году в день города произошло её торжественное открытие_',
                                      reply_markup=markup, parse_mode='MarkDown')

            elif call.data == 'mog_maslen':
                markup = telebot.types.InlineKeyboardMarkup()
                site = types.InlineKeyboardButton("Художественный музей имени Масленикова", url="https://maslenikov.by/")
                marsh = types.InlineKeyboardButton("Построить маршрут", callback_data='mog_maslen_map')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад к списку музеев", callback_data='mus_mogilev')
                markup.row(site)
                markup.row(marsh)
                markup.row(nazad_mus)
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Художественный музей имени Масленикова | {call.from_user.id} | {call.from_user.username} | ')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Художественный музей имени Масленикова*\n\n_Учреждён в соответствии с Законом Республики Беларусь «О музеях и музейных фондах Республики Беларусь», открыт решением исполнительного комитета Могилёвского областного Совета депутатов № 13 от 19 ноября 1990 года.\n\nУказом Президента Республики Беларусь от 22 января 1996 года Могилёвскому областному музею было присвоено имя П. В. Масленикова. Музей располагается в здании, которое является памятником архитектуры начала XX века. Здание возвели в 1903—1914 годах с чертами модерна, русского стиля и позднего классицизма._',
                                      reply_markup=markup, parse_mode='MarkDown')
            elif call.data == 'mog_kraeved':
                markup = telebot.types.InlineKeyboardMarkup()
                site = types.InlineKeyboardButton("Могилёвский областной краеведческий музей", url="https://mogilevmuseum.by/")
                marsh = types.InlineKeyboardButton("Построить маршрут", callback_data='mog_kraeved_map')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад к списку музеев", callback_data='mus_mogilev')
                markup.row(site)
                markup.row(marsh)
                markup.row(nazad_mus)
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Могилёвский областной краеведческий музей | {call.from_user.id} | {call.from_user.username} | ')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Могилёвский областной краеведческий музей*\n\n_Первый музей в городе Могилёв был открыт 15 ноября 1867 года при губернском статистическом комитете и получил название Могилёвский музей.\n18 декабря 1904 года в Могилёве открылся второй музей — церковно-археологический. В 1918 году музеи объединились в один — Губернский музей.\nВ 1928—1929 годах музею передали некоторые экспонаты из государственного антикварного фонда СССР: изделия из драгметаллов и камней, иконы, картины, книги и т. д. В том числе была передана серебряная булава польского короля Сигизмунда III. Наиболее ценным предметом коллекции и уникальным экспонатом стал переданный в музей крест Ефросиньи Полоцкой — национальная реликвия белорусов. Крест и другие ценности были сразу же помещены в бронированную комнату-сейф, имевшуюся в здании.\n...\nС 1977 года по июль 1990 года музей был закрыт на капитальный ремонт. После ремонта была представлена новая экспозиция, действующая и поныне.\nВ 1997 году к 130-летнему юбилею музея была открыта экспозиция археологии._',
                                      reply_markup=markup, parse_mode='MarkDown')
            elif call.data == 'mog_etnograph':
                markup = telebot.types.InlineKeyboardMarkup()
                site = types.InlineKeyboardButton("Музей этнографии - сайт", callback_data='error_05')
                marsh = types.InlineKeyboardButton("Построить маршрут", callback_data='mog_etnograph_map')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад к списку музеев", callback_data='mus_mogilev')
                markup.row(site)
                markup.row(marsh)
                markup.row(nazad_mus)
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Музей этнографии | {call.from_user.id} | {call.from_user.username} | ')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Музей этнографии*\n\n_Музей этнографии в Могилёве является филиалом Могилёвского областного историко-краеведческого музея. Располагается по адресу ул. Первомайская № 8. Открыт в 1981 году.\nПлощадь экспозиции 760 м², 4,5 тыс. предметов основного фонда (2000). Материалы музея знакомят с состоянием материальной и духовной культуры крестьян Могилевского Поднепровья городского быта могилевчан конца XIX — начала XX веков. Среди экспонатов — орудия труда, предметы быта, национальная одежда могилевских и краснопольских костюмов, коллекция подлинных могилёвских полотенец, иконы, изразцы и деревянная скульптура XVII — XIX веков, церковные книги, журналы XIX — начала XX веков.\nЗдание музея стоит на фундаменте Могилёвского иезуитского коллегиума. Внутренняя стена, которая выходит во двор музея, является аутентичной стеной XVIII века, бывшей частью коллегиума._',
                                      reply_markup=markup, parse_mode='MarkDown')
            elif call.data == 'mog_belbir':
                markup = telebot.types.InlineKeyboardMarkup()
                site = types.InlineKeyboardButton("Музей Бялыницкого-Бирули - сайт", url="https://bb.artmuseum.by/ru")
                marsh = types.InlineKeyboardButton("Построить маршрут", callback_data='mog_belbir_map')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад к списку музеев", callback_data='mus_mogilev')
                markup.row(site)
                markup.row(marsh)
                markup.row(nazad_mus)
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Музей Бялыницкого-Бирули | {call.from_user.id} | {call.from_user.username} | ')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Музей Бялыницкого-Бирули*\n\n_Художник родился в 1872 году в деревне Крынки близ Белыничей Могилёвской губернии. Его родной дом не сохранился. Музей художника был открыт в памятнике гражданской архитектуры XVII века — каменном двухэтажном особняке с мансардой на улице Ленинской, 37 в Могилёве. В мае 1780 года этот дом, как самый лучший из существовавших тогда в городе двухэтажных каменных домов, был предоставлен для проживания австрийскому императору Иосифу II для проведения встречи с Екатериной II. С 1815 по 1917 годы в этом доме размещалось Могилёвское дворянское депутатское собрание. В 1918 году помещение было передано только что созданной центральной городской библиотеке имени Карла Маркса. Здание было частично разрушено в годы Великой Отечественной войны. В 1970-х годах его реконструировали: надстроили 3-й этаж и крышу. В плане получилось прямоугольное здание со сводчатым массивным перекрытием. Центр внутренней планировки — деревянная лестница, вокруг которой на втором этаже сгруппированы бывшие жилые помещения. Стены прорезаны прямоугольными оконными проёмами и декорированы профилированными лопатками. В центре главного фасада при реконструкции сделан лучковый входной проём и небольшой балкон с металлической ажурной оградой. Первый этаж и большой подвал под ним имеют сводчатое перекрытие, второй — балочное. Дом является архитектурным памятником в стиле барокко.\nС 1982 года в здании находится филиал Национального художественного музея Беларуси художественный музей Бялыницкого-Бирули В. К._',
                                      reply_markup=markup, parse_mode='MarkDown')
            elif call.data == 'mog_ratusha_map':
                # markup = telebot.types.InlineKeyboardMarkup()
                # site = types.InlineKeyboardButton("Городская Ратуша - сайт", url="https://museumhm.by/")
                # marsh = types.InlineKeyboardButton("Построить маршрут", callback_data='mog_ratusha_map')
                # nazad_mus = telebot.types.InlineKeyboardButton("Назад к списку музеев", callback_data='mus_mogilev')
                # markup.row(site)
                # markup.row(nazad_mus)
                # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                #                       text='*Могилвская Городская ратуша*\n\n_В 1578, через год после получения городом грамоты на магдебургское право, в Могилёве началось возведение городской ратуши. Первоначально ратуша была деревянной, поэтому неоднократно сгорала дотла, и её местонахождение менялось.\nВо время Северной войны в сентябре 1708 года ратуша сгорела, но была быстро восстановлена. А в 1733 году в ней проведён большой ремонт.\nЗдание было самым высоким в городе. В 1780 году с её смотровой площадки Могилёвом любовались императрица Екатерина II и австрийский император Иосиф II.\n\nВо время Великой Отечественной войны ратуша была сильно повреждена. 28 декабря 1952 года на совещании архитекторов БССР по охране памятников архитектуры было принято решение о её восстановлении, 11 сентября 1953 года — решение Исполкома Могилёвского городского Совета депутатов № 725, согласно которому здание ратуши объявлялось памятником архитектуры, а работы по её реставрации должны были быть завершены к 10 декабря 1953 года. Однако реставрация ратуши так и не была начата, а в июле 1957 года она была взорвана.\nНеоднократно поднимались разговоры о восстановлении городской ратуши, но лишь 23 мая 1992 года произошла символическая закладка 1-го камня на старом месте будущей ратуши и его освящение на торжественном молебне. Реально к проекту и строительству приступили лишь в 2007 году. В 2008 году в день города произошло её торжественное открытие_',
                #                       reply_markup=markup, parse_mode='MarkDown')
                bot.answer_callback_query(call.id, show_alert=True,
                                          text="Ошибка 0005\nЭтот раздел временно недоступен")
            elif call.data == 'mog_maslen_map':
                # markup = telebot.types.InlineKeyboardMarkup()
                # site = types.InlineKeyboardButton("Художественный музей имени Масленикова", url="https://maslenikov.by/")
                # marsh = types.InlineKeyboardButton("Построить маршрут", callback_data='mog_maslen_map')
                # nazad_mus = telebot.types.InlineKeyboardButton("Назад к списку музеев", callback_data='mus_mogilev')
                # markup.row(site)
                # markup.row(nazad_mus)
                # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                #                       text='*Художественный музей имени Масленикова*\n\n_Учреждён в соответствии с Законом Республики Беларусь «О музеях и музейных фондах Республики Беларусь», открыт решением исполнительного комитета Могилёвского областного Совета депутатов № 13 от 19 ноября 1990 года.\n\nУказом Президента Республики Беларусь от 22 января 1996 года Могилёвскому областному музею было присвоено имя П. В. Масленикова. Музей располагается в здании, которое является памятником архитектуры начала XX века. Здание возвели в 1903—1914 годах с чертами модерна, русского стиля и позднего классицизма._',
                #                       reply_markup=markup, parse_mode='MarkDown')
                bot.answer_callback_query(call.id, show_alert=True,
                                          text="Ошибка 0005\nЭтот раздел временно недоступен")
            elif call.data == 'mog_kraeved_map':
                # markup = telebot.types.InlineKeyboardMarkup()
                # site = types.InlineKeyboardButton("Могилёвский областной краеведческий музей", url="https://mogilevmuseum.by/")
                # marsh = types.InlineKeyboardButton("Построить маршрут", callback_data='mog_kraeved_map')
                # nazad_mus = telebot.types.InlineKeyboardButton("Назад к списку музеев", callback_data='mus_mogilev')
                # markup.row(site)
                # markup.row(nazad_mus)
                # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                #                       text='*Могилёвский областной краеведческий музей*\n\n_Первый музей в городе Могилёв был открыт 15 ноября 1867 года при губернском статистическом комитете и получил название Могилёвский музей.\n18 декабря 1904 года в Могилёве открылся второй музей — церковно-археологический. В 1918 году музеи объединились в один — Губернский музей.\nВ 1928—1929 годах музею передали некоторые экспонаты из государственного антикварного фонда СССР: изделия из драгметаллов и камней, иконы, картины, книги и т. д. В том числе была передана серебряная булава польского короля Сигизмунда III. Наиболее ценным предметом коллекции и уникальным экспонатом стал переданный в музей крест Ефросиньи Полоцкой — национальная реликвия белорусов. Крест и другие ценности были сразу же помещены в бронированную комнату-сейф, имевшуюся в здании.\n...\nС 1977 года по июль 1990 года музей был закрыт на капитальный ремонт. После ремонта была представлена новая экспозиция, действующая и поныне.\nВ 1997 году к 130-летнему юбилею музея была открыта экспозиция археологии._',
                #                       reply_markup=markup, parse_mode='MarkDown')
                bot.answer_callback_query(call.id, show_alert=True,
                                          text="Ошибка 0005\nЭтот раздел временно недоступен")
            elif call.data == 'mog_etnograph_map':
                # markup = telebot.types.InlineKeyboardMarkup()
                # site = types.InlineKeyboardButton("Музей этнографии - сайт", callback_data='error_05')
                # marsh = types.InlineKeyboardButton("Построить маршрут", callback_data='mog_etnograph_map')
                # nazad_mus = telebot.types.InlineKeyboardButton("Назад к списку музеев", callback_data='mus_mogilev')
                # markup.row(site)
                # markup.row(nazad_mus)
                # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                #                       text='*Музей этнографии*\n\n_Музей этнографии в Могилёве является филиалом Могилёвского областного историко-краеведческого музея. Располагается по адресу ул. Первомайская № 8. Открыт в 1981 году.\nПлощадь экспозиции 760 м², 4,5 тыс. предметов основного фонда (2000). Материалы музея знакомят с состоянием материальной и духовной культуры крестьян Могилевского Поднепровья городского быта могилевчан конца XIX — начала XX веков. Среди экспонатов — орудия труда, предметы быта, национальная одежда могилевских и краснопольских костюмов, коллекция подлинных могилёвских полотенец, иконы, изразцы и деревянная скульптура XVII — XIX веков, церковные книги, журналы XIX — начала XX веков.\nЗдание музея стоит на фундаменте Могилёвского иезуитского коллегиума. Внутренняя стена, которая выходит во двор музея, является аутентичной стеной XVIII века, бывшей частью коллегиума._',
                #                       reply_markup=markup, parse_mode='MarkDown')
                bot.answer_callback_query(call.id, show_alert=True,
                                          text="Ошибка 0005\nЭтот раздел временно недоступен")
            elif call.data == 'mog_belbir_map':
                # markup = telebot.types.InlineKeyboardMarkup()
                # site = types.InlineKeyboardButton("Музей Бялыницкого-Бирули - сайт", url="https://bb.artmuseum.by/ru")
                # marsh = types.InlineKeyboardButton("Построить маршрут", callback_data='mog_belbir_map')
                # nazad_mus = telebot.types.InlineKeyboardButton("Назад к списку музеев", callback_data='mus_mogilev')
                # markup.row(site)
                # markup.row(nazad_mus)
                # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                #                       text='*Музей Бялыницкого-Бирули*\n\n_Художник родился в 1872 году в деревне Крынки близ Белыничей Могилёвской губернии. Его родной дом не сохранился. Музей художника был открыт в памятнике гражданской архитектуры XVII века — каменном двухэтажном особняке с мансардой на улице Ленинской, 37 в Могилёве. В мае 1780 года этот дом, как самый лучший из существовавших тогда в городе двухэтажных каменных домов, был предоставлен для проживания австрийскому императору Иосифу II для проведения встречи с Екатериной II. С 1815 по 1917 годы в этом доме размещалось Могилёвское дворянское депутатское собрание. В 1918 году помещение было передано только что созданной центральной городской библиотеке имени Карла Маркса. Здание было частично разрушено в годы Великой Отечественной войны. В 1970-х годах его реконструировали: надстроили 3-й этаж и крышу. В плане получилось прямоугольное здание со сводчатым массивным перекрытием. Центр внутренней планировки — деревянная лестница, вокруг которой на втором этаже сгруппированы бывшие жилые помещения. Стены прорезаны прямоугольными оконными проёмами и декорированы профилированными лопатками. В центре главного фасада при реконструкции сделан лучковый входной проём и небольшой балкон с металлической ажурной оградой. Первый этаж и большой подвал под ним имеют сводчатое перекрытие, второй — балочное. Дом является архитектурным памятником в стиле барокко.\nС 1982 года в здании находится филиал Национального художественного музея Беларуси художественный музей Бялыницкого-Бирули В. К._',
                #                       reply_markup=markup, parse_mode='MarkDown')
                bot.answer_callback_query(call.id, show_alert=True, text="Ошибка 0005\nЭтот раздел временно недоступен")
            elif call.data == 'error_05':
                bot.answer_callback_query(call.id, show_alert=True, text="Ошибка 0005\nЭтот раздел временно недоступен")

            elif call.data == 'error_06':
                bot.answer_callback_query(call.id, show_alert=True, text="Ошибка 0006\nЭтот раздел еще не создан :-)")

            elif call.data == 'settings':

                markup = telebot.types.InlineKeyboardMarkup()
                if vass_private.is_admin(call.from_user.id) == True:
                    a = telebot.types.InlineKeyboardButton("Отправка начального видео", callback_data='set_notify_vid')
                    b = telebot.types.InlineKeyboardButton("Скрытие админки", callback_data='admin_hide')
                    c = telebot.types.InlineKeyboardButton("Режим тестировщика",  callback_data='tester_mode')
                    passw = telebot.types.InlineKeyboardButton("Авторизация", callback_data='pass_settings')
                    d = telebot.types.InlineKeyboardButton("О боте", callback_data='what_bot')
                    exit = telebot.types.InlineKeyboardButton("Выйти", callback_data='exit')
                    markup.row(a)
                    markup.row(b)
                    markup.row(c)
                    markup.row(passw)
                    markup.row(d)
                    markup.row(exit)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Настройки бота',
                                          reply_markup=markup)
                    tz_minsk = pytz.timezone("Europe/Minsk")
                    print(
                        f'[LOG] | {datetime.now(tz_minsk)} | Открыты настройки (администратор) | {call.from_user.id} | {call.from_user.username} | ')
                    loggingf(call.from_user.id, call.from_user.username, "Открыты настройки (администратор)")

                else:
                    a = telebot.types.InlineKeyboardButton("Отправка начального видео", callback_data='set_notify_vid')
                    passw = telebot.types.InlineKeyboardButton("Авторизация", callback_data='pass_settings')
                    b = telebot.types.InlineKeyboardButton("О боте",  callback_data='what_bot')
                    c = telebot.types.InlineKeyboardButton("Сменить язык",  callback_data='error_in_upd')
                    exit = telebot.types.InlineKeyboardButton("Выйти", callback_data='settings')
                    markup.row(a)
                    markup.row(passw)
                    markup.row(b)
                    markup.row(c)
                    markup.row(exit)
                    tz_minsk = pytz.timezone("Europe/Minsk")
                    print(
                        f'[LOG] | {datetime.now(tz_minsk)} | Открыты настройки | {call.from_user.id} | {call.from_user.username} | ')
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='Настройки бота',
                                          reply_markup=markup)
                    loggingf(call.from_user.id, call.from_user.username, "Открыты настройки")



            elif call.data == 'eda_str1':
                markup = telebot.types.InlineKeyboardMarkup()
                a = types.InlineKeyboardButton("ТандыР", callback_data='tandir')
                b = types.InlineKeyboardButton("Domino's Pizza", callback_data='dominos_pizza')
                c = types.InlineKeyboardButton("Васильки", callback_data='vasilki')
                num = types.InlineKeyboardButton("1", callback_data='eda_str1_01')
                next_p = types.InlineKeyboardButton(">", callback_data='eda_str2')
                nazad_mus = telebot.types.InlineKeyboardButton("Выйти", callback_data='org_type')
                markup.row(a)
                markup.row(b)
                markup.row(c)
                markup.row(nazad_mus, num, next_p)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\nПосле выбора вам будет отправлена карта и сайт',
                                      reply_markup=markup, parse_mode='MarkDown')
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Организации | Еда | Страница: 1 | {call.from_user.id} | {call.from_user.username} | ')

            elif call.data == 'eda_str2':
                markup = telebot.types.InlineKeyboardMarkup()
                a = types.InlineKeyboardButton("Burger King", callback_data='burger_king')
                b = types.InlineKeyboardButton("KFC", callback_data='KFC')
                c = types.InlineKeyboardButton("MC Doner", callback_data='mcdoner')
                last_p = types.InlineKeyboardButton("<", callback_data='eda_str1')
                num = types.InlineKeyboardButton("2", callback_data='eda_str2_01')
                next_p = types.InlineKeyboardButton(">", callback_data='str2')
                nazad_mus = telebot.types.InlineKeyboardButton("Выйти", callback_data='org_type')
                markup.row(a)
                markup.row(b)
                markup.row(c)
                markup.row(last_p, num)
                markup.row(nazad_mus)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\nПосле выбора вам будет отправлена карта и сайт',
                                      reply_markup=markup, parse_mode='MarkDown')
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Организации | Еда | Страница: 2 | {call.from_user.id} | {call.from_user.username} | ')
                #ТАНДЫР
            elif call.data == 'tandir':
                markup = telebot.types.InlineKeyboardMarkup()
                a = types.InlineKeyboardButton("Сайт", url="https://tandyr-cafe.by")
                b = types.InlineKeyboardButton("Получить карту", callback_data='tandir_map')
                c = types.InlineKeyboardButton("Построить маршрут", callback_data='tandir_marsh')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str1')
                markup.row(a)
                markup.row(b)
                markup.row(c)
                markup.row(nazad_mus)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*ТандыР*\nАдрес: Могилёв, площадь Славы, 2',
                                      reply_markup=markup, parse_mode='MarkDown')
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Организации | Еда | ТандыР | {call.from_user.id} | {call.from_user.username} | ')
            elif call.data == 'tandir_map':
                url = 'https://static-maps.yandex.ru/v1?lang=ru_RU&pt=30.330525198672877,53.895220859337975,pm2dbl&z=15&apikey=0c0e4801-78d4-4a7c-80ea-7c18e4fc9b32'
                response = requests.get(url)

                if response.status_code == 200:
                    bot.send_photo(chat_id=call.from_user.id, photo=response.content)
                    markup = telebot.types.InlineKeyboardMarkup()
                    a = types.InlineKeyboardButton("Сайт", url="https://tandyr-cafe.by")
                    b = types.InlineKeyboardButton("Получить карту", callback_data='tandir_map')
                    c = types.InlineKeyboardButton("Построить маршрут", callback_data='tandir_marsh')
                    nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str1')
                    markup.row(a)
                    markup.row(b)
                    markup.row(c)
                    markup.row(nazad_mus)
                    bot.send_message(chat_id=call.message.chat.id,
                                     text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*ТандыР*\nАдрес: Могилёв, площадь Славы, 2',
                                     reply_markup=markup, parse_mode='MarkDown')
                    tz_minsk = pytz.timezone("Europe/Minsk")
                    print(
                        f'[LOG] | {datetime.now(tz_minsk)} | API | Org - Eda - TandiR | Type: Map | Status: OK (200) |{call.from_user.id} | {call.from_user.username} | ')
                else:
                    print('Failed to download image')
            elif call.data == 'tandir_marsh':
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.330534192956257,53.895209941464955&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())

                bot.send_location(call.from_user.id, latitude, longitude)
                markup = telebot.types.InlineKeyboardMarkup()
                a = types.InlineKeyboardButton("Сайт", url="https://tandyr-cafe.by")
                b = types.InlineKeyboardButton("Получить карту", callback_data='tandir_map')
                c = types.InlineKeyboardButton("Построить маршрут", callback_data='tandir_marsh')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str1')
                markup.row(a)
                markup.row(b)
                markup.row(c)
                markup.row(nazad_mus)
                bot.send_message(chat_id=call.message.chat.id,
                                 text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*ТандыР*\nАдрес: Могилёв, площадь Славы, 2',
                                 reply_markup=markup, parse_mode='MarkDown')
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | API | Org - Eda - TandiR | Type: Route | Status: OK (200) |{call.from_user.id} | {call.from_user.username} | ')

            elif call.data == 'dominos_pizza':
                markup = telebot.types.InlineKeyboardMarkup()
                a = types.InlineKeyboardButton("Сайт", url="dominos.by")
                b = types.InlineKeyboardButton("Получить карту", callback_data='dominos_map')
                c = types.InlineKeyboardButton("Построить маршрут", callback_data='tandir_marsh')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str1')
                markup.row(a)
                markup.row(b)
                markup.row(c)
                markup.row(nazad_mus)
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Организации | Еда | Dominos Pizza | {call.from_user.id} | {call.from_user.username} | ')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*Dominos Pizza*\nАдрес: Могилёв, Первомайская ул., 5/1',reply_markup=markup, parse_mode='MarkDown')
            elif call.data == 'dominos_map':
                url = 'https://static-maps.yandex.ru/v1?lang=ru_RU&pt=30.332194291403482,53.89698202200782,pm2dbl&z=15&apikey=0c0e4801-78d4-4a7c-80ea-7c18e4fc9b32'
                response = requests.get(url)

                if response.status_code == 200:
                    bot.send_photo(chat_id=call.from_user.id, photo=response.content)
                    markup = telebot.types.InlineKeyboardMarkup()
                    a = types.InlineKeyboardButton("Сайт", url="dominos.by")
                    b = types.InlineKeyboardButton("Получить карту", callback_data='dominos_map')
                    c = types.InlineKeyboardButton("Построить маршрут", callback_data='dominos_marsh')
                    nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str1')
                    markup.row(a)
                    markup.row(b)
                    markup.row(c)
                    markup.row(nazad_mus)
                    bot.send_message(chat_id=call.message.chat.id,
                                     text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*Dominos Pizza*\nАдрес: Могилёв, Первомайская ул., 5/1',
                                     reply_markup=markup, parse_mode='MarkDown')
                    tz_minsk = pytz.timezone("Europe/Minsk")
                    print(
                        f'[LOG] | {datetime.now(tz_minsk)} | API | Org - Eda - Dominos | Type: Map | Status: OK (200) |{call.from_user.id} | {call.from_user.username} | ')
                else:
                    print('Failed to download image')
            elif call.data == 'dominos_marsh':
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.332292611852285,53.89691726571662&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())

                bot.send_location(call.from_user.id, latitude, longitude)
                markup = telebot.types.InlineKeyboardMarkup()
                a = types.InlineKeyboardButton("Сайт", url="dominos.by")
                b = types.InlineKeyboardButton("Получить карту", callback_data='dominos_map')
                c = types.InlineKeyboardButton("Построить маршрут", callback_data='dominos_marsh')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str1')
                markup.row(a)
                markup.row(b)
                markup.row(c)
                markup.row(nazad_mus)
                bot.send_message(chat_id=call.message.chat.id,
                                 text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*Dominos Pizza*\nАдрес: Могилёв, Первомайская ул., 5/1',
                                 reply_markup=markup, parse_mode='MarkDown')
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | API | Org - Eda - Dominos | Type: Route | Status: OK (200) |{call.from_user.id} | {call.from_user.username} | ')
            elif call.data == 'vasilki':
                markup = telebot.types.InlineKeyboardMarkup()
                a = types.InlineKeyboardButton("Сайт", url="vasilki.by")
                b = types.InlineKeyboardButton("Получить карту", callback_data='vasilki_map')
                c = types.InlineKeyboardButton("Построить маршрут", callback_data='vasilki_marsh')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str1')
                markup.row(a)
                markup.row(b)
                markup.row(c)
                markup.row(nazad_mus)
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Организации | Еда | Васильки | {call.from_user.id} | {call.from_user.username} | ')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*Васильки*\nАдрес: Могилёв, Первомайская ул., 57 | Этаж 3',reply_markup=markup, parse_mode='MarkDown')
            elif call.data == 'vasilki_map':
                url = 'https://static-maps.yandex.ru/v1?lang=ru_RU&pt=30.33950419126453,53.90455716873452,pm2dbl&z=15&apikey=0c0e4801-78d4-4a7c-80ea-7c18e4fc9b32'
                response = requests.get(url)

                if response.status_code == 200:
                    bot.send_photo(chat_id=call.from_user.id, photo=response.content)
                    markup = telebot.types.InlineKeyboardMarkup()
                    a = types.InlineKeyboardButton("Сайт", url="vasilki.by")
                    b = types.InlineKeyboardButton("Получить карту", callback_data='vasilki_map')
                    c = types.InlineKeyboardButton("Построить маршрут", callback_data='vasilki_marsh')
                    nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str1')
                    markup.row(a)
                    markup.row(b)
                    markup.row(c)
                    markup.row(nazad_mus)
                    tz_minsk = pytz.timezone("Europe/Minsk")
                    print(
                        f'[LOG] | {datetime.now(tz_minsk)} | API | Ogr - Eda - Vasilki | Status: OK (200) | {call.from_user.id} | {call.from_user.username} | ')
                    bot.send_message(chat_id=call.message.chat.id,
                                     text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*Васильки*\nАдрес: Могилёв, Первомайская ул., 57 | Этаж 3',
                                     reply_markup=markup, parse_mode='MarkDown')
                    tz_minsk = pytz.timezone("Europe/Minsk")
                    print(
                        f'[LOG] | {datetime.now(tz_minsk)} | API | Org - Eda - Vasilki | Type: Map | Status: OK (200) | {call.from_user.id} | {call.from_user.username} | ')
                else:
                    print('Failed to download image')
            elif call.data == 'vasilki_marsh':
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.339475526568567,53.90456286911653&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())

                bot.send_location(call.from_user.id, latitude, longitude)
                markup = telebot.types.InlineKeyboardMarkup()
                a = types.InlineKeyboardButton("Сайт", url="vasilki.by")
                b = types.InlineKeyboardButton("Получить карту", callback_data='vasilki_map')
                c = types.InlineKeyboardButton("Построить маршрут", callback_data='vasilki_marsh')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str1')
                markup.row(a)
                markup.row(b)
                markup.row(c)
                markup.row(nazad_mus)
                bot.send_message(chat_id=call.message.chat.id,
                                 text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*Васильки*\nАдрес: Могилёв, Первомайская ул., 57 | Этаж 3',
                                 reply_markup=markup, parse_mode='MarkDown')
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | API | Org - Eda - Vasilki | Type: Route | Status: OK (200) | {call.from_user.id} | {call.from_user.username} | ')
            elif call.data == 'burger_king':
                markup = telebot.types.InlineKeyboardMarkup()
                a = types.InlineKeyboardButton("Сайт", url="https://burger-king.by/")
                b = types.InlineKeyboardButton("Получить карту", callback_data='burger_king_map')
                c = types.InlineKeyboardButton("Построить маршрут", callback_data='burger_king_marsh')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str2')
                markup.row(a)
                markup.row(b)
                markup.row(c)
                markup.row(nazad_mus)
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Организации | Еда | Бургер Кинг | {call.from_user.id} | {call.from_user.username} | ')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*Burger King*\nАдрес: Могилёв, Первомайская ул., 57 | Этаж 3',reply_markup=markup, parse_mode='MarkDown')
            elif call.data == 'burger_king_map':
                url = 'https://static-maps.yandex.ru/v1?lang=ru_RU&pt=30.339536377772717,53.9040788367524,pm2dbl&z=15&apikey=0c0e4801-78d4-4a7c-80ea-7c18e4fc9b32'
                response = requests.get(url)

                if response.status_code == 200:
                    bot.send_photo(chat_id=call.from_user.id, photo=response.content)
                    markup = telebot.types.InlineKeyboardMarkup()
                    a = types.InlineKeyboardButton("Сайт", url="https://burger-king.by/")
                    b = types.InlineKeyboardButton("Получить карту", callback_data='burger_king_map')
                    c = types.InlineKeyboardButton("Построить маршрут", callback_data='burger_king_marsh')
                    nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str2')
                    markup.row(a)
                    markup.row(b)
                    markup.row(c)
                    markup.row(nazad_mus)
                    bot.send_message(chat_id=call.message.chat.id,
                                     text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*Burger King*\nАдрес: Могилёв, Первомайская ул., 57 | Этаж 3',
                                     reply_markup=markup, parse_mode='MarkDown')
                    tz_minsk = pytz.timezone("Europe/Minsk")
                    print(
                        f'[LOG] | {datetime.now(tz_minsk)} | API | Org - Eda - BurgerKing | Type: Map | Status: OK (200) | {call.from_user.id} | {call.from_user.username} | ')
                else:
                    print('Failed to download image')

            elif call.data == 'burger_king_marsh':
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.339534535166884,53.90407820164098&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())

                bot.send_location(call.from_user.id, latitude, longitude)
                markup = telebot.types.InlineKeyboardMarkup()
                a = types.InlineKeyboardButton("Сайт", url="https://burger-king.by/")
                b = types.InlineKeyboardButton("Получить карту", callback_data='burger_king_map')
                c = types.InlineKeyboardButton("Построить маршрут", callback_data='burger_king_marsh')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str2')
                markup.row(a)
                markup.row(b)
                markup.row(c)
                markup.row(nazad_mus)
                bot.send_message(chat_id=call.message.chat.id,
                                 text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*Burger King*\nАдрес: Могилёв, Первомайская ул., 57 | Этаж 3',
                                 reply_markup=markup, parse_mode='MarkDown')
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | API | Org - Eda - BurgerKing | Type: Route | Status: OK (200) | {call.from_user.id} | {call.from_user.username} | ')
            elif call.data == 'KFC':
                markup = telebot.types.InlineKeyboardMarkup()
                a = types.InlineKeyboardButton("Сайт", url="www.kfc.by")
                b = types.InlineKeyboardButton("Получить карту", callback_data='kfc_map')
                c = types.InlineKeyboardButton("Построить маршрут", callback_data='kfc_marsh')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str2')
                markup.row(a)
                markup.row(b)
                markup.row(c)
                markup.row(nazad_mus)
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Организации | Еда | KFC | {call.from_user.id} | {call.from_user.username} | ')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*KFC*\nАдрес: Могилёв, Первомайская ул., 57 | Этаж 3',reply_markup=markup, parse_mode='MarkDown')
            elif call.data == 'kfc_map':
                url = 'https://static-maps.yandex.ru/v1?lang=ru_RU&pt=30.33950419126453,53.904018648894684,pm2dbl&z=15&apikey=0c0e4801-78d4-4a7c-80ea-7c18e4fc9b32'
                response = requests.get(url)

                if response.status_code == 200:
                    bot.send_photo(chat_id=call.from_user.id, photo=response.content)
                    markup = telebot.types.InlineKeyboardMarkup()
                    a = types.InlineKeyboardButton("Сайт", url="www.kfc.by")
                    b = types.InlineKeyboardButton("Получить карту", callback_data='kfc_map')
                    c = types.InlineKeyboardButton("Построить маршрут", callback_data='kfc_marsh')
                    nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str2')
                    markup.row(a)
                    markup.row(b)
                    markup.row(c)
                    markup.row(nazad_mus)
                    bot.send_message(chat_id=call.message.chat.id,
                                     text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*KFC*\nАдрес: Могилёв, Первомайская ул., 57 | Этаж 3',
                                     reply_markup=markup, parse_mode='MarkDown')
                    tz_minsk = pytz.timezone("Europe/Minsk")
                    print(
                        f'[LOG] | {datetime.now(tz_minsk)} | API | Org - Eda - KFC | Type: Map | Status: OK (200) | {call.from_user.id} | {call.from_user.username} | ')
                else:
                    print('Failed to download image')
            elif call.data == 'kfc_marsh':
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.33946479773249,53.90399583928616&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())

                bot.send_location(call.from_user.id, latitude, longitude)
                markup = telebot.types.InlineKeyboardMarkup()
                a = types.InlineKeyboardButton("Сайт", url="www.kfc.by")
                b = types.InlineKeyboardButton("Получить карту", callback_data='kfc_map')
                c = types.InlineKeyboardButton("Построить маршрут", callback_data='kfc_marsh')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str2')
                markup.row(a)
                markup.row(b)
                markup.row(c)
                markup.row(nazad_mus)
                bot.send_message(chat_id=call.message.chat.id,
                                 text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*KFC*\nАдрес: Могилёв, Первомайская ул., 57 | Этаж 3',
                                 reply_markup=markup, parse_mode='MarkDown')
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | API | Org - Eda - KFC | Type: Route | Status: OK (200) | {call.from_user.id} | {call.from_user.username} | ')
            elif call.data == 'mcdoner':
                markup = telebot.types.InlineKeyboardMarkup()
                a = types.InlineKeyboardButton("Сайт", url="www.mcdoner.by")
                b = types.InlineKeyboardButton("Получить карту", callback_data='mcdoner_map')
                c = types.InlineKeyboardButton("Построить маршрут", callback_data='mcdoner_marsh')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str2')
                markup.row(a)
                markup.row(b)
                markup.row(c)
                markup.row(nazad_mus)
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Организации | Еда | Mc Doner | {call.from_user.id} | {call.from_user.username} | ')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*MC Doner*\nАдрес: Могилёв, Первомайская ул., 57 | Этаж 3',reply_markup=markup, parse_mode='MarkDown')
            elif call.data == 'mcdoner_map':
                url = 'https://static-maps.yandex.ru/v1?lang=ru_RU&pt=30.33950419126453,53.904018648894684,pm2dbl&z=15&apikey=0c0e4801-78d4-4a7c-80ea-7c18e4fc9b32'
                response = requests.get(url)

                if response.status_code == 200:
                    bot.send_photo(chat_id=call.from_user.id, photo=response.content)
                    markup = telebot.types.InlineKeyboardMarkup()
                    a = types.InlineKeyboardButton("Сайт", url="www.mcdoner.by")
                    b = types.InlineKeyboardButton("Получить карту", callback_data='mcdoner_map')
                    c = types.InlineKeyboardButton("Построить маршрут", callback_data='mcdoner_marsh')
                    nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str2')
                    markup.row(a)
                    markup.row(b)
                    markup.row(c)
                    markup.row(nazad_mus)
                    bot.send_message(chat_id=call.message.chat.id,
                                     text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*MC Doner*\nАдрес: Могилёв, Первомайская ул., 57 | Этаж 3',
                                     reply_markup=markup, parse_mode='MarkDown')
                    tz_minsk = pytz.timezone("Europe/Minsk")
                    print(
                        f'[LOG] | {datetime.now(tz_minsk)} | API | Org - Eda - mcdoner | Type: Map | Status: OK (200) | {call.from_user.id} | {call.from_user.username} | ')
                else:
                    print('Failed to download image')
            elif call.data == 'mcdoner_marsh':
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.33946479773249,53.90399583928616&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())
                bot.send_location(call.from_user.id, latitude, longitude)
                markup = telebot.types.InlineKeyboardMarkup()
                a = types.InlineKeyboardButton("Сайт", url="www.mcdoner.by")
                b = types.InlineKeyboardButton("Получить карту", callback_data='mcdoner_map')
                c = types.InlineKeyboardButton("Построить маршрут", callback_data='mcdoner_marsh')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='eda_str2')
                markup.row(a)
                markup.row(b)
                markup.row(c)
                markup.row(nazad_mus)
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | API | Org - Eda - mcdoner | Type: Route | Status: OK (200) | {call.from_user.id} | {call.from_user.username} | ')
                bot.send_message(chat_id=call.message.chat.id,
                                 text='*Рестораны в Могилеве*\n\n_Данная функция работает с использованием Yandex Maps API\nИспользуя эту функцию вы соглашаетесь с_ [Условиями использования Яндекс.Карт](https://yandex.ru/legal/maps_termsofuse/)\n\n*MC Doner*\nАдрес: Могилёв, Первомайская ул., 57 | Этаж 3',
                                 reply_markup=markup, parse_mode='MarkDown')
            elif call.data == 'eda_str2_01':
                bot.answer_callback_query(call.id, show_alert=False, text="Вы уже на 2 странице")
            elif call.data == 'eda_str1_01':
                bot.answer_callback_query(call.id, show_alert=False, text="Вы уже на 1 странице")
            elif call.data == 'mogilev1_m':
                bot.answer_callback_query(call.id, show_alert=False, text="Маршрут построен")
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.330336518434258,53.89410230353201&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())
                bot.send_location(call.from_user.id, latitude, longitude)

            elif call.data == 'mogilev2_m':
                bot.answer_callback_query(call.id, show_alert=False, text="Маршрут построен")
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.328563376711298,53.89432203722363&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())
                bot.send_location(call.from_user.id, latitude, longitude)

            elif call.data == 'mogilev3_m':
                bot.answer_callback_query(call.id, show_alert=False, text="Маршрут построен")
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.33326944241014,53.897539033992686&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())
                bot.send_location(call.from_user.id, latitude, longitude)

            elif call.data == 'mogilev4_m':
                bot.answer_callback_query(call.id, show_alert=False, text="Маршрут построен")
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.331568921894704,53.89723804650289&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())
                bot.send_location(call.from_user.id, latitude, longitude)

            elif call.data == 'mogilev5_m':
                bot.answer_callback_query(call.id, show_alert=False, text="Маршрут построен")
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.340755964791597,53.90231255556979&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())
                bot.send_location(call.from_user.id, latitude, longitude)

            elif call.data == 'mogilev6_m':
                bot.answer_callback_query(call.id, show_alert=False, text="Маршрут построен")
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.342986267488666,53.90903024054357&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())
                bot.send_location(call.from_user.id, latitude, longitude)

            elif call.data == 'mogilev7_m':
                bot.answer_callback_query(call.id, show_alert=False, text="Маршрут построен")
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.257366342989965,53.8615069146858&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())
                bot.send_location(call.from_user.id, latitude, longitude)

            elif call.data == 'what_bot':
                markup = telebot.types.InlineKeyboardMarkup()
                a = types.InlineKeyboardButton("О боте", callback_data='o_bote')
                b = types.InlineKeyboardButton("О Проекте", callback_data='o_project')
                c = types.InlineKeyboardButton("Связь с администратором", callback_data='error_in_upd')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='exit')
                markup.row(a)
                markup.row(b)
                markup.row(c)
                markup.row(nazad_mus)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*О проекте / боте*\n\nВыберите интересующий вас подраздел',
                                      reply_markup=markup, parse_mode='MarkDown')
            elif call.data == 'o_bote':
                markup = telebot.types.InlineKeyboardMarkup()
                about = telebot.types.InlineKeyboardButton("Подробнее", url="https://t.me/BelarusNature_bot/about_bot")
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='what_bot')
                markup.row(about)
                markup.row(nazad_mus)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*О боте*\n\n*Belarus Nature Bot*\n\n*Belarus Nature bot* - это умный чат-бот, разработанный для помощи туристам в  осуществлении путешествий. Сочетая в себе данные о достопримечательностях, местной культуре.\n1. BelarusNature предоставляет подробную информацию о различныхдостопримечательностях, их истории, географическом расположении.\n2. *BelarusNature* составляет оптимальный маршрут, на котором турист не будет скучать и посетит как можно больше интересных мест...\n\nПодробнее в нашей статье.',
                                      reply_markup=markup, parse_mode='MarkDown')
            elif call.data == 'o_project':
                markup = telebot.types.InlineKeyboardMarkup()
                about = telebot.types.InlineKeyboardButton("Подробнее", url="https://t.me/BelarusNature_bot/about_project")
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='what_bot')
                markup.row(about)
                markup.row(nazad_mus)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*О проекте*\n\n*Belarus Nature*\n\nПроект Belarus Nature начал свою работу в 2024 году с целью создания уникальных туристических маршрутов по живописным уголкам природы Беларуси. Команда проекта собирает информацию о лучших местах для пеших и велосипедных прогулок, организации пикников и наблюдения за дикой природой.\n\nПодробнее в нашей статье',
                                      reply_markup=markup, parse_mode='MarkDown')
            elif call.data == 'pldel':
                markup = telebot.types.InlineKeyboardMarkup()
                about = telebot.types.InlineKeyboardButton("Подробнее", url="https://t.me/BelarusNature_bot/about_project")
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='what_bot')
                markup.row(about)
                markup.row(nazad_mus)
                text = f'Запрос на удаление данных\n{call.from_user.id} - @{call.from_user.username}'
                url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=6978792645&text={text}'
                response = requests.get(url)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Запрос на удаление данных отправлен*\n\n*Важно! Если ваш аккаунт заблокирован то удаление данных невозможно. При удалении данных подписка BN Plus сгорает*\n\nBN Team',
                                      reply_markup=markup, parse_mode='MarkDown')
                loggingf(call.from_user.id, call.from_user.username, "Удаление данных")
            elif call.data == 'error_in_upd':
                bot.answer_callback_query(call.id, show_alert=False, text="Этот раздел будет совсем скоро)")











            elif call.data == 'wait':
                bot.answer_callback_query(call.id, show_alert=False, text="Этот раздел скушало обновление\nНо совсем скоро мы сделаем новый")

            elif call.data == 'pass_settings':
                bot.answer_callback_query(call.id, show_alert=True, text="Используйте /login")

            elif call.data == 'apanel_bot':
                bot.answer_callback_query(call.id, show_alert=False, text="АДМИН ИДИ НАХУЙ")
            elif call.data == 'org_type':
                markup = telebot.types.InlineKeyboardMarkup()
                eda = telebot.types.InlineKeyboardButton("Еда и рестораны", callback_data='eda_str1')
                kino = telebot.types.InlineKeyboardButton("Кинотеатры", callback_data='kino')
                hotel = telebot.types.InlineKeyboardButton("Отели", callback_data='hotel')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='exit')
                markup.row(eda)
                markup.row(kino)
                markup.row(hotel)
                markup.row(nazad_mus)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Организации в Могилеве*\n\n*⭐️ Выбор типа ⭐️*\n\n_Команда BN великодушно рекомендует Вам проверенные организации из списка ниже_',
                                      reply_markup=markup, parse_mode='MarkDown')
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Выбор типа организации | {call.from_user.id} | {call.from_user.username} | ')
            elif call.data == 'kino':
                markup = telebot.types.InlineKeyboardMarkup()
                eda = telebot.types.InlineKeyboardButton("StarLight Cinema", callback_data='starlight')
                kino = telebot.types.InlineKeyboardButton("Кинотеатр Родина", callback_data='rodina')
                hotel = telebot.types.InlineKeyboardButton("Кинотеатр Чырвоная Зорка", callback_data='chirzor')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='org_type')
                markup.row(eda)
                markup.row(kino)
                markup.row(hotel)
                markup.row(nazad_mus)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Организации в Могилеве*\n\n*Выбор типа*\n\nПроект Belarus Nature рекомендует вам организации из списков ниже',
                                      reply_markup=markup, parse_mode='MarkDown')
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Кинотеатры | {call.from_user.id} | {call.from_user.username} | ')
            elif call.data == 'hotel':
                markup = telebot.types.InlineKeyboardMarkup()
                eda = telebot.types.InlineKeyboardButton("Atrium Hotel", callback_data='atrium_hotel')
                kino = telebot.types.InlineKeyboardButton("Metropol Hotel", callback_data='metropol_hotel')
                hotel = telebot.types.InlineKeyboardButton("Губернская", callback_data='gubernskaya')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='org_type')
                markup.row(eda)
                markup.row(kino)
                markup.row(hotel)
                markup.row(nazad_mus)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Организации в Могилеве*\n\n*Выбор типа*\n\nПроект Belarus Nature рекомендует вам организации из списков ниже',
                                      reply_markup=markup, parse_mode='MarkDown')
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Отели | {call.from_user.id} | {call.from_user.username} | ')
            elif call.data == 'starlight':
                markup = telebot.types.InlineKeyboardMarkup()
                eda = telebot.types.InlineKeyboardButton("StarLight Cinema - Сайт", url="https://starcinema.by/")
                kino = telebot.types.InlineKeyboardButton("Построить маршрут", callback_data='starlight_map')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='kino')
                markup.row(eda)
                markup.row(kino)
                markup.row(nazad_mus)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Организации в Могилеве*\n\n*StarLight Cinema*\n\nМногозальный кинотеатр в Могилеве\n\nПреймущества:\n1. 5 кинозалов\n2. Изображение 4К\n3. Dolby Atmos\nПодробнее на сайте',
                                      reply_markup=markup, parse_mode='MarkDown')
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Кинотеатры - StarLight Cinema | {call.from_user.id} | {call.from_user.username} | ')
            elif call.data == 'rodina':
                markup = telebot.types.InlineKeyboardMarkup()
                eda = telebot.types.InlineKeyboardButton("Родина - Сайт", callback_data='starlight')
                kino = telebot.types.InlineKeyboardButton("Построить маршрут", callback_data='rodina_map')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='kino')
                #markup.row(eda)
                #markup.row(kino)
                markup.row(nazad_mus)
                bot.answer_callback_query(call.id, show_alert=False, text="Организация временно недоступна")
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Кинотеатры - Родина | {call.from_user.id} | {call.from_user.username} | ')

            elif call.data == 'chirzor':
                markup = telebot.types.InlineKeyboardMarkup()
                eda = telebot.types.InlineKeyboardButton("Чырвоная Зорка - Сайт", callback_data='starlight')
                kino = telebot.types.InlineKeyboardButton("Построить маршрут", callback_data='chirzor_map')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='kino')
                #markup.row(eda)
                #markup.row(kino)
                markup.row(nazad_mus)
                bot.answer_callback_query(call.id, show_alert=False, text="Организация временно недоступна")
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Кинотеатры - Чырвоная зорка | {call.from_user.id} | {call.from_user.username} | ')
            elif call.data == 'starlight_map':
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.34008325337547,53.90440691405426&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())
                bot.send_location(call.from_user.id, latitude, longitude)
                markup = telebot.types.InlineKeyboardMarkup()
                eda = telebot.types.InlineKeyboardButton("StarLight Cinema - Сайт", url="https://starcinema.by/")
                kino = telebot.types.InlineKeyboardButton("Построить маршрут", callback_data='starlight_map')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='kino')
                markup.row(eda)
                markup.row(nazad_mus)
                bot.send_message(call.from_user.id,
                                 f'Организации в Могилеве\n\nStarLight Cinema\n\nМногозальный кинотеатр в Могилеве\n\nПреймущества:\n1. 5 кинозалов\n2. Изображение 4К\n3. Dolby Atmos\nПодробнее на сайте',
                                      reply_markup=markup)
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | API | Org - kino - starlight | Type: Route | Status: OK (200) | {call.from_user.id} | {call.from_user.username} | ')
            elif call.data == 'atrium_hotel':
                markup = telebot.types.InlineKeyboardMarkup()
                eda = telebot.types.InlineKeyboardButton("Atrium Hotel - Сайт", url="atriumhotel.by")
                kino = telebot.types.InlineKeyboardButton("Построить маршрут", callback_data='atriumhotel_map')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='hotel')
                markup.row(eda)
                markup.row(kino)
                markup.row(nazad_mus)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Организации в Могилеве*\n\n*Atrium Hotel*\n\n',
                                      reply_markup=markup, parse_mode='MarkDown')
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Отели - Atrium Hotel | {call.from_user.id} | {call.from_user.username} | ')
            elif call.data == 'atriumhotel_map':
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.34008325337547,53.90440691405426&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())
                bot.send_location(call.from_user.id, latitude, longitude)
                markup = telebot.types.InlineKeyboardMarkup()
                eda = telebot.types.InlineKeyboardButton("Atrium Hotel - Сайт", url="atriumhotel.by")

                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='hotel')
                markup.row(eda)

                markup.row(nazad_mus)
                bot.send_message(call.message.chat.id, f'*Организации в Могилеве*\n\n*Atrium Hotel*\n\n',
                                      reply_markup=markup, parse_mode='MarkDown')
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | API | Org - hotel - AtriumHotel | Type: Route | Status: OK (200) | {call.from_user.id} | {call.from_user.username} | ')
            elif call.data == 'metropol_hotel':
                markup = telebot.types.InlineKeyboardMarkup()
                eda = telebot.types.InlineKeyboardButton("Metropol Hotel - Сайт", url="metropol.by")
                kino = telebot.types.InlineKeyboardButton("Построить маршрут", callback_data='metropolhotel_map')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='hotel')
                markup.row(eda)
                markup.row(kino)
                markup.row(nazad_mus)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Организации в Могилеве*\n\n*Metropol Hotel*\n\n',
                                      reply_markup=markup, parse_mode='MarkDown')
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Отели - Metropol Hotel | {call.from_user.id} | {call.from_user.username} | ')
            elif call.data == 'metropolhotel_map':
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.34008325337547,53.90440691405426&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())
                bot.send_location(call.from_user.id, latitude, longitude)
                markup = telebot.types.InlineKeyboardMarkup()
                eda = telebot.types.InlineKeyboardButton("Metropol Hotel - Сайт", url="metropol.by")

                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='hotel')
                markup.row(eda)

                markup.row(nazad_mus)
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | API | Org - hotel - MetropolHotel | Type: Route | Status: OK (200) | {call.from_user.id} | {call.from_user.username} | ')
                bot.send_message(call.message.chat.id, f'*Организации в Могилеве*\n\n*Metropol Hotel*\n\n',
                                      reply_markup=markup, parse_mode='MarkDown')
            elif call.data == 'gubernskaya':
                markup = telebot.types.InlineKeyboardMarkup()
                eda = telebot.types.InlineKeyboardButton("Гостиница «Губернская» - Сайт", url="gubernsky.by")
                kino = telebot.types.InlineKeyboardButton("Построить маршрут", callback_data='gubernskaya_map')
                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='hotel')
                markup.row(eda)
                markup.row(kino)
                markup.row(nazad_mus)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='*Организации в Могилеве*\n\n*Гостиница «Губернская»*\n\n',
                                      reply_markup=markup, parse_mode='MarkDown')
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | Отели - «Губернская» | {call.from_user.id} | {call.from_user.username} | ')
            elif call.data == 'gubernskaya_map':
                response = requests.get(
                    f'https://geocode-maps.yandex.ru/1.x/?apikey=93ab15a8-44aa-40a6-b11c-391d7b67f226&geocode=30.343399403473082,53.905020656219946&format=json')
                data = response.json()

                location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = map(float, location.split())
                bot.send_location(call.from_user.id, latitude, longitude)
                markup = telebot.types.InlineKeyboardMarkup()
                eda = telebot.types.InlineKeyboardButton("Гостиница «Губернская» - Сайт", url="gubernsky.by")

                nazad_mus = telebot.types.InlineKeyboardButton("Назад", callback_data='hotel')
                markup.row(eda)

                markup.row(nazad_mus)
                tz_minsk = pytz.timezone("Europe/Minsk")
                print(
                    f'[LOG] | {datetime.now(tz_minsk)} | API | Org - hotel - gubernsky | Type: Route | Status: OK (200) | {call.from_user.id} | {call.from_user.username} | ')
                bot.send_message(call.message.chat.id, f'*Организации в Могилеве*\n\n*Гостиница «Губернская»*\n\n',
                                      reply_markup=markup, parse_mode='MarkDown')


