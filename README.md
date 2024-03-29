# BookLand
BookLand is a django app for a LMS (Library Management System ) :<br /><br />
Where you can :

<h3>As an "Admin": </h3> 
<ul><li>Add , Update , Delete : Users, Groups , Authors , Books , Categories  </li>
</ul>
<h3>As a "User":</h3>
<ul><li>Sign-Up , Sign-In<br /></li>
<li>Change Password </li>
<li>Update your profile</li>
<li>List all available books </li>
<li>Add , List , Delete : Books to your wish list </li>
<li>Add , List , Delete : Books to your Reading list </li>
<li>Follow your favourite Authors and View books written by them </li> 
<li>Follow your favourite book categories and view books under them </li>
<li>Search by book or by author name </li>
<li>Rate a book </li>
<li>View top rated books</li>
<li>View top Followed Authors</li>
<li>View Author Bio</li>
<li>View Category Info</li></ul>

<h2>Datadog: </h2>
This app will send metrics to datadog.com APM by default just install ddtrace using "pip install ddtrace"
For More Info: https://www.datadoghq.com/blog/monitoring-django-performance/

<h2>Running The App</h2>

- Run on the terminal: 
```python
 pip install -r requirements.txt
``` 
- Create a root DB user and DB Named "BookStore" or change the settings for that in the DataBase section in ```settings.py ```
- Create Django ```Secret``` and update ```settings.py```
- Run 
```python
python manage.py migrate 
```
- Run
```python 
python manage.py runserver
```
- Now you should see this output on your terminal: 
``` 
Performing system checks...

System check identified no issues (0 silenced).
Django version 2.0.2, using settings 'BookStore.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C. 
```
- Now Copy that link :
```sh
http://127.0.0.1:8000/ 
```
- Paste it in your Browser
- To Create The Admin user : Run 
```python
python manage.py createsuperuser
```
- and Follow the instructions 


<h2>Steps to Docorize a Django App: </h2>

Steps to set up Django on MySQL in Docker containers (using docker compose)

### Prerequisites:
- Installed Docker
- Installed docker-compose
- Your Django application code

### Desired Specs:
- Python 3.8.10 
- MySQL 5.7 
- docker compose version 3

### Steps:
- Dockerfile:
  
![image](https://user-images.githubusercontent.com/22475831/163283452-010ccb25-b93d-4b43-afe1-b3eb72ac998d.png)

- docker-compose.yml

![image](https://user-images.githubusercontent.com/22475831/163283760-a9abe602-b41a-40c7-aeb9-31d40b6e90c5.png)

### requirements.txt
  
- Run 
```python
pip install pipreqs
```
- in your project directory to extract ``` requirements.txt ``` run:
```python
pipreqs "/path/to/project" 
```     
- settings.py

  ![image](https://user-images.githubusercontent.com/22475831/163284435-fe9cf55d-39d5-49ee-b942-d16e0388f8a1.png)
  
- Run 
```sh
docker-compose build
```
- Run 
```sh
docker-compose up
```
- Open browser to ``` localhost:8000 ```
  
## Screenshots

![image](https://user-images.githubusercontent.com/22475831/162617770-d94f7358-05a9-42ba-8323-b31840fdb2e4.png)
![image](https://user-images.githubusercontent.com/22475831/162617855-58d7ed35-12c9-4915-a8e4-48a8d610b61a.png)
![image](https://user-images.githubusercontent.com/22475831/162617880-86931367-5fdb-40b1-84ac-7a10fc626f1d.png)
![image](https://user-images.githubusercontent.com/22475831/162617940-7c9fbc1a-3ce2-43cb-ba50-9bf9df9183d9.png)
![image](https://user-images.githubusercontent.com/22475831/162617971-cc61cfa3-2fb2-44d8-842c-720fa010a7b3.png)
![image](https://user-images.githubusercontent.com/22475831/162618025-e6f3523a-7b5f-4f88-9a7c-fdf35c8e38b7.png)
![image](https://user-images.githubusercontent.com/22475831/162618135-7b6311c9-b708-4c21-a542-2c5299dec982.png)
