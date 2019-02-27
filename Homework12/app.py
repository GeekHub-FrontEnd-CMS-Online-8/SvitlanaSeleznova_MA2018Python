from flask import Flask, render_template, request
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locations.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    zip_code = request.form['zip_code']
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+zip_code+'&sensor=true&key=AIzaSyCDKSQdglP_kfxPsZsDfqXxO0T193LJZfs'

    params = {
        'address': zip_code,
        'sensor': 'true',
        'key': 'AIzaSyCDKSQdglP_kfxPsZsDfqXxO0T193LJZfs'
    }
    req = requests.get(url, params=params)
    res = req.json()
    address = res['results'][0]['formatted_address']
    latitude = res['results'][0]['geometry']['location']['lat']
    lat = str(latitude)
    longitude = res['results'][0]['geometry']['location']['lng']
    long = str(longitude)
    from models import Locations
    new_zip_code = Locations(zip_code=zip_code, address=address, latitude=lat, longitude=long)

    db.session.add(new_zip_code)
    db.session.commit()

    return render_template('result.html', zip_code=zip_code, address=address, lat=lat, long=long)

@app.route('/show-results')
def show_results():
    from models import Locations
    locations = Locations.query.all()
    return render_template('show_results.html', locations=locations)

if __name__ == '__main__':
    app.run(debug=True)