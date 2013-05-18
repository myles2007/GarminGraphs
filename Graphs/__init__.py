from flask import Flask

DEBUG = True
UPLOAD_FOLDER = '/Users/mylesloffler/GarminGraphs/Graphs/activities/'
ALLOWED_EXTENSIONS = set(['gpx', 'pdf', 'png', 'jpg'])

app = Flask(__name__)
app.config['DEBUG'] = DEBUG
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

import Graphs.views


