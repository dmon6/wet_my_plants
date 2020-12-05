from flask import Flask, render_template, url_for
from markupsafe import escape
from services.serial_control import SerialControl
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

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/pictures', methods=['GET', 'POST']) 
def pictures():
    return render_template('pictures.html', title='Pictures', posts=picture_posts)

if __name__ == '__main__':
    app.run(debug=True)