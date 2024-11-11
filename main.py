from testf import loggingf
import requests
import ru
from functions import user, admin, flog
from functions.other import generate_password
import vass_private

PROXY_API_KEY = 'sk-04QYlQmpbMQFmMJMhB6o4Z9N0sqMcrBy'
from threading import Thread
from telebot import *
from config import TOKEN
import json
bot = telebot.TeleBot(TOKEN)

import datetime
from flask import Flask
app = Flask(__name__)
current_date = datetime.date.today()
current_date_time = datetime.datetime.now()
current_time = current_date_time.time()

users = {}
# ОБЪЯВЛЕНИЯ ВНЕШНИХ КОМАНД START
ru.register_commands(bot)
flog.register_commands(bot)
user.register_commands(bot)
admin.register_commands(bot)
# ОБЪЯВЛЕНИЯ ВНЕШНИХ КОМАНД END

@bot.message_handler(commands=['start'])
def welcome(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()

    # Извлекаем параметр из команды


    nachnem = types.InlineKeyboardButton('Начать использование на русском', callback_data='nachnem')
    rules = types.InlineKeyboardButton('Правила использования', url="t.me/BelarusNature_bot/rules")
    ya_maps = types.InlineKeyboardButton('Условия использования Яндекс.Карт',
                                         url="https://yandex.ru/legal/maps_termsofuse/")

    markup.add(nachnem)
    markup.add(rules)
    markup.add(ya_maps)
    with open("users.json", "r") as f_o:
        data_from_json = json.load(f_o)

    user_id = message.from_user.id
    username = message.from_user.username
    time.localtime()
    if str(user_id) not in data_from_json:
        data_from_json[user_id] = {"username": username, "language": "ru", "password": generate_password(), "login": "True", "premium": "False", "out": "False", "notify": "True", "hiden": "False", "tester": "False", "RegDate": str(current_date), "RegTime": str(current_time),
                                   "status": "Tester", "ban": "False"}
    with open("users.json", "w") as f_o:
        json.dump(data_from_json, f_o, indent=4, ensure_ascii=False)
    bot.send_message(chat_id,
                     'Добро пожаловать в бота\n\n---\nНажимая кнопку "Начнем" вы соглашаетесь со всеми правилами',
                     reply_markup=markup)
    if len(message.text.split()) > 1:
        deep_link = message.text.split()[1]  # Получаем часть после /start
    else:
        deep_link = None
#    ОБРАБОТКА СОДЕРЖАНИЯ УРЛА
    if deep_link == 'minsk_1':
        bot.send_message(chat_id, 'Вы выбрали Minsk 1')
    elif deep_link == 'minsk_2':
        bot.send_message(chat_id, 'Вы выбрали Minsk 2 BN Plus')
    elif deep_link == 'brest_1':
        bot.send_message(chat_id, 'Вы выбрали Brest 1')
    elif deep_link == 'vitebsk_1':
        bot.send_message(chat_id, 'Вы выбрали Vitebsk 1')
    elif deep_link == 'gomel_1':
        bot.send_message(chat_id, 'Вы выбрали Gomel 1')
    elif deep_link == 'grodnol_1':
        bot.send_message(chat_id, 'Вы выбрали Grodno 1')
    elif deep_link == 'mogilev_2':
        bot.send_message(chat_id, 'Вы выбрали Mogilev 2 BN Plus')
        if vass_private.is_premium(message.from_user.id):
            bot.send_message(chat_id, 'Доступ разрешен')
        else:
            bot.send_message(chat_id, 'Доступ запрещен\nТребуется BN Plus')

        
    elif deep_link == 'find_my_pass':
        login(message)
    elif deep_link == 'login_error':
        login(message)
@bot.message_handler(commands=['testlogin'])
def login(message):
    user_id = str(message.from_user.id)
    loggingf(message.from_user.id, message.from_user.username, "Login")
    chat_id = message.chat.id
    passw = vass_private.get_pass(user_id)
    markup = types.InlineKeyboardMarkup()
    on = telebot.types.InlineKeyboardButton(f"Включить авторизацию", callback_data=f'logintrue_{user_id}')
    off = telebot.types.InlineKeyboardButton(f"Отключить авторизацию", callback_data=f'loginfalse_{user_id}')
    url = telebot.types.InlineKeyboardButton(f"Быстрая авторизация", url=f'https://web.bn-team.xyz/?username={user_id}&password={passw}')
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
@bot.message_handler(content_types="web_app_data")  # получаем отправленные данные
def answer(webAppMes):
       print(webAppMes)  # вся информация о сообщении
       print(webAppMes.web_app_data.data)  # конкретно то что мы передали в бота
       bot.send_message(webAppMes.chat.id, f"получили инофрмацию из веб-приложения: {webAppMes.web_app_data.data}")
       # отправляем сообщение в ответ на отправку данных из веб-приложения

@bot.message_handler(commands=['tandir'])
def send_location_tandir(call):
    response = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey=b629996f-0c90-40c0-ace1-9956639dd201&geocode=30.330534192956257,53.895209941464955&format=json')
    data = response.json()

    location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    longitude, latitude = map(float, location.split())

    bot.send_location(call.from_user.id, latitude, longitude)


@bot.message_handler(commands=['project_zero'])
def zero_command(message):
    if message.from_user.id == 6978792645:
        user_id = message.from_user.id
        result = vass_private.project_zero()
        markup = telebot.types.InlineKeyboardMarkup()
        banb = telebot.types.InlineKeyboardButton(f"Да", callback_data='startzero6978792645')
        user = telebot.types.InlineKeyboardButton(f"Нет", callback_data='stopzero6978792645')
        markup.row(banb)
        markup.row(user)

        bot.send_message(message.chat.id, "Запустить аварийный протокол?", reply_markup=markup)

    else:
        pass

@bot.message_handler(commands=['clck'])
def set_premium(message):
    endpoint = 'https://clck.ru/--'

    if vass_private.is_premium(message.from_user.id):
        if len(message.text.split()) != 2:
            bot.send_message(message.chat.id, "Использование: /clck [ссылка]")
            return

        original_url = message.text.split()[1]
        response = requests.get(endpoint, params={'url': original_url})

        if response.status_code == 200:
            result = response.text  # Вам нужно обработать ответ, чтобы получить и вывести сокращенную ссылку
            # Предположим, что сокращенная ссылка возвращается в виде текста (или JSON)
            bot.send_message(message.chat.id, f"Сокращенная ссылка: {result}")
        else:
            bot.send_message(message.chat.id, "Ошибка при сокращении ссылки. Попробуйте еще раз позже.")
    else:
        bot.send_message(message.chat.id, "У вас нет доступа к этой команде\nДля доступа купите BN Plus")




def run_flask():
    app.run(debug=True, use_reloader=False)  # use_reloader=False, чтобы избежать запуска Flask дважды

def start_bot():
    while True:
        vass_private.info()
        vass_private.start()
        time.sleep(3)

        print('| WEB App Successfully start')
        print('| Bot Successfully start')

        print('| Time Successfully reset')
        try:
            if __name__ == '__main__':
                bot.polling(none_stop=True)
                print('Start')

        except Exception as e:
            vass_private.error(e)
            time.sleep(2)

@app.route('/')
def home():
    return "Welcome to the VASS Web App!"

if __name__ == '__main__':
    print('| | |  VASS GROUP | | | |')
    print('| |  Access allowed | | |')
    print('Authorization not required')
    print('-------------------------')
    time.sleep(1)

    # Запуск Flask в отдельном потоке
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    # Запуск бота
    start_bot()

