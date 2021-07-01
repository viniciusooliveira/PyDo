import uvicorn
from fastapi import FastAPI
from app.routes import routes
from dotenv import load_dotenv
from os import environ
load_dotenv()
#config = dotenv.dotenv_values(".env")

print(environ["APP_NAME"])

app = FastAPI(
    title=environ["APP_NAME"],
    version="0.0.1-pre.alpha",
    description="A Todo List API made with Python, FastAPI, SQLAlchemy and a lot of work."
)

app.include_router(routes.router)


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
