from flask import Flask, request, jsonify, make_response, send_file
import json
import requests
import mysql.connector

app = Flask(__name__)


@app.route("/api/hello")
def hello():
    print("Hello Request Received")
    return "Hello This is the Flask App"


# createAccount
@app.route("/api/createAccount", methods=["POST"])
def createAccount():
    username = request.get_json()["username"]
    password = request.get_json()["password"]

    config = {
        "user": "root",
        "password": "sherlockeD123",
        "host": "db",
        "port": "3306",
        "database": "MSCI",
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    query = "SELECT * FROM Users WHERE userName = %s;"

    cursor.execute(query, [password])

    results = cursor.fetchone()

    if results:
        return jsonify("username already exists")

    cursor = connection.cursor()

    query = "INSERT INTO Users (userName, userPassword) VALUES (%s, %s);"

    cursor.execute(query, [username, password])

    print(cursor)

    return jsonify(message="Successfully updated resource."), 200


""" The following code issues a call to the MET Api, and returns a json object, 
with the details of 8 pre-determined works of art so that they can be formatted for gameplay.
 """


def fetchArtInformation(artObjectIDs):
    # Define index, and Cardset dictionary
    idx = 0
    cardSet = {}
    # This for loop goes through all IDs provided in the list of art pieces chosen and pulls the required information about them from the MET's API
    for i in artObjectIDs:
        apiResponse = requests.get(
            "https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(i)
        )
        artDetails = apiResponse.json()
        # We add another object to the Cardset dictionary for each art piece, containing info on Name, ObjectID, URL and status
        cardSet[idx] = {
            "cardId": idx + 1,
            "ObjectID": str(i),
            "artName": artDetails["title"],
            "artURL": artDetails["primaryImage"],
            "active": False,
            "status": False,
        }
        idx += 1
    # Returns a nested Json object, with multiple artCards inside
    return json.dumps(cardSet)


@app.route("/api/MetAPI")
def pullMETAPI():
    print("Met API Method:")

    # These are the ObjectIDs of 8 pieces we selected for this demo.
    # For future iterations of the game, these objectIDs will need to be selected by the system.
    artObjectIDs = [16577, 436944, 437879, 436101, 40081, 437329, 436840, 435882]
    return fetchArtInformation(artObjectIDs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
