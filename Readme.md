This is the simple django-prototype app I created to make it faster to start new django projects.

It has basic email/password authorization, docker files and postgresql db.

1. `git clone django-prototype`
2. `docker compose up --build`
3. `docker compose exec web python app/manage.py migrate`
4. `docker compose exec web python app/manage.py createsuperuser`
5. go to `http://localhost:8000/auth/login/`

Currently available views:

1. _/auth/login/_
2. _/auth/logout/_
3. _/auth/signup/_
4. _/auth/index/_
