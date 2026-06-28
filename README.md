# Overview


This project is a Cloud To-Do List web application built with Python using the Flask framework. The application integrates with a MongoDB Atlas cloud database to store and manage tasks. Users can create, view, edit, and delete tasks through a simple web interface. Each task consists of a title and a completion status, and all changes are saved directly to the cloud database, allowing data to persist between sessions.
To use the program, start the Flask application and open the provided local web address in a web browser. From the home page, users can add new tasks, edit existing tasks, mark tasks as completed, and delete tasks they no longer need. Every action is immediately reflected in the MongoDB Atlas database, demonstrating full Create, Read, Update, and Delete (CRUD) functionality.

The purpose of this project was to learn how to develop a Python web application that communicates with a cloud-hosted database. Through this project, I gained experience using Flask to build a web application and PyMongo to interact with MongoDB Atlas. The project demonstrates how cloud databases can be used to store persistent data without requiring a locally hosted database server while implementing the essential CRUD operations required for database-driven applications.

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of the cloud database.}

[Software Demo Video](https://youtu.be/D2ECkQSvZ_M)

# Cloud Database

This project uses MongoDB Atlas, a cloud-hosted NoSQL database service. MongoDB Atlas stores data as JSON-like documents rather than traditional rows and columns, making it flexible and easy to use for web applications. The application connects to the database using the PyMongo library and a secure connection string stored in a .env file. All task data is stored remotely in MongoDB Atlas, allowing the application to retrieve and update information without maintaining a local database server.

The database created for this project is named todo_database and contains a single collection named tasks. Each document in the collection represents one task in the to-do list.
This simple structure provides all the information needed to support the application's Create, Read, Update, and Delete (CRUD) operations while keeping the database easy to understand and maintain.

# Development Environment

The tools used in this project are VsCode and MongoDB

The languages used in this project are Python, HTML, and CSS.

# Useful Websites

- [RealPython Database Tutorials](https://realpython.com/tutorials/databases/)
- [Boot.Dev Demo Game](https://www.boot.dev/try/coding-game?utm_source=google&utm_medium=cpc&utm_campaign=23318594387&gad_source=1&gad_campaignid=23318594387&gbraid=0AAAAACKV4BBmMhzlYjuVh6cEs9g08DPEd&gclid=Cj0KCQjwjIPSBhCCARIsABGyK7vpcAO9Coa1i1epT9Oxi1TmU77YrdX6osAG7GqHaK_XmMkTWIh_SH8aAj3wEALw_wcB)

# Future Work

- I want to have more tabs of "To-Do" and "Completed" so the takss can be dragged around instead of just clicking.
- I want to add more tabs for people to add their names where users can have groups.
- I want to add more style to the web app where tasks are listed horizontal and you scroll left and right nor them.