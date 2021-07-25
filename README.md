# Crazliv-Games-Project

## Basic API performing CRUD operations
Here a django project 'student' is created and inside this project, a 'user' app is there.
'user' app consists of two model, i.e., BasicDetails and Education


### Getting Started
Using DRF, REST API is created here.

### Installation
Clone into your local system
```
git clone https://github.com/VishalTiwari-99/Crazliv-Games-Project.git
```
Install requirements
```
pip install -r requirements.txt
```
Migrate the databases
```
python manage.py makemigrations
python manage.py migrate
```
Finally run application on local system
```
python manage.py runserver
```

### Following are the endpoints of API
- To get list of all the education institution: http://127.0.0.1:8000/api/education-list/  (GET request only)
- To get list of all the students: http://127.0.0.1:8000/api/details-list/  (GET request only)
- For registration of new user: http://127.0.0.1:8000/dj-rest-auth/registration/
- For base root view/ API root: http://127.0.0.1:8000/api/
- For accessing student details: http://127.0.0.1:8000/api/details/  (GET, POST, Authentication Required)
- To modify the student records: http://127.0.0.1:8000/api/details/[id] (GET, POST, Authentication Required)
- For accessing educaition details: http://127.0.0.1:8000/api/education/  (GET, POST, Authentication Required)
- To modify the education records:  http://127.0.0.1:8000/api/education/[id]  (GET, POST, Authentication Required)
