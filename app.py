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
   nameSearched=request.args.get("name","")  #an den valei name, epistrefei empty string, dld to ""
   query={"name": {"$regex":nameSearched,"$options":"i"}}
   results=mongo.db.athletes.find(query).sort("price",-1)
   clean_results=[]
   for athlete in results:
      athlete['_id']=str(athlete['_id'])
      clean_results.append(athlete)
   return jsonify(clean_results)


# to $regex psaxnei na vrei an mia akolouthia p exei grapsei o allos yparxei se kapoio name
# an grapseis gi sou vriskei to giannis ( gi is in giannis)
#to "$options": "i" . to option shmainei rythmiseis kai to i shmainei case Insensitive
# ara mikra kai kefalaia ola sto idio saki 
# to id tou athlete to kanume string gt to _id ths mongodb einai special object pou den to diavazei h py3
#shoutout thano an to diavazeis auto 


 # /popular: Αναπτύξτε ένα GET request που θα επιστρέφει μία λίστα με τα top-5 πιο
#δημοφιλή προϊόντα με βάση των αριθμό των Likes.
@app.route('/popular') # tha to kanei o giannis 
def get5MostPopular():
   return jsonify(list(mongo.db.athletes.find().sort("likes",-1).limit(5)))
   # to find ta fernei ola, to sort likes-1 krataei ta top me likes apo max pros min
   #to limit 5 krataei ta 5 max likes, to list ta kanei lista kai to jsonify ta kanei json
   








if __name__=='__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)