# Social Network

Учебный проект социальной сети на Django. В проекте есть главная страница, страницы входа и регистрации, форма регистрации и модель профиля пользователя.

## Технологии

- Python
- Django 6.1.2
- PostgreSQL
- HTML, CSS и JavaScript

## Что находится в проекте

- `home/` — главная страница.
- `login/` — страница входа.
- `register/` — регистрация пользователя и создание профиля.
- `sociial_Network/` — настройки и URL-маршруты Django.
- `templates/` — общие HTML-шаблоны.
- `static/` — CSS и JavaScript.
- `manage.py` — запуск команд Django.

## Запуск на Windows

### 1. Установить зависимости

Нужны Python и PostgreSQL. Откройте CMD в папке проекта и выполните:

```cmd
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Создать базу данных PostgreSQL

Создайте базу данных с именем `social_network` в PostgreSQL. Например, через `psql`:

```sql
CREATE DATABASE social_network;
```

### 3. Указать настройки подключения

В том же окне CMD задайте пароль пользователя PostgreSQL (укажите свой пароль вместо `ВАШ_ПАРОЛЬ`):

```cmd
set DB_NAME=social_network
set DB_USER=postgres
set DB_PASSWORD=ВАШ_ПАРОЛЬ
set DB_HOST=localhost
set DB_PORT=5432
```

Эти значения действуют в текущем окне CMD. Не добавляйте реальные пароли и секретные ключи в GitHub.

### 4. Применить миграции и запустить сайт

```cmd
python manage.py migrate
python manage.py runserver
```

Откройте в браузере: http://127.0.0.1:8000/

Панель администратора находится по адресу http://127.0.0.1:8000/admin/ . Для создания администратора выполните:

```cmd
python manage.py createsuperuser
```

## Загрузка на GitHub

Создайте пустой репозиторий на GitHub. Затем откройте CMD в корневой папке проекта (там, где находится `manage.py`) и выполните команды, заменив адрес на ссылку своего репозитория:

```cmd
git init
git add .
git status
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/ВАШ_ЛОГИН/ИМЯ_РЕПОЗИТОРИЯ.git
git push -u origin main
```

Если команда `git remote add origin` сообщает, что `origin` уже существует, используйте:

```cmd
git remote set-url origin https://github.com/ВАШ_ЛОГИН/ИМЯ_РЕПОЗИТОРИЯ.git
```

## Важно

Папка виртуального окружения, локальная база данных, IDE-настройки и файлы с секретами исключены через `.gitignore`. Для реального размещения сайта в интернете обязательно задайте собственный `DJANGO_SECRET_KEY`, выключите `DJANGO_DEBUG` и настройте `DJANGO_ALLOWED_HOSTS`.
