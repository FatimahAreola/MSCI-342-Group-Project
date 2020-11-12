from flask import Flask, request, json, jsonify
from flask_cors import CORS
import requests
import mysql.connector
import os

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

    print("username", username)
    print("password", password)

    config = {
        "user": "root",
        "password": "sherlockeD123",
        "host": "db",
        "port": "3306",
        "database": "MSCI",
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    query = "SELECT * FROM Users WHERE userName = %s AND userPassword = %s;"

    cursor.execute(query, [username, password])

    results = cursor.fetchone()

    if results:
        return jsonify(results[0]), 200
    else:
        return jsonify("Invalid Username or Password"), 401


""" The following code issues a call to the MET Api, and returns a json object, 
with the details of 8 pre-determined works of art so that they can be formatted for gameplay.
 """


def fetchArtInformation(i):
    # Numbers from 1 to number of images, identified by the number of processes created
    idx = current_process()._identity[0]
    # pulls the required information from the MET's API
    apiResponse = requests.get(
        "https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(i)
    )
    artDetails = apiResponse.json()
    # We add another object to the Cardset dictionary for each art piece, containing info on Name, ObjectID, URL and status
    cardSet = {
        "cardId": idx,
        "ObjectID": str(i),
        "artName": artDetails["title"],
        "artUrl": artDetails["primaryImage"],
        "active": False,
        "status": False,
    }
    # Returns a Json object
    return cardSet


@app.route("/api/MetAPI")
def pullMETAPI():
    print("Met API Method:")

    # These are the ObjectIDs of 8 pieces we selected for this demo.
    # For future iterations of the game, these objectIDs will need to be selected by the system.
    artObjectIDs = [16577, 436944, 437879, 436101, 40081, 437329, 436840, 435882]
    numPieces = len(artObjectIDs)

    # Multiprocessing here
    p = Pool(numPieces)
    artPieces = p.map(fetchArtInformation, artObjectIDs)

    for x in range(numPieces):
        cardSet = {
            "cardId": x + numPieces + 1,
            "ObjectID": artPieces[x].get("ObjectID"),
            "artName": artPieces[x].get("artName"),
            "artUrl": artPieces[x].get("artUrl"),
            "active": False,
            "status": False,
        }
        artPieces.append(cardSet)

    return jsonify(artPieces)


@app.route("/api/ping")
def ping():
    return jsonify("pong")


if __name__ == "__main__":
    app.run()
