# LittleLemon Capstone

Django project for the Little Lemon restaurant, with a REST API, token authentication, and Djoser.

## How to run it

1. Create and activate a virtual environment.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure the database.

The project is currently configured to use MySQL in `littlelemon/settings.py`. Make sure the `LittleLemon` database exists and update the username, password, host, and port to match your environment.

4. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser if you need access to the admin panel:

```bash
python manage.py createsuperuser
```

6. Start the server:

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

## Created endpoints

According to the Backend Developer Capstone course this are the required enpoints

### Frontend

- `GET /` - Main page rendered from `templates/index.html`

### Authentication

- `POST /auth/users/` - Register a new user
Try register the next user in body section
```bash
{
    "username":"Alvoid",
    "password":"Kjkszpj101"
}
```
- `POST /auth/token/login/` - Obtain an authentication token
- `POST /auth/token/logout/` - Destroy the Token, ensure use the token in auth header
- `GET /auth/` - User and authentication endpoints provided by Djoser

### Restaurant API

- `GET /api/restaurant/message/` - Protected message, requires authentication
- `GET /api/restaurant/menu/items` - List menu items
- `POST /api/restaurant/menu/items` - Create a menu item
- `GET /api/restaurant/menu/<int:pk>` - Retrieve a menu item by id
- `PUT /api/restaurant/menu/<int:pk>` - Update a menu item
- `PATCH /api/restaurant/menu/<int:pk>` - Partially update a menu item
- `DELETE /api/restaurant/menu/<int:pk>` - Delete a menu item

### Reservations

The `BookingViewSet` is exposed with `DefaultRouter` under `api/restaurant/booking/`:

- `GET /api/restaurant/booking/tables/` - List bookings
- `POST /api/restaurant/booking/tables/` - Create a booking
- `GET /api/restaurant/booking/tables/<int:pk>/` - Retrieve a booking by id
- `PUT /api/restaurant/booking/tables/<int:pk>/` - Update a booking
- `PATCH /api/restaurant/booking/tables/<int:pk>/` - Partially update a booking
- `DELETE /api/restaurant/booking/tables/<int:pk>/` - Delete a booking

### Test

I implemented a test for creating items in the menu, you can checked in `restaurant/tests.py`

Run `python manage.py test` to try the test

## Notes

- The `message/` endpoint and the `menu/items` view require an authenticated user.
- To use protected endpoints, you can authenticate with a token or with Django REST Framework session authentication.
