# Testing
## This folder contains unit tests for code written for this project. This document consists of guidelines on how to run these tests.

# Unit Tests for PR 32: Improve Home Page

# 1. Unit Tests for all Buttons
# a. Go to "Home" compoenent
# b. Identify code for buttons:
# <button v-on:click="routeToGame" class="play-button options">
#   RANDOM PLAY
# </button>
# c. Alter "RANDOM PLAY" code to read any text. Example "Hello"
# d. Save and route to application locally. To do so, follow instructions on project README file
# e. Home page should display button with name "Hello"