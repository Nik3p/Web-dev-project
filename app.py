from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import numpy as np
from bson.objectid import ObjectId

app=Flask(__name__)
CORS(app)

 # connecting database with flask 
app.config["MONGO_URI"]="mongodb://localhost:27017/netflex"
mongo= PyMongo(app)


@app.route ('/like',methods=['POST'])
def like():
   data = request.get_json()
   id = data["id"]
   mongo.db.athletes.update_one({"_id": Obje ctId(id)},{"$inc": {"likes": 1}})
   return jsonify({"message": "Liked!"})

   




@app.route('/search')    
def search():
   nameSearched=request.args.get("name","") 
  # an den valei name, epistrefei empty string, dld to ""
   return jsonify(list(mongo.db.athletes.find({"name": {"$regex":nameSearched,"$options":"i"}}).sort("price",-1)))
# to $regex psaxnei na vrei an mia akolouthia p exei grapsei o allos yparxei se kapoio name
# an grapseis gi sou vriskei to giannis ( gi is in giannis)
#to "$options": "i" . to option shmainei rythmiseis kai to i shmainei case Insensitive
# ara mikra kai kefalaia ola sto idio saki 
#shoutout thano an to diavazeis auto 


 # /popular: Αναπτύξτε ένα GET request που θα επιστρέφει μία λίστα με τα top-5 πιο
#δημοφιλή προϊόντα με βάση των αριθμό των Likes.
@app.route('/popular') 
def get5MostPopular():
   return jsonify(list(mongo.db.athletes.find().sort("likes",-1).limit(5)))
   # to find ta fernei ola, to sort likes-1 krataei ta top me likes apo max pros min
   #to limit 5 krataei ta 5 max likes, to list ta kanei lista kai to jsonify ta kanei json
   







if __name__=='__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)