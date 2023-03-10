# Установка

1. Для начала склонируйте репозиторий:
```
git clone https://github.com/madjar-code/Music-API
```

2. Создайте виртуальное окружение:
```
py -m venv venv
```

3. Активируйте виртуальное окружение:
```
venv\Scripts\activate
```

4. Установите необходимые зависимости из requirements.txt:
```
pip install -r requirements.txt
```

5. Переименуйте файл example.env в .env и укажите необходимые значения переменных окружения. (example.env находится в папке server/server)

6. Время проводить миграции для базы данных:
```
py manage.py migrate
```

7. Чтобы использовать админ-панель, необходимо создать суперпользователя посредством
команды ```py manage.py createsuperuser```. Валидация паролей отключена.

8. Далее мы запускаем сервер:
```
py manage.py runserver
```

9. Для просмотра документации перейдите по адресу: localhost:8000/
