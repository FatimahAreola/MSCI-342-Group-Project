""" This document contains unit tests and guidelines for the code found under the pullAPIImages method in the app.py file.
It is likely that future iterations of this code (future sprints) will require reference to multiple documents for this method.
This document will continue to be updated as such.

Instructions to run:
The following tests will need to be run under the method pullMETAPI in the file app.py.
Currently the code runs on a set of ObjectIDs predetermined by the team, the test conditions below are for different 
variations of ObjectIDs.


Author: Fatimah Areola, 
Created: October 23, 2020
Updated: November 21, 2020
    """
from flask import Flask, request, json, jsonify
from flask_cors import CORS
import requests
import mysql.connector
import os
import random
import multiprocessing
from multiprocessing import Pool, current_process

def fetchArtInformation(i):

    # pulls the required information from the MET's API
    apiResponse = requests.get(
        "https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(i))
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

""" The following test unit tests cover an early iteration of the fetchArtInformation method.
Author: Fatimah Areola, 
Created: October 23, 2020
    """
#Unit Test 1.a: Invalid Input Type
#Arrange:
#in this case 2 of the values are strings, not integers
artObjectIDs = [16577,"436944",437879,436101,40081,437329,"436840",435882]
#Act:
p = Pool(len(artObjectIDs))
artPieces = p.map(fetchArtInformation, artObjectIDs)
print(artPieces)
#Assert:
    #Expected Result: Attribute Error
    #Actual Result: Attribute Error

#Unit Test 1.b: Invalid Input Type
#Arrange:
#in this case 2 of the values are strings, not integers
artObjectIDs = [16577,"abcd",437879,436101,40081,437329,"436840",435882]
#Act:
p = Pool(len(artObjectIDs))
artPieces = p.map(fetchArtInformation, artObjectIDs)
print(artPieces)
#Assert:
    #Expected Result: AttributionError
    #Actual Result: AttributionError

#Unit Test 2.a: Missing Values
#Arrange:
#in this case one of the values is blank
artObjectIDs = [16577,,437879,436101,40081,437329,436840,435882]
#Act:
p = Pool(len(artObjectIDs))
artPieces = p.map(fetchArtInformation, artObjectIDs)
print(artPieces)
#Assert:
    #Expected Result: Code does not compile
    #Actual Result: Code does not compile

#Unit Test 2.b: Missing Values
#Arrange:
#there is one less value in the list
artObjectIDs = [16577, 437879,436101,40081,437329,436840,435882]
#Act:
p = Pool(len(artObjectIDs))
artPieces = p.map(fetchArtInformation, artObjectIDs)
print(artPieces)
#Assert:
    #Expected Result: AttributeError
    #Actual Result: AttributeError

#Unit Test 3: Requested Object Does Not Exist
#This would occur when we make a request to the MET API for a feature of an artwork or ObjectID that does not exist.
#Arrange:
#there are two "made up" values in the list
artObjectIDs = [00000,12345,436101,40081,437329,436840,435882]
#Act:
p = Pool(len(artObjectIDs))
artPieces = p.map(fetchArtInformation, artObjectIDs)
print(artPieces)
#Assert:
    #Expected Result: Request.exceptions error Max retries exceeded with url
    #Actual Result: Request.exceptions error Max retries exceeded with url


#Unit Test 4: Missing Return
#This would occur when we make a request to the MET API for a feature of an object, where the object does not have that value.
#Example: requesting the image URL for an artwork that does not have a url included in its record.
#Arrange:
#Each of the below IDs do not have a value for the ImageURL field.
artObjectIDs = [437112,438008,437135,438004,437133,437127,437124,438007]
#Act:
p = Pool(len(artObjectIDs))
artPieces = p.map(fetchArtInformation, artObjectIDs)
print(artPieces)
#Assert:
    #Expected Result: null or "" alternates between the two depending on the artwork referenced
    #Actual Result: "" for all object IDs above  

""" The following test unit tests cover the selectArt method.
Author: Fatimah Areola, 
Created: November 21, 2020
    """
from flask import Flask, request, json, jsonify
from flask_cors import CORS
import requests
import mysql.connector
import os
import random
import multiprocessing
from multiprocessing import Pool, current_process


def selectArt (selectedArtist):

    artArray = [[438821,436449,437999,438001,436448,337858,344577,337172],
    [336327,436527,436530,436531,436524,436534,437998,436529],
    [437397,437392,337491,437390,437402,437396,437389,437398],
    [10793,10786,10795,10796,10794,10790,10788,10798],
    [10154,10155,10151,10150,10158,21186,10156,10149],
    [435882,435885,437990,435871,435874,435873,435870,435879],
    [786115,370826,365307,337070,786093,785991,785974,691010],
    [752047,11865,11859,11862,11866,11860,11863,11872]]
    
    artists= ["Paul Gauguin", "Vincent van Gogh", "Rembrandt", "Asher Brown Durand", "Albert Bierstadt", "Paul Cézanne", "Auguste Edouart", "Frederic Remington"]
    
    for a in range(8):
        if selectedArtist == artists[a]:
            artistIdx=artists.index(artists[a]) 
            artObjectIDs=artArray[artistIdx]f
            return (artObjectIDs)
    
    #If none of the listed artists have been selected, a random game is generated
    artObjectIDs = [] 
    for i in range(8):
        x=0
        y=0
        while x==y:
            x=random.randint(0,7)
            y=random.randint(0,7)
          
        artObjectIDs.append(artArray[x][y])
    return (artObjectIDs)



#Unit Test 1.a: Invalid Input Type
#Arrange:
#in this an integer is passed in place of the string meant to represent the selected artist
selectedArtist = 12345
#Act:
print(selectArt(selectedArtist))
#Assert:
    #Expected Result: Game executes with randomly generated array of art
    #Actual Result: [436448, 436448, 436449, 438001, 786115, 437390, 10788, 11860]

#Unit Test 2.a: Missing Values
#Arrange:
#in this case an empty string has been passed as the selected artist
selectedArtist = ''

#Act:
print(selectArt(selectedArtist))

#Assert:
    #Expected Result: Game executes with randomly generated array of art
    #Actual Result:  [785991, 337858, 438001, 11859, 437402, 11866, 437397, 10154]

#Unit Test 2.b: Missing Values
#Arrange:
#in this case a null value has been passed as the selected artist
selectedArtist = null
#Act:
print(selectArt(selectedArtist))
#Assert:
    #Expected Result: Game executes with randomly generated array of art
    #Actual Result: [435885, 435874, 438001, 11862, 10798, 337858, 11862, 786115]

#Unit Test 2.c: Missing Values
#Arrange:
#in this case no value has been passed as the selected artist
selectedArtist =

#Act:
print(selectArt(selectedArtist))

#Assert:
    #Expected Result: Code will not compile
    #Actual Result: Code does not compile


#Unit Test 3: Requested Object Does Not Exist
#This would occur when a string is passed that is not an identified artist in the game
#Arrange:
selectedArtist = 'Claude Monet'

#Act:
print(selectArt(selectedArtist))

#Assert:
    #Expected Result: Game executes with randomly generated array of art
    #Actual Result: [436534, 10793, 370826, 365307, 10795, 10798, 10155, 437396]