from fastapi import APIRouter
from services import *

spreadsrouter = APIRouter()

@spreadsrouter.get("/",response_model=ResponseSchema)
async def get_spreads():
    spreads = {"message": "Spreads!"}
    return ResponseSchema(status='success', code='spread', description='ok', data=[spreads])


@spreadsrouter.get("/all",response_model=ResponseSchema)
async def get_spreads_all():
    try:
        spread = await AlgoSpreads()
        spreads = await spread.get_spreads_all()
        return ResponseSchema(status='success', code='spread', description='ok', data=spreads)
    except Exception as e:
        return exception_handler(e)

@spreadsrouter.get("/{strategy}",response_model=ResponseSchema)
async def get_spreads_data(strategy: str):
    try:
        spread = await AlgoSpreads()
        spreads= await spread.get_spreads_data(strategy)
        return ResponseSchema(status='success', code='spread', description='ok', data=spreads)
    except Exception as e:
        return exception_handler(e)
