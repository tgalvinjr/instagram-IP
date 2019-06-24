# Instagram Clone

## Description
####  This is an instagram clone  for the popular photo app,Instagram.

## Features (The user can:)
* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.

## Setup/Installation Requirements
### Prerequisites
* python3.6
* pip
* Virtual environment(virtualenv)
* Text editor
* Django
* Postgresql

### Cloning/Installing and running
* Clone the application using git clone(this copies the app onto your device). In terminal:

          $ git clone https://github.com/tgalvinjr/instagram-IP.git
          $ cd gallery

* Creating the virtual environment

          $ python3.6 -m venv --without-pip virtual
          $ source virtual/bin/env
          $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

          $ python3.6 -m pip install Django==1.11
          $ python3.6 -m pip3 install django-Bootstrap3
          $ python3.6 -m pip install Pillow
          $ python3.6 -m pip install -r requirements.txt
          $ psql
          $ CREATE DATABASE gallery;
          $ python3 manage.py migrate

* Run the application:

          $ python3 manage.py runserver
### Testing the Application
* To run the tests for the class files:

          $ python3.6 manage.py test

## Technologies Used
* Python 3.6
* Django 1.11
* Bootstrap


## Github Pages
    The UI templates can be tested on [Heroku](https://alvogram.herokuapp.com/home)

## Known Bugs
None at the moment

### Author(s) information
Alvin Michoma
[Github](https://github.com/tgalvinjr)

## License and Copyright information
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/tgalvinjr/instagram-IP/blob/master/LICENSE) file for details

## Acknowledgments
- Hat tip to anyone who unblocked me in class
- Special thanks to Moringa TMs Peter and Newton for the guidance