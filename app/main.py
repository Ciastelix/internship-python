from fastapi import FastAPI
from app.containers import Container
from . import endpoints

container = Container()

db = container.db()
db.create_database()
app = FastAPI()
app.container = container
app.include_router(endpoints.router)