from typing import List
from fastapi import APIRouter, Depends, status

from app.domain.business.todo_business import TodoBusiness, get_instance as businessInstance
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
async def list_all(business: TodoBusiness = Depends(businessInstance)):
    result = await business.get_all()
    return result


@router.get("/{item_id}",
            name="List a single Todo Item",
            description="Returns the selected Todo Item",
            response_model=Todo)
async def get(item_id: int, business: TodoBusiness = Depends(businessInstance)):
    result = await business.get(item_id)
    return result


@router.post("/",
             name="Create a new Todo Item",
             description="Returns the registered Todo Item",
             response_model=Todo)
async def post(model: Todo, business: TodoBusiness = Depends(businessInstance)):
    model.id = None
    result = await business.save(model)
    return result


@router.put("/{item_id}",
            name="Updates an Todo Item",
            description="Returns the registered Todo Item",
            response_model=Todo)
async def put(item_id: int, model: Todo, business: TodoBusiness = Depends(businessInstance)):
    model.id = item_id
    result = await business.save(model)
    return result


@router.delete("/{item_id}",
               name="Delete a Todo Item",
               description="Delete a Todo Item",
               status_code=status.HTTP_202_ACCEPTED)
async def put(item_id: int, business: TodoBusiness = Depends(businessInstance)):
    await business.delete(item_id)
