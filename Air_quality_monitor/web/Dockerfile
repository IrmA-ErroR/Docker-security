FROM python:3.13-alpine
RUN apk update sqlite-libs && apk upgrade sqlite-libs
# Создаем непривилегированного пользователя
RUN adduser -D appuser
USER appuser
WORKDIR /app
# зависимости
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt && \
    pip3 cache purge
# Запускаем от appuser и ограничиваем возможности
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
# Защищенные настройки Flask
ENV FLASK_ENV=production \
    FLASK_DEBUG=0
CMD ["python3", "app.py"]