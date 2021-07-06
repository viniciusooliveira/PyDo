import typing
from fastapi import APIRouter, Depends, status

from app.domain.business.list_business import ListBusiness, get_instance as businessInstance
from app.domain.models import List

router = APIRouter(
    prefix="/list",
    tags=["To-Do Lists"],
    responses={
        404: {"description": "Not found"}
    }
)


@router.get("/",
            name="List Todo Lists",
            description="Returns a list of all registered Todo Lists",
            response_model=typing.List[List])
async def list_all(business: ListBusiness = Depends(businessInstance)):
    result = await business.get_all()
    return result


@router.get("/{item_id}",
            name="List a single Todo List",
            description="Returns the selected Todo List",
            response_model=List)
async def get(item_id: int, business: ListBusiness = Depends(businessInstance)):
    result = await business.get(item_id)
    return result


@router.post("/",
             name="Create a new Todo List",
             description="Returns the registered Todo List",
             response_model=List)
async def post(model: List, business: ListBusiness = Depends(businessInstance)):
    model.id = None
    result = await business.save(model)
    return result


@router.put("/{item_id}",
            name="Updates an Todo List",
            description="Returns the registered Todo List",
            response_model=List)
async def put(item_id: int, model: List, business: ListBusiness = Depends(businessInstance)):
    model.id = item_id
    result = await business.save(model)
    return result


@router.delete("/{item_id}",
               name="Delete a Todo List",
               description="Delete a Todo List",
               status_code=status.HTTP_202_ACCEPTED)
async def put(item_id: int, business: ListBusiness = Depends(businessInstance)):
    await business.delete(item_id)
