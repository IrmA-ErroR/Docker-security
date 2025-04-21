FROM python:3.9-slim
# Создаем непривилегированного пользователя
RUN useradd -m appuser && \
    mkdir -p /app && \
    chown appuser:appuser /app
WORKDIR /app
# зависимости
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip cache purge
# Копируем код от имени appuser
COPY --chown=appuser:appuser . .
# Запрещаем запись в файловую систему (read-only)
RUN chmod -R 555 /app && \
    mkdir -p /app/instance && \
    chmod 700 /app/instance
# Запускаем от appuser и ограничиваем возможности
USER appuser
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
# Защищенные настройки Flask
ENV FLASK_ENV=production \
    FLASK_DEBUG=0
CMD ["python", "app.py"]