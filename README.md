## Requirements

- Please install the following:
    - pyhon 3.8
    - `pip install django`
    - `pip install djangorestframework`
- This app uses the built-in SQLite3 database for development. 

# Commands

- To start the server: `manage.py runserver 8000`
    - Then, you can visit the ` http://127.0.0.1:8000/` for admin ui. 
    - You can log in with `admin/admin` for the test database.
- To run unit tests: `manage.py test`

# Notes
- I have created a basic `django-rest` application, prepared to handle the Glucose Levels as specified.
- The app is configured to serve a (smaller, than specified) data object. All basic CRUD actions should work, as I just utilized the built-in Serializers, Models, and Views.
- The app provides a basic security (more of a Proof of Concept in this state) where a user can require an Auth Token to access the REST endpoints.
- The app has a bult-in viewer, as Django-rest provides it.
- There are already existing data in the DB to test the application.
- I wrote only two tests, as instead of full coverage, I focused my time on other tasks, but this is not something I would normally do as testing is always a priority.
- I have run out of time while was working on the filtering and ordering of the data.
- I think I have provided a solid base for the tasks and bonus objectives, but I couldn't finish them as I ran out of time.
- I spend roughly 1.5 hours on the backend side (I have less experience with backend frameworks, my main focus in Frontend usually)
  - I spend one night yesterday to learn how Django-REST works, as I needed to learn a framework which works like NodeJS + Express for the Python stack.


