import json
import telebot
import requests
API_TOKEN = '7347749794:AAEEs0RKg-VE-1TxxMrSwWCccH_JY9QUoO4'  # Замените на ваш токен
bot = telebot.TeleBot(API_TOKEN, threaded=False)
BNGIVETEXTV = f'Вам выдали BN Plus\n\nТеперь:\n1.Отключено видео\n2.Доступен раздел "DVIZH"\n3.Редактирование профиля*\n4.Общение с другими пользователями\n5.И еще какая-то штучка'
BNGIVETEXTZ = f'Ваш BN Plus деактивирован администратором'
SETADMIN = f'Вас повысили до Администратора'
SETUSER = f'Ваш аккаунт администратора деактивирован'
SETUSERLOG = f'CONSOLE LOG | SETUSER | '
TOKEN = '6501184236:AAG1uvyzQyn5HqXJwWZbT1kNoUHGdc452jo'
import json
def info():
    print('| | | | | | | | | | | | |')
    print('| | |  VASS GROUP | | | |')
    print('| |  Sergei Nikitko | | |')
    print('| | | |BN T E A M | | | |')
    print('| | | V. 0.0.9 REF  | | |')
    print('| | | | B E T A | | | | |')
    print('| | | | | | | | | | | | |')

def start():
    print('| Starting...')


def start_ok():
    print('| Successfully start')

def error(e):
    print('-------------------------')
    print('-------------------------')
    print('| | Error: ', e)
    print('| | | | | | | | | | | | |')
    print('| | | R E S T A R T | | |')
    print('| | | | | | | | | | | | |')
    print('-------------------------')
    print('-------------------------')
inform = str("Информационая страница\n\nСетевые подключения:\nVSG API --- OK\nYandex API --- OK\nYa.Cloud API --- [OK]\nbn.vass-group.xyz --- [OK]\nserver.bn.vass-group.xyz --- [OK]\n\nВнутреннее состояние:\nТип запуска --- Ручной\nРазработчик --- {ADMIN}")


def is_user_banned(user_id):
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        user_data = users_data.get(str(user_id))

        if user_data:
            return user_data.get('ban') == 'True'
        else:
            return False  # Пользователь не найден, считаем, что он не заблокирован

    except FileNotFoundError:
        print("Файл с данными пользователей не найден.")
        return False
    except json.JSONDecodeError:
        print("Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON.")
        return False
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return False
def is_premium(user_id):
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        user_data = users_data.get(str(user_id))

        if user_data:
            return user_data.get('premium') == 'True'
        else:
            return False  # Пользователь не найден, считаем, что он не заблокирован

    except FileNotFoundError:
        print("Файл с данными пользователей не найден.")
        return False
    except json.JSONDecodeError:
        print("Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON.")
        return False
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return False
def is_login(user_id):
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        user_data = users_data.get(str(user_id))

        if user_data:
            return user_data.get('login') == 'True'
        else:
            return False  # Пользователь не найден, считаем, что он не заблокирован

    except FileNotFoundError:
        print("Файл с данными пользователей не найден.")
        return False
    except json.JSONDecodeError:
        print("Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON.")
        return False
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return False
def is_notify(user_id):
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        user_data = users_data.get(str(user_id))

        if user_data:
            return user_data.get('notify') == 'True'
        else:
            return False  # Пользователь не найден, считаем, что он не заблокирован

    except FileNotFoundError:
        print("Файл с данными пользователей не найден.")
        return False
    except json.JSONDecodeError:
        print("Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON.")
        return False
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return False
def get_pass(user_id):
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        user_data = users_data.get(str(user_id))

        if user_data:
            return user_data.get('password')
        else:
            return False  # Пользователь не найден, считаем, что он не заблокирован

    except FileNotFoundError:
        print("Файл с данными пользователей не найден.")
        return False
    except json.JSONDecodeError:
        print("Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON.")
        return False
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return False
def is_hide(user_id):
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        user_data = users_data.get(str(user_id))

        if user_data:
            return user_data.get('hiden') == 'True'
        else:
            return False  # Пользователь не найден, считаем, что он не заблокирован

    except FileNotFoundError:
        print("Файл с данными пользователей не найден.")
        return False
    except json.JSONDecodeError:
        print("Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON.")
        return False
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return False

