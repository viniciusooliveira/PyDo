from fastapi import APIRouter
from app.routes import todo_routes

router = APIRouter()

router.include_router(todo_routes.router)
