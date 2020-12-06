from flask import Flask, render_template, url_for, redirect, url_for
from markupsafe import escape
from services.serial_control import SerialControl
from services import DerekWateringService
import os

app = Flask(__name__)

picture_posts = [{
                'filename': 'media/baby_yoda.png',
                'description': 'Baby Yoda'
            },
            {
                'filename': 'media/boba_fett.jpg',
                'description': 'Boba Fett'
            }]
            
services = DerekWateringService()

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', current_moisture=services.get_moisture(), last_water=services.get_last_water_time())

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/pictures', methods=['GET', 'POST']) 
def pictures():
    return render_template('pictures.html', title='Pictures', posts=picture_posts)

@app.route("/get_moisture")
def _get_moisture():
    return render_template('home.html', current_moisture=services.get_moisture(), last_water=services.get_last_water_time())

if __name__ == '__main__':
    app.run(debug=True)