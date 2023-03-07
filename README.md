# aaCoffeeChallenge

## Backend
1. Navigate to root of directory, and run following cmd: `source recapp/bin/activate`
2. Navigate to recapp/coffee_app, run following cmd: `python manage.py runserver`
3. Utilize api urls specified in recapp/coffee_app/aacoffee/views.py and recapp/coffee_app/aacoffee/urls.py

## Backend API Routes
<!-- -->
### Ping
<!-- -->
- `Coffee Ping:` `GET` http://localhost:8000/api/coffee/ping
- `Post Ping:` `GET` http://localhost:8000/api/post/ping
<!-- -->
### Coffee
<!-- -->
- `Coffee Index:` `GET` http://localhost:8000/api/coffee
- `Coffee Show:` `GET` http://localhost:8000/api/coffee/<int:coffee_id>/
- `Coffee Create:` `POST` http://localhost:8000/api/coffee
- `Coffee Delete:` `Delete` http://localhost:8000/api/coffee/<int:coffee_id>/
<!-- -->
### Post
<!-- -->
- `Post Index:` `GET` http://localhost:8000/api/post
- `Post Show:` `GET` http://localhost:8000/api/post/<int:post_id>/
- `Post Create:` `POST` http://localhost:8000/api/post
- `Post Delete:` `Delete` http://localhost:8000/api/post/<int:post_id>/

