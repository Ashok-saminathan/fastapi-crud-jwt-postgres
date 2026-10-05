from fastapi import FastAPI

from .database import engine, Base
from .routers import users, items

# Create the tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD with JWT Auth", version="1.0")

app.include_router(users.router)
app.include_router(items.router)


@app.get("/")
def root():
    return {"message": "FastAPI CRUD API is running"}