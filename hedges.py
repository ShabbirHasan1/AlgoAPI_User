from fastapi import APIRouter
from services import *

hedgessrouter = APIRouter()

@hedgessrouter.get("/",response_model=ResponseSchema)
async def get_hedges():
    hedges = {"message": "Hedges!"}
    return ResponseSchema(status='success', code='hedge', description='ok', data=[hedges])


@hedgessrouter.get("/all",response_model=ResponseSchema)
async def get_hedges_all():
    try:
        hedge = await AlgoHedges()
        hedges = await hedge.get_hedges_all()
        return ResponseSchema(status='success', code='hedge', description='ok', data=hedges)
    except Exception as e:
        return exception_handler(e)

@hedgessrouter.get("/{strategy}",response_model=ResponseSchema)
async def get_hedge_data(strategy: str):
    try:
        hedge = await AlgoHedges()
        hedge_data = await hedge.get_hedges_data(strategy)
        return ResponseSchema(status='success', code='hedge', description='ok', data=[hedge_data])
    except Exception as e:
        return exception_handler(e)