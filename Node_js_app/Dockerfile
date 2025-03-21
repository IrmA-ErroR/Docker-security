# базовый образ
FROM node:10-alpine
RUN mkdir -p /src/app
WORKDIR /src/app
ONBUILD COPY package.json /src/app/package.json
# установка зависимостей через npm
ONBUILD RUN npm install
COPY . /src/app
# порт
EXPOSE 3000
# запуск приложения
CMD ["npm", "start"]
