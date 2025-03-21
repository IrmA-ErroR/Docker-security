const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const Chart = require('chart.js');
const path = require('path');
const { stringify } = require('querystring');

const app = express();
const port = 3000;

// базa данных
let db = new sqlite3.Database('./database.db', (err) => {
  if (err) {
    console.error("Ошибка при подключении к базе данных:", err.message);
  } else {
    console.log("Подключение к базе данных установлено");
  }
});


db.serialize(() => {
  db.run("CREATE TABLE IF NOT EXISTS air_quality (date TEXT, air_quality INTEGER, pollen_percentage INTEGER, dust_percentage INTEGER)");

  // Генерация данных
  const startDate = new Date(2025, 1, 14);
  const endDate = new Date(2025, 2, 14);
  let currentDate = startDate;

  while (currentDate <= endDate) {
    const airQuality = Math.floor(Math.random() * 22) + 1;
    const pollen = Math.floor(Math.random() * 22) + 1;
    const dust = Math.floor(Math.random() * 22) + 1;

    db.run("INSERT INTO air_quality (date, air_quality, pollen_percentage, dust_percentage) VALUES (?, ?, ?, ?)",
      [currentDate.toISOString().split('T')[0], airQuality, pollen, dust]);

    currentDate.setDate(currentDate.getDate() + 1);
  }
});

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));


app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    db.all("SELECT * FROM air_quality ORDER BY date ASC", [], (err, rows) => {
      if (err) {
        console.error("Ошибка при получении данных из базы:", err.message);
        throw err;
      }
  
      // Проверка на пустые данные
      if (rows.length === 0) {
        console.log('Нет данных в базе');
      }
  
      // Подготовка данных для графика
      const dates = rows.map(row => row.date);
      const airQualityData = rows.map(row => row.air_quality);
      const pollenData = rows.map(row => row.pollen_percentage);
      const dustData = rows.map(row => row.dust_percentage);
  
      // Отправляем данные в шаблон для рендеринга
      res.render('index', {
        dates: JSON.stringify(dates),
        airQualityData: JSON.stringify(airQualityData),
        pollenData: JSON.stringify(pollenData),
        dustData: JSON.stringify(dustData)
      });
    });
  });
  

// Запуск сервера
app.listen(port, () => {
  console.log(`Сервер запущен на порту ${port}`);
});
