FROM postgres:13-alpine
# скрипт инициализации с проверкой прав
COPY --chown=postgres:postgres init.sql /docker-entrypoint-initdb.d/
RUN chmod 600 /docker-entrypoint-initdb.d/init.sql
# Запускаем от имени непривилегированного пользователя
USER postgres
EXPOSE 5432
# мониторинг
HEALTHCHECK --interval=30s --timeout=5s \
  CMD pg_isready -U airuser -d air_quality_db || exit 1