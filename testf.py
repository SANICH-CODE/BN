import json
import os
from datetime import datetime


def loggingf(userid, username, command):
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    log_entry = f"{time} | {command} | UserID: {userid}, Username: {username}"

    # Проверяем, существует ли файл logs.json
    if os.path.exists('logs.json'):
        with open('logs.json', 'r', encoding='utf-8') as file:
            logs = json.load(file)
    else:
        logs = {}

    # Если даты нет в логе, создаем новую запись
    if date not in logs:
        logs[date] = {}

    # Если время уже существует, добавляем к нему новое действие
    if time in logs[date]:
        logs[date][time].append(log_entry)
    else:
        logs[date][time] = [log_entry]

    # Сохраняем измененный журнал обратно в файл
    with open('logs.json', 'w', encoding='utf-8') as file:
        json.dump(logs, file, indent=4, ensure_ascii=False)
def adminloggingf(userid, command, adminid, admus):
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    log_entry = f"{time} | {command} | AdminID: {adminid}, Adminname: {admus}, UserID: {userid}"

    # Проверяем, существует ли файл logs.json
    if os.path.exists('logs.json'):
        with open('logs.json', 'r', encoding='utf-8') as file:
            logs = json.load(file)
    else:
        logs = {}

    # Если даты нет в логе, создаем новую запись
    if date not in logs:
        logs[date] = {}

    # Если время уже существует, добавляем к нему новое действие
    if time in logs[date]:
        logs[date][time].append(log_entry)
    else:
        logs[date][time] = [log_entry]

    # Сохраняем измененный журнал обратно в файл
    with open('logs.json', 'w', encoding='utf-8') as file:
        json.dump(logs, file, indent=4, ensure_ascii=False)
def banloggingf(userid, command, adminid, admus, reason):
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    log_entry = f"{time} | {command} | AdminID: {adminid}, Adminname: {admus}, UserID: {userid}, Причина {reason}"

    # Проверяем, существует ли файл logs.json
    if os.path.exists('logs.json'):
        with open('logs.json', 'r', encoding='utf-8') as file:
            logs = json.load(file)
    else:
        logs = {}

    # Если даты нет в логе, создаем новую запись
    if date not in logs:
        logs[date] = {}

    # Если время уже существует, добавляем к нему новое действие
    if time in logs[date]:
        logs[date][time].append(log_entry)
    else:
        logs[date][time] = [log_entry]

    # Сохраняем измененный журнал обратно в файл
    with open('logs.json', 'w', encoding='utf-8') as file:
        json.dump(logs, file, indent=4, ensure_ascii=False)
def banloggingf(userid, adminid, admus, text):
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    log_entry = f"{time} | Direct Message | AdminID: {adminid}, Adminname: {admus}, UserID: {userid}, Текст: {text}"

    # Проверяем, существует ли файл logs.json
    if os.path.exists('logs.json'):
        with open('logs.json', 'r', encoding='utf-8') as file:
            logs = json.load(file)
    else:
        logs = {}

    # Если даты нет в логе, создаем новую запись
    if date not in logs:
        logs[date] = {}

    # Если время уже существует, добавляем к нему новое действие
    if time in logs[date]:
        logs[date][time].append(log_entry)
    else:
        logs[date][time] = [log_entry]

    # Сохраняем измененный журнал обратно в файл
    with open('logs.json', 'w', encoding='utf-8') as file:
        json.dump(logs, file, indent=4, ensure_ascii=False)