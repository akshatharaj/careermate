# Careermate

CareerMate is a Django application that provides users a platform to share Interview
experiences and Company review with other users.


## Installation

### Fork the careermate repository  and check it out

    $ cd ~/Code
    $ git clone git@github.com:username/careermate.git

### Make a new virtual environment

    $ virtualenv --no-site-packages --distribute ~/Code/env
    $ cd ~/Code/env
    $ . bin/activate
    $ pip install -U distribute

### Install careermate and all its dependencies

    $ cd ~/Code/careermate
    $ ./build.bash develop
    $ pip install requirements.txt

### Copy the main Django files (or create a new django project)

    $ cd ~/Code
    $ mkdir project
    $ cp ~/Code/careermate/pkg/project/__init__.py ~/Code/project/; cp ~/Code/careermate/pkg/project/manage.py ~/Code/project/

### Then run

    $ python manage.py syncdb
    $ python manage.py migrate
    $ python manage.py collectstatic

## Documentation

### User accounts

    There are two kinds of user accounts. Normal users register on the website and gain access
    to the features (posting new reviews, responding to reviews) on the site. 

    Admin users are set up on the server who can moderate posts, post responses and make decisions
    on reports user submit on the site. 
    For testing use the admin account:
    username: admin
    password: admin


### Functionality
    Users can create new posts after logging in. Ohter users respond to posts and have the option of
    subscribing to future responses on the post.

    Users can report posts they think should be taken offline giving a reason.

    Admin users can review all page reports. They may choose to accept the page report (available as
    an admin action on the post report) which results in the post taken offline and all other reports
    on the same post are deleted too. Admin users may delete the reports they think are not acceptable.


