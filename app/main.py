from fastapi import Body, FastAPI
from . import models
from .database import engine, get_db
from .routers import post, user, auth, vote
from .config import Settings





# creates the database with tables from the models given in the models file
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message" : "Welcome to my API!"}



