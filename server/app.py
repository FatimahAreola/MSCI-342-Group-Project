from flask import Flask, request, json, jsonify
from flask_cors import CORS
import requests
import mysql.connector
import os
import random
import multiprocessing
from multiprocessing import Pool, current_process

app = Flask(__name__)
DEBUG = True
app.config.from_object(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


class DbSelector:
    def __init__(self):
        self.config = {
            "user": os.environ["DB_USER"],
            "password": os.environ["DB_PASSWORD"],
            "host": os.environ["DB_HOST"],
            "port": os.environ["DB_PORT"],
            "database": os.environ["DB_NAME"],
        }

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor(prepared=True)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.commit()
        self.connection.close()
        self.cursor.close()


@app.route("/api/hello")
def hello():
    print("Hello Request Received")
    return jsonify("Hello This is the Flask App")


# createAccount
@app.route("/api/createAccount", methods=["POST"])
def createAccount():
    username = request.get_json()["username"]
    password = request.get_json()["password"]

    with DbSelector() as d:

        query = "SELECT * FROM Users WHERE userName = %s;"

        d.cursor.execute(query, [username])

        results = d.cursor.fetchone()

        if results:
            return jsonify("username already exists"), 403

        query = "INSERT INTO Users (userName, userPassword) VALUES (%s, %s);"

        d.cursor.execute(query, [username, password])

    return jsonify(message="Successfully updated resource."), 200


# Login
@app.route("/api/Login", methods=["POST"])
def Login():
    username = request.get_json()["username"]
    password = request.get_json()["password"]

    with DbSelector() as d:

        query = "SELECT * FROM Users WHERE userName = %s AND userPassword = %s;"

        d.cursor.execute(query, [username, password])

        results = d.cursor.fetchone()

    if results:
        return jsonify(results[0], results[3].decode()), 200
    else:
        return jsonify("Invalid Username or Password"), 401


""" The following code issues a call to the MET Api, and returns a json object, 
with the details of 8 pre-determined works of art so that they can be formatted for gameplay.
 """


def fetchArtInformation(i):

    # pulls the required information from the MET's API
    apiResponse = requests.get(
        "https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(i)
    )
    artDetails = apiResponse.json()
    # We add another object to the Cardset dictionary for each art piece, containing info on Name, ObjectID, URL and status
    cardSet = {
        "ObjectID": str(i),
        "artName": artDetails["title"],
        "artUrl": artDetails["primaryImage"],
        "artistName": artDetails["artistDisplayName"],
        "artCulture": artDetails["culture"],
        "artPeriod": artDetails["period"],
        "birthYear": artDetails["artistBeginDate"],
        "deathYear": artDetails["artistEndDate"],
        "active": False,
        "status": False,
    }
    # Returns a Json object
    return cardSet


def selectArt (selectedArtist):

    artArray = [[437112,438008,437135,438004,437133,437127,437124,438007],
    [336327,436527,436530,436531,436524,436534,437998,436529],
    [437397,437392,337491,437390,437402,437396,437389,437398],
    [10793,10786,10795,10796,10794,10790,10788,10798],
    [10154,10155,10151,10150,10158,21186,10156,10149],
    [435882,435885,437990,435871,435874,435873,435870,435879],
    [786115,370826,365307,337070,786093,785991,785974,691010],
    [488319,352408,369076,360146,369093,369079,369096,359991]]
    
    artists= ['Monet', 'VanGogh', 'Rembrandt','Durand','Bierstadt','Cezanne','Edouart','Kandinsky']
    
    for a in artists:
        if selectedArtist == artists[a]:
            artistIdx=artists.index(a) 
            artObjectIDs=artArray[artistIdx]
    

    #we need to figure out which
    if (selectedArtist == "") or (selectedArtist is None):
        for i in range (8):
            x=0
            y=0
            while x==y:
                x=random.randint(0,7)
                y=random.randint(0,7)

        artObjectIDs[i]=artArray[x][y]

    return (artObjectIDs)


@app.route("/api/MetAPI")
def pullMETAPI():
    print("Met API Method:")

    # These are the ObjectIDs of 8 pieces we selected for this demo.
    # For future iterations of the game, these objectIDs will need to be selected by the system.
    # Multiprocessing here
    selectedArtist = request.get_json()["selectArtist"]
    artObjectIDs = selectArt(selectedArtist) #temporary
    numPieces = len(artObjectIDs)
    p = Pool(numPieces)
    artPieces = p.map(fetchArtInformation, artObjectIDs)

    for x in range(numPieces):
        pointer = artPieces[x]
        pointer['cardId']=x+1
        cardSet = {
            "cardId": x + numPieces + 1,
            "ObjectID": artPieces[x].get("ObjectID"),
            "artName": artPieces[x].get("artName"),
            "artUrl": artPieces[x].get("artUrl"),
            "artistName": artPieces[x].get("artistDisplayName"),
            "artCulture": artPieces[x].get("culture"),
            "artPeriod": artPieces[x].get("period"),
            "birthYear": artPieces[x].get("artistBeginDate"),
            "deathYear": artPieces[x].get("artistEndDate"),
            "active": False,
            "status": False,
        }
        artPieces.append(cardSet)

    return jsonify(artPieces)


@app.route("/api/updateBestTime", methods=["POST"])
def updateTime():
    userID = request.get_json()["userId"]
    bestTime = request.get_json()["bestTime"]

    with DbSelector() as d:

        query = "UPDATE Users SET Users.bestTime = %s WHERE userId = %s;"

        d.cursor.execute(query, [bestTime, userID])

        results = d.cursor.rowcount

    if results:
        return jsonify(results), 200
    else:
        return jsonify("Error updating best time"), 401


@app.route("/api/ping")
def ping():
    return jsonify("pong")


if __name__ == "__main__":
    app.run()
