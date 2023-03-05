from flask import Flask
from flask import request
from pymongo import MongoClient
from routes.endpoints import lc_app

app = Flask(__name__)
app.register_blueprint(lc_app)


app.run()