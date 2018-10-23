# Explora
A web based application that analyses college projects using text mining concepts
This application is created for colleges and universities where one keep a 'one-stop' record for all research projects and students and faculty can search the projects present in the database

#Technologies Used
- Frontend : HTML, CSS, jQuery
- Backend : Python CGI
- Database : MySQL

## Project Upload
It allows users to store their project details in the application database by filling out a form.The user then has to enter project details.
The application analyses the title and abstract of the project, from where key word extraction module identifies the important keywords and displays it to the user from where the user can select the appropriate ones. Finally the user can submit the project to the application

## Project Search
It allows users to search projects by using following parameters:
- By Title
- By Domain
- By Faculty
- By keywords ( tags )
- Searching similar projects
For every successful search, the results will be displayed from where you can click on respective project to get it's details

## Faculty Login
Faculty access has been provided to the application where the faculty can do the following:
- Review projects under faculty
- can change status of the project
- can change password

## Database Requirements
Following tables are maintained in MySQL :
- projects : where all the project details will be stored
- keywords : list of keywords that you want to extract out of the context
- faculty : where all faculty names, login id and password can be stored
Schema of the database can be found in the [database] (https://github.com/rishavmedhi/Explora/) folder
