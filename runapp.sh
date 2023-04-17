source venv/bin/activate
python3 manage.py makemigrations book_api
python3 manage.py migrate book_api
python3 manage.py migrate 
python3 manage.py runserver
