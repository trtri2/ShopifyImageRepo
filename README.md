
# The Doggie Records - A Shopify Fall 2021 Intern Challenge Submission

[PROJECT VIDEO DEMO](https://drive.google.com/file/d/1w0mDLJicNSZUOYoIPtBTKmVbVB2bEhrL/view?usp=sharing)

## PROJECT SCOPE
### Purpose
This is my challenge submission for Shopify's Fall 2021 Developer Intern position. The back-end challenge involves creating an image repository and allowed for some open-ended interpretations in the implementation. The project is a flask web app with a Web API to add, remove, and view images using a PostgreSQL database. SQLAlchemy was used to handle the object relational mapping between the front-end and back-end. You can check out a quick video demo of the features and use cases [here.](https://drive.google.com/file/d/1w0mDLJicNSZUOYoIPtBTKmVbVB2bEhrL/view?usp=sharing)

### Design Considerations
* Given the task is a back-end focused challenge, I used a micro web framework such as Flask to get the project up and started quickly and easily, so I can focus on back-end implementations and Web API structure. I didn't spend too much time on styling and the user experience portion of this challenge. [See [here](https://github.com/trtri2/TheShoppies2021) for my front-end submission here where I did ;) ]
* PostgreSQL was used as the DB of choice as its a popular open-source relational DB management system at the time and wanted to take the opportunity to get more hands on experience with it. 
* SQLAlchemy was a good solution to use as the object relational mapping and abstract the database specific details away the solution, which lets the project be easily migrated to a different database service such as sqlite. 

## ENVIRONMENT
- Python 3 
- Flask (WEB API)
- PostgreSQL (Database) 
- SQLAlchemy (ORM)

## SETUP
Download or clone the repo and set up the python and postgreSQL dependencies below. Afterwards, you can run 

	python3 app.py

which will launch the flask server and be available at `localhost:5000`

### Python3

1. It's a good practice to work with a virtual environment to manage your project dependencies and libraries in Python. Create and run the virtual env by running:

		python3 -m venv virtualenv
		
		source virtualenv/bin/activate
2. Install the necessary requirements and dependencies using pip.
		
		pip install -r requirements.txt
		
### Import PostgreSQL Database

1. [Download PostgreSQL](https://www.postgresql.org/download/)

The connection details are configured in app.py as follows:

![DB Connection Config line 11 in app.py](https://i.ibb.co/x7vFZwP/Screen-Shot-2021-05-05-at-12-33-50-AM.png)

2. Start the PostgreSQL service (i.e. for Mac Homebrew: `brew services start postgresql`)
3. Create a template table to import the database 'repo.db'

	   $ createdb -T template0 repodb
4. Import database dump

		$ psql repodb < repo.db

5. (Optional) In the current connection URI config above, we can see the default user is 'postgres' and 'password'. You can create the user role as follows:

		$ psql repodb
		
		repodb=# CREATE ROLE postgres WITH LOGIN SUPERUSER;

	Otherwise, you can change the connection URI to use your own {user.name} and {user.password} in your local postgresql server.

## TESTING HARNESS

In the /test directory run the following command to run the tests using the pytest library:

	pytest run_tests.py

