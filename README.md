# Employee Management (Django, black & white)

    python -m venv venv
    source venv/bin/activate        # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

Open http://127.0.0.1:8000/ and add a department first, then employees.
Optional admin: `python manage.py createsuperuser` then visit /admin/.
