# Testing
## This folder contains unit tests for code written for this project. This document consists of guidelines on how to run these tests.

# Unit Tests for PR 32: Improve Home Page and PR 33: Logout Button 

# 1. Unit Test for ALL Buttons
# a. Navigate to "Home" compoenent
# b. Identify code for buttons:
# <button v-on:click="routeToGame" class="play-button options">
#   RANDOM PLAY
# </button>
# c. Alter "RANDOM PLAY" code to read any text. Example "hello"
# d. Save and route to application locally. To do so, follow instructions on project README file
# e. Home page should display button with name "hello"
# f. Note that this unit test can be used for all buttons on the home page

# 2. Unit Test for ALL Page Routes
# a. Navigate to "Home" compoenent
# b. Identify code for route functions:
# routeToProfile: function () {
#		this.$router.push("/profile");
#	},
# c. Add "console.log("hello");" on line above "};"
# d. Save and route to application locally. To do so, follow instructions on project README file
# e. Click on "MY PROFILE" button, see result on JavaScript console -> should see hello executed
# f. Note that this unit test can be used for all buttons on the home page