def is_admin(user_id):
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        user_data = users_data.get(str(user_id))

        if user_data:
            return user_data.get('status') == 'admin'
        else:
            return False  # Пользователь не найден, считаем, что он не заблокирован

    except FileNotFoundError:
        print("Файл с данными пользователей не найден.")
        return False
    except json.JSONDecodeError:
        print("Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON.")
        return False
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return False
def reg_date(user_id):
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        user_data = users_data.get(str(user_id))
        return user_data.get('RegDate')


    except FileNotFoundError:
        print("Файл с данными пользователей не найден.")
        return False
    except json.JSONDecodeError:
        print("Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON.")
        return False
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return False


def reg_time(user_id):
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        user_data = users_data.get(str(user_id))
        time = str(user_data.get('RegTime'))
        return time


    except FileNotFoundError:
        print("Файл с данными пользователей не найден.")
        return "ERR"
    except json.JSONDecodeError:
        print("Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON.")
        return "ERR"
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return False
def isprem(user_id):
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        user_data = users_data.get(str(user_id))
        prem = user_data.get('premium')
        if prem == "True":
            return "✨ Подписка активна ✨"
        else:
            return "❌ Подписка отсутствует ❌"


    except FileNotFoundError:
        print("Файл с данными пользователей не найден.")
        return False
    except json.JSONDecodeError:
        print("Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON.")
        return False
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return False


def count_users():
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        return len(users_data)  # Возвращаем количество пользователей

    except FileNotFoundError:
        print("Файл с данными пользователей не найден.")
        return 0
    except json.JSONDecodeError:
        print("Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON.")
        return 0
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return 0

def search_user(user_id, keys_to_return=None):
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        # Проверяем, является ли users_data словарем
        if not isinstance(users_data, dict):
            print("Ошибка: Данные пользователей должны быть словарем.")
            return None

        # Поиск пользователя по user_id
        user = users_data.get(user_id)
        if user:
            # Если указаны ключи для возвращения
            if keys_to_return:
                # Получаем только значения по указанным ключам и объединяем их в строку
                return ', '.join(user[key] for key in keys_to_return if key in user)
            # Возвращаем все значения пользователя, объединенные в строку
            return ', '.join(user.values())  # Объединяем все значения пользователя в строку
        else:
            return "Пользователь не найден."


    except FileNotFoundError:
        print("Файл с данными пользователей не найден.")
        return None
    except json.JSONDecodeError:
        print("Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON.")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return None


def ban_user(user_id, admin_id, admin_us, reason):
    try:
        # Открываем пользователи
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        # Проверяем наличие пользователя
        if user_id in users_data:
            # Устанавливаем значение 'ban' в true
            users_data[user_id]['ban'] = 'True'
            # Сохраняем изменения обратно в файл
            msg = f'Ваш аккаунт заблокирован\n\nАдминистратор: @{admin_us} ({admin_id})\nПричина: {reason}'
            url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={user_id}&text={msg}'
            requests.get(url)
            with open('users.json', 'w') as file:
                json.dump(users_data, file, indent=4, ensure_ascii=False)
            return f"Пользователь {user_id} был забанен."
        else:
            return "Пользователь не найден."



    except FileNotFoundError:

        print("Файл с данными пользователей не найден.")
    except json.JSONDecodeError:

        print("Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON.")
    except Exception as e:

        print(f"Произошла ошибка: {str(e)}")
