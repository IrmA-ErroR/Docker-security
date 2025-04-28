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
    
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
CMD curl -f http://localhost:5000/health || exit 1

CMD ["python3", "app.py"]