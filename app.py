from flask import Flask, redirect, url_for, render_template, request, abort
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)


client = pymongo.MongoClient("mongodb+srv://pstud:gVJQTsM2ftVKES5d@inf1039cardapuc.1cskrne.mongodb.net/?retryWrites=true&w=majority")

db = client.cardapuc

col = db.restaurantes


@app.route("/", methods=["POST", "GET"])
def landing_page():
    
    if request.method == "POST":
        
        restname = request.form["nome"]
        
        result = col.find_one({"nome": restname})

        try:

            result['_id'] = str(result['_id'])
        
        except:
            abort(404)
        return render_template("landing.html", result = result)
    
    return render_template("landing.html")

@app.route("/<name>/")
def restaurant_page(name):
    result = col.find_one({"nome": name})
    return render_template("restaurant.html", result = result)