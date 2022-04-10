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
<ol>
<li> Run on the terminal: "pip install -r requirements.txt"</li>
<li> Create a root DB user and DB Named "BookStore" or change the settings for that in the DataBase section in settings.py </li>
<li> Run "python manage.py migrate"</li>
<li> Run "python manage.py runserver"</li>
<li>Now you should see this output on your terminal: "Performing system checks...

System check identified no issues (0 silenced).
April 10, 2022 - 12:13:25
Django version 2.0.2, using settings 'BookStore.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
"<br /><br />Now Copy that link :"http://127.0.0.1:8000/" Paste it in your Browser</li>
<li>For Admin user : Run "python manage.py createsuperuser" and Follow the instructions </li>
</ol>

<h2>Screenshots</h2>

![image](https://user-images.githubusercontent.com/22475831/162617770-d94f7358-05a9-42ba-8323-b31840fdb2e4.png)
![image](https://user-images.githubusercontent.com/22475831/162617855-58d7ed35-12c9-4915-a8e4-48a8d610b61a.png)
![image](https://user-images.githubusercontent.com/22475831/162617880-86931367-5fdb-40b1-84ac-7a10fc626f1d.png)
![image](https://user-images.githubusercontent.com/22475831/162617940-7c9fbc1a-3ce2-43cb-ba50-9bf9df9183d9.png)
![image](https://user-images.githubusercontent.com/22475831/162617971-cc61cfa3-2fb2-44d8-842c-720fa010a7b3.png)
![image](https://user-images.githubusercontent.com/22475831/162618025-e6f3523a-7b5f-4f88-9a7c-fdf35c8e38b7.png)
![image](https://user-images.githubusercontent.com/22475831/162618135-7b6311c9-b708-4c21-a542-2c5299dec982.png)