def login_true(user_id):
    try:
        # Открываем пользователи
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        # Проверяем наличие пользователя
        if user_id in users_data:
            # Устанавливаем значение 'ban' в true
            users_data[user_id]['login'] = 'True'
            # Сохраняем изменения обратно в файл
            msg = f'Системное сообщение\n\nИзменение настроек приватности\nАвторизация включена'
            url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={user_id}&text={msg}'

            with open('users.json', 'w') as file:
                json.dump(users_data, file, indent=4, ensure_ascii=False)
            return f"Авторизация включена."
        else:
            return "Пользователь не найден."



    except FileNotFoundError:

        print("Файл с данными пользователей не найден.")
    except json.JSONDecodeError:

        print("Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON.")
    except Exception as e:

        print(f"Произошла ошибка: {str(e)}")

def login_false(user_id):
    try:
        # Открываем пользователи
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        # Проверяем наличие пользователя
        if user_id in users_data:
            # Устанавливаем значение 'ban' в true
            users_data[user_id]['login'] = 'False'
            # Сохраняем изменения обратно в файл
            msg = f'Системное сообщение\n\nИзменение настроек приватности\nАвторизация отключена'
            url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={user_id}&text={msg}'

            with open('users.json', 'w') as file:
                json.dump(users_data, file, indent=4, ensure_ascii=False)
            return f"Авторизация отключена."
        else:
            return "Пользователь не найден."



    except FileNotFoundError:

        print("Файл с данными пользователей не найден.")
    except json.JSONDecodeError:

        print("Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON.")
    except Exception as e:

        print(f"Произошла ошибка: {str(e)}")
def set_password(user_id, password):
    try:
        # Открываем пользователи
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        # Проверяем наличие пользователя
        if user_id in users_data:
            # Устанавливаем значение 'ban' в true
            users_data[user_id]['password'] = f'{password}'
            # Сохраняем изменения обратно в файл

            with open('users.json', 'w') as file:
                json.dump(users_data, file, indent=4, ensure_ascii=False)
            return f"Пароль изменен"
        else:
            return "Пользователь не найден."



    except FileNotFoundError:

        print("Файл с данными пользователей не найден.")
    except json.JSONDecodeError:

        print("Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON.")
    except Exception as e:

        print(f"Произошла ошибка: {str(e)}")







def set_not_false(user_id):
    try:
        # Открываем пользователи
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        # Проверяем наличие пользователя
        if user_id in users_data:
            # Устанавливаем значение 'ban' в true
            users_data[user_id]['notify'] = 'False'
            # Сохраняем изменения обратно в файл
            with open('users.json', 'w') as file:
                json.dump(users_data, file, indent=4, ensure_ascii=False)

        else:
            pass

    except FileNotFoundError:
        return "Файл с данными пользователей не найден."
    except json.JSONDecodeError:
        return "Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON."
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"


