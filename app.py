from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import numpy as np

app=Flask(__name__)
CORS(app)

 # connecting database with flask 
app.config["MONGO_URI"]="mongodb://localhost:27017/netflex"
mongo= PyMongo(app)


@app.route ('/like',methods=['POST']) # tha to kanei o nikos 
def like():
   data.request




@app.route('/search')     # tha to kanei o giannis 
def search():
  mongo.db.netflex.find({"$search":"value"}       ).list().


@app.route('/popular') # tha to kanei o giannis 
def popular():
   







if __name__=='__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)