# FastAPI CRUD with JWT Authentication and PostgreSQL

A CRUD application built with FastAPI. Users register and log in to receive a JWT access token, which is required to create, read, update and delete items stored in PostgreSQL.

## Setup

1. Create and activate a virtual environment:
```
   python -m venv venv
   venv\Scripts\activate
```
2. Install dependencies:
```
   pip install -r requirements.txt
```
3. Create a PostgreSQL database named `crud_db`.
4. Create a `.env` file with these values:
```
   DATABASE_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/crud_db
   SECRET_KEY=change_this_to_a_long_random_string
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
```
5. Run the server:
```
   uvicorn app.main:app --reload
```
6. Open Swagger UI at http://127.0.0.1:8000/docs

## Endpoints

- `POST /users/register` - create a user
- `POST /users/login` - returns username and access token
- `POST /items/` - create an item
- `GET /items/` - list your items
- `GET /items/{item_id}` - get one item
- `PUT /items/{item_id}` - update an item
- `DELETE /items/{item_id}` - delete an item