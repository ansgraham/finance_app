# Берём официальный Python 3.12 образ
FROM python:3.12-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код проекта внутрь контейнера
COPY . .

# Команда, которая будет запускаться при старте контейнера
CMD ["python3", "-m", "app.main"]
