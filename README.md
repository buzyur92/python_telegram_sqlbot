<h2>Телеграм бот, который подсказывает основные postgreSQL запросы</h2>

> **Статус проекта:**
>
> 🟢 Поддерживается (активный) 

## Цели и Задачи
Помочь QA инженеру быстро вспомнить нужные SQL запросы.

Бот предлагает название запроса и какую функцию этот запрос выполняет

## 🖼 Скриншоты

Меню бота:

![image](https://raw.githubusercontent.com/buzyur92/python_telegram_sqlbot/refs/heads/main/static/menu.png)



## 💻 Технологии

* Python
* Библиотека `python-telegram-bot`

## ⏬ Установка на локальном компьютере

1. Скачать проект
   
2. Создать бота и через [@BotFather](https://t.me/BotFather) и вставить в проекте свой токен от бота

3. Создаём виртуальное окружение внутри папки проекта.
Далее команды для MacOS (для windows инуструкция [есть вот тут](https://realpython.com/python-virtual-environments-a-primer/#create-it))

``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```
4. Устанавливаем библиотеки

``` markdown
python3 -m pip install pyTelegramBotAPI
```

``` markdown
python3 -m pip install faker
```

5. Запускаем
``` markdown
python3 card_bot.py
```

## Автор

Даниил Бузюров ([@buzyur](https://t.me/buzyur))
