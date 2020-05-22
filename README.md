Editor: Davis Bosworth dboswor2@uoregon.edu

## Building/Running my Program in terminal
$ docker-compose build

$ docker-compose up

## Test Cases

test 1 (Normal case):  
	Entering 200, 400 ,600 km into the control distance km input will receive
 	open_time and close_time as the outputs for each distance.
	Once the submit button is selected the webpage is cleared for new entries and 
	open time and close time are sent to the database.
	This can be verified in the Javascript Console. Once the display button is clicked
	a new tab will open with a table of all logged open and close times.


test 2 (Edge case): 
	If 0 entries are input for the control distances and the display button is 
	selected an error page (none.html) will load; prompting the user to enter a 
	distance. The webpage will contain a link back to the home page.
	The same functionality is invoked when the submit button is selected and
	there are 0 entries.

# Project 5: Brevet time calculator with Ajax and MongoDB

Simple list of controle times from project 4 stored in MongoDB database.

## What is in this repository

You have a minimal implementation of Docker compose in DockerMongo folder, using which you can connect the flask app to MongoDB (as demonstrated in class). Refer to the lecture slide "05a-Table-driven.pdf" and "05b-Docker-Compose.pdf" (dated 10/24 and 10/26). You'll also need MongoCommands.txt. Solved acp_times.py file is in piazza under resources tab! 

## Functionality you'll add

~Submit clears the webpage for new entries and pushes the current entries to the database.
~Display loads a new page with a table of all open and close times logged during the current session.

You will reuse *your* code from project 4 (https://bitbucket.org/UOCIS322/proj4-brevets/). Recall: you created a list of open and close controle times using AJAX. In this project, you will create the following functionality. 1) Create two buttons ("Submit") and ("Display") in the page where have controle times. 2) On clicking the Submit button, the control times should be entered into the database. 3) On clicking the Display button, the entries from the database should be displayed in a new page. 

Handle error cases appropriately. For example, Submit should return an error if there are no controle times. One can imagine many such cases: you'll come up with as many cases as possible.


