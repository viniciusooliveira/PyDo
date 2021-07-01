from typing import List
from fastapi import APIRouter
from app.domain.models import Todo

router = APIRouter(
    prefix="/todo",
    tags=["To-Do Items"],
    responses={
        404: {"description": "Not found"}
    }
)


@router.get("/",
            name="List Todo Items",
            description="Returns a list of all registered Todo Items",
            response_model=List[Todo])
async def list_all():
    return [
        {
            "id": 42,
            "name": "Convert all Post-Its to Todo",
            "done": False
        },
        {
            "id": 43,
            "name": "Learn Python",
            "done": False
        }
    ]


@router.get("/{item_id}",
            name="List a single Todo Item",
            description="Returns the selected Todo Item",
            response_model=Todo)
async def get(item_id: int):
    return {
        "id": 42,
        "name": "Convert all Post-Its to Todo",
        "done": False
    }


@router.post("/",
             name="Create a new Todo Item",
             description="Returns the registered Todo Item",
             response_model=Todo)
async def post(model: Todo):
    return model


@router.put("/{item_id}",
            name="Updates an Todo Item",
            description="Returns the registered Todo Item",
            response_model=Todo)
async def put(item_id: int, model: Todo):
    model.id = item_id
    return model
