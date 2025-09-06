# Интернет-магазин (Django)

Учебный проект по созданию интернет-магазина на Django.

## Стек технологий
- Python 3.10+
- Django 5+
- PostgreSQL
- Bootstrap 5
- HTML/CSS

## Возможности проекта

Приложение `catalog`
- Модели:
  - Product (название, описание, цена, категория, изображение, дата создания)
  - Category (название, дата создания)
  - Contact (форма обратной связи)
- Админка с регистрацией моделей, фильтрацией и поиском
- Работа с фикстурами и кастомной командой для наполнения тестовыми данными
- Страницы:
  - Главная с последними товарами и пагинацией
  - Подробная страница товара
  - Страница контактов с формой обратной связи
  - Форма добавления новых товаров (для администраторов)
- Поддержка статики и медиа файлов
- Вывод сообщений пользователю через Django messages
- Безопасное хранение секретов через `.env`
- Все контроллеры переведены с FBV на CBV

Приложение `blog`

- Модель `BlogPost` с полями:
  - Заголовок
    - Содержимое 
    - Превью (изображение)
    - Дата создания 
    - Признак публикации (булевое поле)
    - Количество просмотров

- Реализован полный CRUD через CBV (ListView, DetailView, CreateView, UpdateView, DeleteView)
- При просмотре статьи увеличивается счетчик просмотров
- На список статей выводятся только опубликованные статьи
- После редактирования происходит перенаправление на страницу этой статьи
- Шаблоны используют базовый шаблон и подшаблон с меню

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

- Создаём базу PostgreSQL

- Создаём пользователя и пароль

- Настройки подключения указываем в `.env` файле (см. `.env.example`)

5. Применяем миграции:

```
python manage.py migrate
```
6. Создаём суперпользователя:

```
python manage.py createsuperuser
```
7. Загружаем тестовые данные (опционально):
```
python manage.py loaddata catalog/fixtures/categories.json
python manage.py loaddata catalog/fixtures/products.json
```
8. Запускаем сервер:

```
python manage.py runserver
```

## Работа с проектом
- Админка доступна по адресу: http://127.0.0.1:8000/admin/
- Главная страница: http://127.0.0.1:8000/
- Страница контактов: http://127.0.0.1:8000/contacts/
- Страница блога: http://127.0.0.1:8000/blog/

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
├─ blog/
│  ├─ models.py
│  ├─ views.py
│  ├─ urls.py
│  └─ templates/blog/
├─ config/
│  ├─ settings.py
│  └─ urls.py
├─ manage.py
├─ requirements.txt
└─ README.md
```

## Переменные окружения
Все секретные ключи и настройки базы данных вынесены в `.env`

Пример файла: `.env.example`

Настройки включают:

```
SECRET_KEY=
DEBUG=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=
EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

## Лицензия

Проект используется в образовательных целях.