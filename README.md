Editor: Davis Bosworth dboswor2@uoregon.edu

## Building/Running my Program in terminal
$ docker-compose build
$ docker-compose up

## Test Cases
Two test cases for the submit and display buttons can be found in the text file tests.txt.

# Project 5: Brevet time calculator with Ajax and MongoDB

Simple list of controle times from project 4 stored in MongoDB database.

## What is in this repository

You have a minimal implementation of Docker compose in DockerMongo folder, using which you can connect the flask app to MongoDB (as demonstrated in class). Refer to the lecture slide "05a-Table-driven.pdf" and "05b-Docker-Compose.pdf" (dated 10/24 and 10/26). You'll also need MongoCommands.txt. Solved acp_times.py file is in piazza under resources tab! 

## Functionality you'll add

~Submit clears the webpage for new entries and pushes the current entries to the database.
~Display loads a new page with a table of all open and close times logged during the current session.

You will reuse *your* code from project 4 (https://bitbucket.org/UOCIS322/proj4-brevets/). Recall: you created a list of open and close controle times using AJAX. In this project, you will create the following functionality. 1) Create two buttons ("Submit") and ("Display") in the page where have controle times. 2) On clicking the Submit button, the control times should be entered into the database. 3) On clicking the Display button, the entries from the database should be displayed in a new page. 

Handle error cases appropriately. For example, Submit should return an error if there are no controle times. One can imagine many such cases: you'll come up with as many cases as possible.


