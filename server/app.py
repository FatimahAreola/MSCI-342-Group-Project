from flask import Flask, json, jsonify
from flask_cors import CORS
import requests
import mysql.connector

app = Flask(__name__)
DEBUG = True
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/api/hello')
def hello():
    print('Hello Request Received')
    return jsonify('Hello This is the Flask App')



""" The following code issues a call to the MET Api, and returns a json object, 
with the details of 8 pre-determined works of art so that they can be formatted for gameplay.
 """

def fetchArtInformation(artObjectIDs):
 #Define index, and Cardset dictionary
    idx=0
    cardSet={}  
#This for loop goes through all IDs provided in the list of art pieces chosen and pulls the required information about them from the MET's API
    for i in artObjectIDs:
        apiResponse = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(i))
        artDetails = apiResponse.json()
#We add another object to the Cardset dictionary for each art piece, containing info on Name, ObjectID, URL and status
        cardSet[idx]={
        'cardId': idx+1,
        'ObjectID': str(i),
        'artName': artDetails["title"],
        'artURL': artDetails["primaryImage"],
        'active':  False,
        'status': False
        }
        idx+=1
#Returns a nested Json object, with multiple artCards inside
    return (json.dumps(cardSet))


@app.route('/api/MetAPI')
def pullMETAPI():
    print('Met API Method:')

#These are the ObjectIDs of 8 pieces we selected for this demo.
#For future iterations of the game, these objectIDs will need to be selected by the system.
    artObjectIDs = [16577,436944,437879,436101,40081,437329,436840,435882]
    return(fetchArtInformation(artObjectIDs))


@app.route('/api/ping')
def ping():
    return jsonify('pong')


if __name__ == '__main__':
    app.run()
