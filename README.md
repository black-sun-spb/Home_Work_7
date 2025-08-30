# Интернет-магазин (Django)

Учебный проект по созданию интернет-магазина на Django.

## Стек технологий
- Python 3.10+
- Django 5+
- PostgreSQL
- Bootstrap 5
- HTML/CSS

## Возможности проекта
- Создан Django-проект и приложение `catalog`
- Модели `Product` и `Category` с базовыми полями
- Админка с регистрацией моделей и фильтрацией/поиском
- Подключена база данных PostgreSQL
- Работа с фикстурами для моделей
- Кастомная команда для наполнения тестовыми данными
- Страницы: главная с последними товарами и страница контактов
- Поддержка статики и медиа файлов
- Форма обратной связи с сохранением данных через админку

## Установка проекта
1. Клонируем репозиторий:
```
git clone <repo_url>
cd shop_project
```
2. Создаём виртуальное окружение и активируем его:

```
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```
3. Устанавливаем зависимости:

```
pip install -r requirements.txt
```
4. Настраиваем базу данных:

Создаём базу PostgreSQL

Создаём пользователя и пароль

Настройки подключения указываем в .env файле (см. .env.example)

5. Применяем миграции:

```
python manage.py migrate
```
6. Создаём суперпользователя:

```
python manage.py createsuperuser
```
7. Запускаем сервер:

```
python manage.py runserver
```

## Работа с проектом
Админка доступна по адресу: http://127.0.0.1:8000/admin/

Главная страница: http://127.0.0.1:8000/

Страница контактов: http://127.0.0.1:8000/contacts/

Для загрузки тестовых данных используем кастомную команду или фикстуры:

```
python manage.py loaddata catalog/fixtures/categories.json
python manage.py loaddata catalog/fixtures/products.json
```
## Структура проекта
```
shop_project/
├─ catalog/
│  ├─ admin.py
│  ├─ models.py
│  ├─ views.py
│  ├─ urls.py
│  ├─ templates/catalog/
│  └─ static/catalog/
├─ config/
│  ├─ settings.py
│  └─ urls.py
├─ manage.py
├─ requirements.txt
└─ README.md
```
## Переменные окружения
Все секретные ключи и настройки базы данных вынесены в .env

Пример файла: .env.example

Настройки включают:

    SECRET_KEY

    DEBUG

    DATABASE_NAME

    DATABASE_USER

    DATABASE_PASSWORD

    DATABASE_HOST

    DATABASE_PORT

## Лицензия

Проект используется в образовательных целях.