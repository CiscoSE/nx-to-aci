import os
from flask import Flask
import flask_sijax


app = Flask(__name__)

app.config["SIJAX_STATIC_PATH"] = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app.config["SIJAX_JSON_URI"] = '/static/js/sijax/json2.js'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['BOOTSTRAP_USE_MINIFIED'] = True
app.secret_key = 'A0Zr4FcD2K3LjmwS918jHH!jm84$#ssaWQsif!1'
from app import views

flask_sijax.Sijax(app)
