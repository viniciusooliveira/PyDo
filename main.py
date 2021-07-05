import uvicorn
from os import environ
from fastapi import FastAPI
import app.config
from app.routes import routes
from app.infra.db.database import create_tables

create_tables()

app = FastAPI(
    title=environ["PYDO_APP_NAME"],
    version="0.0.1",
    description="A Todo List API made with Python, FastAPI, SQLAlchemy and a lot of work."
)

app.include_router(routes.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
