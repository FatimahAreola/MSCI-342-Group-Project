from flask import Flask, json
import requests
#import mysql.connector

app = Flask(__name__)



@app.route('/api/hello')
def hello():
    print('Hello Request Received')
    return ('Hello')

#Selected 8 Random Pieces Just to Get the Code to work
artObjectIDs = [16577,436944,437879,436101,40081,437329,436840,435882]


#Define JSON CardSet Object and JSON Card Object
cardSet={}

@app.route('/api/MetTest')
def returnAPIImages():
    print('Hello Request Received')
    #return 'Hello This is the Flask App2'
    #with request.urlopen("https://collectionapi.metmuseum.org/public/collection/v1/objects/45734")
#Loop through CardSet
    for i in artObjectIDs:
        cardSet.append(populateCardDetails(i))
    
    return (cardSet)


#Populate Cards
def populateCardDetails(i):
    apiResponse = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + i.toString()).json()
#artDetails = apiResponse.json()
    artCard={}
#Hard coded the line below because I just want to make sure stuff works first
    artCard['CardID'] = 1
    artCard['ObjectID'] = i.toString()
    artCard['artName'] = apiResponse["title"]
#I'm assuming by artURL you mean Image URL
    artCard['artURL'] = apiResponse["primaryImage"]
    artCard['active'] = false
    artCard['status'] = false
    return (artCard)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
