""" This document contains unit tests and guidelines for the code found under the pullAPIImages method in the app.py file.
It is likely that future iterations of this code (future sprints) will require reference to multiple documents for this method.
This document will continue to be updated as such.

Instructions to run:
The following tests will need to be run under the method pullMETAPI in the file app.py.
Currently the code runs on a set of ObjectIDs predetermined by the team, the test conditions below are for different 
variations of ObjectIDs.


Author: Fatimah Areola, October 23, 2020 """



#Unit Test 1.a: Invalid Input Type
#Arrange:
#in this case 2 of the values are strings, not integers
artObjectIDs = [16577,"436944",437879,436101,40081,437329,"436840",435882]
#Act:
fetchArtInformation(artObjectIDs)
#Assert:

#Unit Test 1.b: Invalid Input Type
#Arrange:
#in this case 2 of the values are strings, not integers
artObjectIDs = [16577,abcd,437879,436101,40081,437329,"436840",435882]
#Act:
fetchArtInformation(artObjectIDs)
#Assert:


#Unit Test 2.a: Missing Values
#Arrange:
#in this case one of the values is blank
artObjectIDs = [16577,,437879,436101,40081,437329,436840,435882]
#Act:
fetchArtInformation(artObjectIDs)
#Assert:

#Unit Test 2.b: Missing Values
#Arrange:
#in there is one less value in the list
artObjectIDs = [16577, 437879,436101,40081,437329,436840,435882]
#Act:
fetchArtInformation(artObjectIDs)
#Assert:

#Unit Test 3: Requested Object Does Not Exist
#This would occur when we make a request to the MET API for a feature of an artwork or ObjectID that does not exist.


#Unit Test 4: Missing Return
#This would occur when we make a request to the MET API for a feature of an object, where the object does not have that value.
#Example: requesting the image URL for an artwork that does not have a url included in its record.