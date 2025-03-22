from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import random
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///air_quality.db'
db = SQLAlchemy(app)

class AirQuality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    dust = db.Column(db.Float, nullable=False)
    pollen = db.Column(db.Float, nullable=False)

def generate_data():
    start_date = datetime.date(2025, 2, 14)
    for i in range(30):
        date = start_date + datetime.timedelta(days=i)
        dust = round(random.uniform(5, 27), 1)
        pollen = round((i / 30) * 10, 1)
        entry = AirQuality(date=date.strftime('%Y-%m-%d'), dust=dust, pollen=pollen)
        db.session.add(entry)
    db.session.commit()

@app.route('/')
def index():
    data = AirQuality.query.all()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if AirQuality.query.count() == 0:
            generate_data()
    app.run(host='0.0.0.0', port=5000)
