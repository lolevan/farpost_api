# Farpost API Service

API-сервис для получения данных о первых 10 объявлениях.

## Описание

Этот проект представляет собой API-сервис, разработанный с использованием Django, который позволяет получить информацию о первых 10 объявлениях. Реализована регистрация пользователей и аутентификация с использованием токенов. Данные могут быть добавлены в базу данных вручную или любым удобным способом.

## Установка

### Локальная установка (SQLite)

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/lolevan/farpost_api.git
    cd farpost_api/project
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv env
    source venv/bin/activate   # Для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Примените миграции и создайте суперпользователя:

    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

5. Заполните базу данных тестовыми данными:

    ```bash
    python manage.py populate_ads
    ```

6. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

### Установка с использованием Docker и PostgreSQL

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/lolevan/farpost_api.git
    cd farpost_api/project
    ```

2. Запустите сервисы с помощью Docker Compose:

    ```bash
    docker-compose up --build
    ```

## API Методы

### Регистрация пользователя

```bash
curl -X POST http://localhost:8000/api/register/ \
     -H "Content-Type: application/json" \
     -d '{
           "username": "testuser",
           "email": "testuser@example.com",
           "password": "testpassword"
         }'
```

### Получение токена аутентификации

```bash
curl -X POST http://localhost:8000/api/api-token-auth/ \
     -H "Content-Type: application/json" \
     -d '{
           "username": "admin",
           "password": "admin"
         }'
```

### Получение списка объявлений

```bash
curl -X GET http://localhost:8000/api/ads/ \
     -H "Authorization: Token YOUR_TOKEN_HERE"
```

### Получение информации об объявлении по ID

```bash
url -X GET http://localhost:8000/api/ads/1/ \
     -H "Authorization: Token YOUR_TOKEN_HERE"
```

### Создание нового объявления

```bash
curl -X POST http://localhost:8000/api/ads/ \
     -H "Authorization: Token YOUR_TOKEN_HERE" \
     -H "Content-Type: application/json" \
     -d '{
           "title": "New Ad",
           "ad_id": 11,
           "author": "Author 11",
           "views_count": 110,
           "position": 11
         }'
```

### Обновление объявления

```bash
curl -X PUT http://localhost:8000/api/ads/1/ \
     -H "Authorization: Token YOUR_TOKEN_HERE" \
     -H "Content-Type: application/json" \
     -d '{
           "title": "Updated Ad",
           "ad_id": 1,
           "author": "Updated Author",
           "views_count": 1000,
           "position": 1
         }'
```

### Удаление объявления

```bash
curl -X DELETE http://localhost:8000/api/ads/1/ \
     -H "Authorization: Token YOUR_TOKEN_HERE"
```

### Пример страниц
Приложение включает простые данные в бд.

- Логин и пароль от админки при запуске через docker:
  - Логин: admin
  - Пароль: admin

