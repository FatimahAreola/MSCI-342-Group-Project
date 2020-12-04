# Testing
## This folder contains unit tests for code written for this project. This document consists of guidelines on how to run these tests.

## Unit Tests for PR 32: Improve Home Page and PR 33: Logout Button 

## Unit Test for ALL Buttons
1. Navigate to "Home" compoenent
2. Identify code for buttons: ```<button v-on:click="routeToGame" class="play-button options"> RANDOM PLAY </button>``` 
3. Alter "RANDOM PLAY" code to read any text. Example "hello"
4. Save and route to application locally. To do so, follow instructions on project README file
5. Home page should display button with name "hello"
6. Note that this unit test can be used for all buttons on the home page

## 2. Unit Test for ALL Page Routes
1. Navigate to "Home" compoenent
2. Identify code for route functions: ```routeToProfile: function () { this.$router.push("/profile"); };``` 

3. Add ```console.log("hello");``` on line above ```};```
4. Save and route to application locally. To do so, follow instructions on project README file
5. Click on "MY PROFILE" button, see result on JavaScript console -> should see hello executed
6. Note that this unit test can be used for all buttons on the home page