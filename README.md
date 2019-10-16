# Instagram App
This is an instagram clone app developed with django with the aim of getting a better understanding of django framework.

# Description
This is a simple clone of instagram. The app allows user to create accounts and register to them with their credentials. The site also supports uploading of images. Logged in users are able to view photos uploaded by other users on the home page of site.

# Specifications
Find the specs here

# Set Up and Installations
### Prerequisites
Ubuntu Software
Python3.6
Postgres
python virtualenv

Clone the project repo by running <git clone https://github.com/Gideon-Muriithi/instagram_clone>.

Create virtual environment by running <python3.6 -m venv pip virtual> while in the dirctory of the cloned project. Activate the virtual environment by running <source virtual/bin/activate>.

Install all the dependencies necessarry for running the application using this command: pip install-r requirements.txt

Create a database: psql then create the databse using this command: CREATE DATABASE instagram

Run migrations using these respective commmands: python3.6 manage.py makemigrations images then: python3.6 manage.py migrate

Run the app using this command: python3.6 manage.py runserver on the terminal.You can then open the app on your browser

Create .env file and paste paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DBNAME = 'instagram'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'

Run initial Migration
python3.6 manage.py makemigrations gram
python3.6 manage.py migrate
Run the app
python3.6 manage.py runserver
Open terminal on localhost:8000

# Known bugs
Like and follow functionalities not working as per the expections

# Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- JavaScript
- Heroku
- Postgresql

# Support and contact details
For any comments, reviews or advice contact me on gideonapptests@gmail.com.

# License
Copyright (c) Gideon Muriithi