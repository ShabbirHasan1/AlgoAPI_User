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
        hedge = await AlgoHedge()
        hedges = await hedge.get_hedges_all()
        return ResponseSchema(status='success', code='hedge', description='ok', data=hedges)
    except Exception as e:
        return exception_handler(e)

@hedgessrouter.get("/{strategy}",response_model=ResponseSchema)
async def get_hedge_data(strategy: str):
    try:
        hedge = await AlgoHedge()
        hedge_data = await hedge.get_hedges_data(strategy)
        return ResponseSchema(status='success', code='hedge', description='ok', data=[hedge_data])
    except Exception as e:
        return exception_handler(e)


@hedgessrouter.post("/createhedge",response_model=ResponseSchema)
async def create_hedge_data(hedge: HedgesSchemaIn):
    try:
        algoHedges = await AlgoHedge()
        hedge_data = await algoHedges.create_hedge(hedge)
        return ResponseSchema(status='success', code='hedge', description='ok', data=[hedge_data])
    except Exception as e:
        return exception_handler(e)