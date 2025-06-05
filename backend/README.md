Manual for amlukito

Run Backend Server
1. Open 2 terminals 
[First Terminal]
1. `cd backend/`
2. `source backendvenv/bin/activate` #Activate virtual environment named backendvenv
3. `python manage.py runserver` #Run Django development server
[Second Terminal]
1. `cd backend/`
2. `source backendvenv/bin/activate` #Activate virtual environment named backendvenv

Database
1. Create model(database structure) in polls/models.py
2. Any changes to models.py should be saved by running:
    `python manage.py makemigrations`
    `python manage.py migrate`
3. Create data to populate database in a separate file (e.g. polls/populate_db.py)
4. Run populate_db.py file: `python heavenlyvitamin/populate_db/populate_db.py`
5. View database of development server by going to:
    `http://127.0.0.1:8000/admin/heavenlyvitamin`
    Credentials of superadmin: 
    username: amlukito
    password: angiem11
6. Initialize new table by registering model to `heavenlyvitamin/admin.py`

API
1. Create a view in `backend/heavenlyvitamin/views.py`. Views are function that enables an API to receive request and responds with a web response. When creating a view, make sure to cross-check with the `models.py` and `admin.py` on how to access the data.
2. The request data will be the key to accesing the view. 
3. Add specific paths (urls) into `heavenlyvitamin/urls.py` to indicate web response to the API request.


