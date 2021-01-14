# Tripster


I have build a Hotel site which has:

    Rooms
    Book A Room
    Search Over Rooms
    About
    Contact

STEPS TO RUN THE PROJECT-

clone the project:

    https://github.com/97shivank/Hotel-Site-with-Django.git

create and start a a virtual environment:

    virtualenv env --no-site-packages
    source env/bin/activate
    
Install the project dependencies:    
    
    pip install -r requirements.txt
    
create a file named "secrets.sh":
touch secrets.sh (linux):
obtain a secret from MiniWebTool key and add to secrets.sh:

    export SECRET_KEY='<secret_key>'
    
create a postgres db and add the credentials to settings.py:

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
    }
    
then run:

    python manage.py migrate
    
create admin account:

    python manage.py createsuperuser
    
then:

    python manage.py makemigrations django-hotel
    
to makemigrations for the app:
then again run:

    python manage.py migrate
    
to start the development server:

    python manage.py runserver
    
and open localhost:8000 on your browser to view the app:    


HOME 

![alt text](https://user-images.githubusercontent.com/31972312/91582175-128a9300-e96d-11ea-8f82-586c8e2c24b7.png)

PROPERTIES
![alt text](https://user-images.githubusercontent.com/31972312/91582201-19b1a100-e96d-11ea-8932-3c43cf1b3ffe.png)

AGENTS
![alt text](https://user-images.githubusercontent.com/31972312/91582218-20401880-e96d-11ea-99b1-7280ea420572.png)

ABOUT
![alt text](https://user-images.githubusercontent.com/31972312/91581906-baec2780-e96c-11ea-81e3-4de59522ffcf.png)

CONTACT US 
![alt text](https://user-images.githubusercontent.com/31972312/91582243-27672680-e96d-11ea-95cd-b362163afdfe.png)
