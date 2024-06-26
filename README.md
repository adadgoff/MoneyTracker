# MoneyTracker

## Проектирование приложения
Проектирование приложения доступно по ссылке https://www.figma.com/file/u6kYi9BUZ6rey5jx3i8PUU/MoneyTracker?type=whiteboard&node-id=0%3A1&t=ltpKOIF6maRyzfVr-1.

Пожалуйста, прочитайте, там немного.

## Запуск и версия python

Версия python `3.12.3`. На других версиях что-то может не работать.

Для запуска кода Вы можете создать виртуальное окружение. Пример на операционной системе `Windows`.

```
cd src
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python main.py
```

## Структура проекта

```
|- docs                 # условие тестового задания.
|- resources            # ресурсы программы.
   |- databases         # базы данных в формате ".csv".
   |- translations      # переводы в формате ".json".
|- src                  # код программы. 
   |- app               # код приложения.
      |- auth           # модуль, отвечающий за логику авторизации приложения.
      |- core           # модуль, отвечающий за настройки приложения.
      |- database       # модуль, отвечающий за "подключение" к базе данных.
      |- entry          # модуль, отвечающий за логику записей.
      |- user           # модуль, отвечающий за логику пользователей.
      |- utils          # утилиты.
      |- app_main.py    # точка входа приложения.
   |- main.py           # точка входа.
   |- requirements.txt  # зависимости проекта.
```

## Возможные улучшения

- [ ] Упростить логику работы с переводом.
- [ ] Работать с SQL-базой данных. Работать с асинхронной базой данных. Так как работа тестовая, решил не создавать
  подключение к БД и не занимать порт под неё.
