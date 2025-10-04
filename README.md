# DIARY - Веб-приложение для ведения личного дневника

#### Приложение позволяет пользователям создавать, редактировать и удалять записи в дневнике, 
#### а также просматривать свои записи в удобном интерфейсе. 
#### Пользовательский интерфейс реализован с использованием Django шаблонов и Bootstrap стилей 
#### для создания адаптивного и современного дизайна.

### Функционал сайта:
1. **Регистрация и аутентификация пользователей:** 
   - Пользователи должны иметь возможность зарегистрироваться, войти в систему и выйти из неё.
2. **Создание, редактирование и удаление записей в дневнике:** 
   - Авторизованные пользователи могут добавлять новые записи в дневник, редактировать существующие записи (только свои) и удалять ненужные записи.
3. **Просмотр записей:** 
   - Пользователи могут просматривать список всех своих записей.
   - Пользователи могут просматривать отдельные записи в подробном виде.
4. **Поиск по записям:** 
   - Возможность поиска записей по заголовку или содержимому в интерфейсе сайта.

## ✨ Возможности

- **Аутентификация пользователей** (регистрация, вход, выход)
- **`CRUD` операции** с записями дневника
- **Система тегов** для организации записей
- **Чистый UI** с `Bootstrap`
- **Адаптивный дизайн**
- **`Docker`- контейнеризация**
- **`CI/CD pipeline`** с `GitHub Actions`
- **`PostgreSQL`** как основная БД

## 🛠️ Технологический стек

## Технологический стек и требования

- Язык программирования: Python: 3.13
- Фреймворк: Django: 5.2.7 (Django REST Framework при необходимости)
- База данных: PostgreSQL (через psycopg2)
- psycopg2 и psycopg2-binary
- pandas, requests, python-dotenv, pillow
- Шаблоны и стили: Django шаблоны для рендеринга HTML страниц, Bootstrap для стилизации интерфейса
- Контейнеризация: Docker для упаковки приложения и базы данных
- Poetry для управления зависимостями
- Линтинг и форматирование: flake8, mypy, black, isort
- Тестирование: pytest (pytest-django при необходимости) и coverage
- Документация:  файл README.md с описанием структуры проекта


## 🚀 Быстрый старт

### 1. Клонирование репозитория
```
git clone https://github.com/evgeniya-avksenteva/Diploma_Project.git
```

### 2. Запуск приложения
```
docker-compose up --build
```

### 3. Применение миграций и создание тестовых данных
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py create_test_data
```

### 4. Настройка окружения
Создайте файл .env (или .env.example) и заполните параметры БД и секретов. Пример переменных:
```commandline
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=pythonproject_db
DB_USER=pythonproject_user
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

### 4. Применение миграций и подготовка базы данных
```commandline
poetry run python manage.py migrate
```

### 5. Создание суперпользователя (администратор Django)
```commandline
poetry run python manage.py createsuperuser
```

### 6. Запуск локального сервера
```commandline
poetry run python manage.py runserver
```
Приложение будет доступно по адресу: http://127.0.0.1:8000

##  Запуск через `Docker`

### Сборка и запуск:
```commandline
docker build -t diary-app .
docker run -p 8000:8000 diary-app
```

### Или с Docker Compose:
```commandline
docker-compose up --build
```

## Тестирование и качество кода

### Запуск тестов:
```commandline
poetry run python manage.py test
```

### Запуск с coverage:
```commandline
coverage run manage.py test
coverage report
```

### Проверка покрытия:
```commandline
coverage run manage.py test
coverage report
```

## Форматирование (Black) и сортировка импортов (Isort):
```commandline
poetry run black .
poetry run isort .
```

## Линтинг (Flake8):
```commandline
poetry run flake8
```

## CI/CD Pipeline

### В проекте используется GitHub Actions для автоматизации:

- Автоматическое тестирование при `push/pull` request
- Сборка `Docker` образа
- Автоматический деплой на сервер
- `API Endpoints`


## Встраиваемые команды (для удобства)

### Миграции:
```commandline
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```
### Создание тестовых данных (если реализовано):
```commandline
poetry run python manage.py create_test_data
```
### Запуск тестов с конкретными тестами (пример):
```commandline
pytest
python manage.py test diary.tests
```
