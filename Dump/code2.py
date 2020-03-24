from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://srujandeshpande:mongodb@cluster0-e0fen.azure.mongodb.net/covid_v1?retryWrites=true&w=majority'
mongo = PyMongo(app, connect=True)

@app.route("/")
def home_page():
	data = mongo.db.UserData.find()
	return str(data)

@app.route('/xyz')
def hello_world2():
	return 'Hello, again the World!'