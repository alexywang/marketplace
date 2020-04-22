Students
-------------------------------
Alex Wang 260684151
Aidan Weber-Concannon 260708481
Olivia Woodhouse 260734701


Instructions
-------------------------------
1. Additonal packages required: six, simplejson, pillow,  
2. Create super user using: python manage.py createsuperuser
4. Delete all files in migration folders except _init_.py to start with a fresh database
5. python manage.py sqlclear
6. python manage.py makemigrations 
7. python manage.py migrate 
8. Go to localhost:8000/admin and use super user to populate the Category table with some category names (e.g. bed, table, chair)
9. python manage.py runserver 

Have fun 🙂