from fastapi import APIRouter
from app.routes import todo_routes, list_routes

router = APIRouter()

router.include_router(todo_routes.router)
router.include_router(list_routes.router)

