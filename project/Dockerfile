# Используем официальный образ Python
FROM python:3.9-slim


# Устанавливаем зависимости для PostgreSQL
RUN apt-get update && apt-get install -y postgresql-client

# Создаем и переходим в рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости проекта
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Устанавливаем переменные окружения
ENV DOCKERIZED=true
ENV POSTGRES_DB=farpost
ENV POSTGRES_USER=farpost_user
ENV POSTGRES_PASSWORD=farpost_password
ENV POSTGRES_HOST=db

# Копируем скрипт ожидания
COPY wait-for-postgres.sh /wait-for-postgres.sh
RUN chmod +x /wait-for-postgres.sh

# Открываем порт 8000 для доступа к приложению
EXPOSE 8000

# Запускаем сервер
CMD ["/wait-for-postgres.sh", "db", "python manage.py runserver 0.0.0.0:8000"]