def unban_user(user_id, admin_id, admin_us, reason):
    try:
        # Открываем пользователи
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        # Проверяем наличие пользователя
        if user_id in users_data:
            msg = f'Ваш аккаунт разблокирован\n\nАдминистратор: @{admin_us} ({admin_id})\nПричина: {reason}'
            url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={user_id}&text={msg}'
            requests.get(url)
            # Устанавливаем значение 'ban' в true
            users_data[user_id]['ban'] = 'False'
            # Сохраняем изменения обратно в файл
            with open('users.json', 'w') as file:
                json.dump(users_data, file, indent=4, ensure_ascii=False)
            return f"Пользователь {user_id} был разбанен."
        else:
            return "Пользователь не найден."

    except FileNotFoundError:
        return "Файл с данными пользователей не найден."
    except json.JSONDecodeError:
        return "Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON."
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"
def set_admin(user_id):
    try:
        # Открываем пользователи
        with open('users.json', 'r') as file:
            users_data = json.load(file)
        url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={user_id}&text={SETADMIN}'
        requests.get(url)
        # Проверяем наличие пользователя
        if user_id in users_data:
            # Устанавливаем значение 'ban' в true
            users_data[user_id]['status'] = 'admin'
            # Сохраняем изменения обратно в файл
            with open('users.json', 'w') as file:
                json.dump(users_data, file, indent=4, ensure_ascii=False)
            return f"Пользователь {user_id} повышен до Administrator."
        else:
            return "Пользователь не найден."

    except FileNotFoundError:
        return "Файл с данными пользователей не найден."
    except json.JSONDecodeError:
        return "Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON."
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"
def set_premium(user_id):
    try:
        # Открываем пользователи
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        # Проверяем наличие пользователя
        if user_id in users_data:
            url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={user_id}&text={BNGIVETEXTV}'
            requests.get(url)
            # Устанавливаем значение 'ban' в true
            users_data[user_id]['premium'] = 'True'
            users_data[user_id]['notify'] = 'False'
            # Сохраняем изменения обратно в файл
            with open('users.json', 'w') as file:
                json.dump(users_data, file, indent=4, ensure_ascii=False)
            return f"Пользователь {user_id} Получил BN PLus"


        else:
            return "Пользователь не найден."

    except FileNotFoundError:
        return "Файл с данными пользователей не найден."
    except json.JSONDecodeError:
        return "Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON."
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"
def den_premium(user_id):
    try:
        # Открываем пользователи
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        # Проверяем наличие пользователя
        if user_id in users_data:
            url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={user_id}&text={BNGIVETEXTZ}'
            requests.get(url)
            # Устанавливаем значение 'ban' в true
            users_data[user_id]['premium'] = 'False'
            users_data[user_id]['notify'] = 'True'
            # Сохраняем изменения обратно в файл
            with open('users.json', 'w') as file:
                json.dump(users_data, file, indent=4, ensure_ascii=False)
            return f"Пользователю {user_id} удален BN Plus"


        else:
            return "Пользователь не найден."

    except FileNotFoundError:
        return "Файл с данными пользователей не найден."
    except json.JSONDecodeError:
        return "Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON."
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"
def set_user(user_id):
    try:
        # Открываем пользователи
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        # Проверяем наличие пользователя
        if user_id in users_data:
            url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={user_id}&text={SETUSER}'
            requests.get(url)
            # Устанавливаем значение 'ban' в true
            users_data[user_id]['status'] = 'user'
            # Сохраняем изменения обратно в файл
            with open('users.json', 'w') as file:
                json.dump(users_data, file, indent=4, ensure_ascii=False)
            return f"Пользователь {user_id} понижен до User."
        else:
            return "Пользователь не найден."

    except FileNotFoundError:
        return "Файл с данными пользователей не найден."
    except json.JSONDecodeError:
        return "Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON."
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"


def to_msg(us_id, msg, own_id, own_us):
    to_msg_text = f"Получено новое сообщение\nОтправитель: @{own_us} ({own_id})\nПолучатель: Вы {us_id}\n\n---\n{msg}\n---\nДля ответа: /to {own_id} текст"

    # Кодирование параметров текста в URL
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={us_id}&text={to_msg_text}'
    with open('users.json', 'r') as file:
        users_data = json.load(file)

    # Проверяем наличие пользователя
    if us_id in users_data:
        requests.get(url)
        return "200"
    else:
        return "Error"



def project_zero():
    user_id = '6978792645'
    try:
        # Открываем пользователи
        with open('users.json', 'r') as file:
            users_data = json.load(file)

        # Проверяем наличие пользователя
        if user_id in users_data:

            # Устанавливаем значение 'ban' в true
            users_data[user_id]['status'] = 'admin'
            users_data[user_id]['ban'] = 'False'
            # Сохраняем изменения обратно в файл
            with open('users.json', 'w') as file:
                json.dump(users_data, file, indent=4, ensure_ascii=False)
            return f"Выполнено"
        else:
            return "Отказ"

    except FileNotFoundError:
        return "Файл с данными пользователей не найден."
    except json.JSONDecodeError:
        return "Ошибка при чтении файла данных. Убедитесь, что файл имеет правильный формат JSON."
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"