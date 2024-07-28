#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/hbnb')
def hbnb():
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port)
