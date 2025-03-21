FROM node:latest
WORKDIR /usr/src/app
COPY . .

RUN npm install express chart.js sqlite3 ejs
EXPOSE 3000
CMD ["node", "app.js"]
