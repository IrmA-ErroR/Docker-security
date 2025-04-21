from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Конфигурация базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://airuser:airpassword@db/air_quality_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class AirQuality(db.Model):
    __tablename__ = 'air_quality'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True, nullable=False)
    pollen_level = db.Column(db.Integer, nullable=False)
    dust_pm25 = db.Column(db.Float, nullable=False)
    dust_pm10 = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    wind_speed = db.Column(db.Float)

@app.route('/')
def index():
    data = AirQuality.query.order_by(AirQuality.date).all()
    dates = [record.date.strftime('%Y-%m-%d') for record in data]
    pollen = [record.pollen_level for record in data]
    pm25 = [record.dust_pm25 for record in data]
    pm10 = [record.dust_pm10 for record in data]
    
    return render_template('index.html', 
                         dates=dates,
                         pollen=pollen,
                         pm25=pm25,
                         pm10=pm10,
                         records=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)