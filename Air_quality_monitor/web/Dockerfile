FROM python:3.9-slim
# Создаем непривилегированного пользователя
RUN useradd -m appuser
USER appuser
WORKDIR /app
# зависимости
COPY . .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip cache purge
# Запускаем от appuser и ограничиваем возможности
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
# Защищенные настройки Flask
ENV FLASK_ENV=production \
    FLASK_DEBUG=0
CMD ["python", "app.py"]