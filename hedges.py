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
        hedge = await AlgoHedge(settings.Broker,settings.UserId)
        hedges = await hedge.get_hedges_all()
        return ResponseSchema(status='success', code='hedge', description='ok', data=hedges)
    except Exception as e:
        return exception_handler(e)

@hedgessrouter.get("/strategy/{strategy}",response_model=ResponseSchema)
async def get_hedges_startegy_data(strategy: str):
    try:
        hedge = await AlgoHedge(settings.Broker,settings.UserId)
        hedge_data = await hedge.get_hedges_strategy(strategy)
        return ResponseSchema(status='success', code='hedge', description='ok', data=[hedge_data])
    except Exception as e:
        return exception_handler(e)

@hedgessrouter.get("/strategy/{strategy}/{status}",response_model=ResponseSchema)
async def get_hedges_startegy_status_data(strategy: str,status: str):
    try:
        hedge = await AlgoHedge(settings.Broker,settings.UserId)
        hedge_data = await hedge.get_hedges_strategy_status(strategy,status)
        return ResponseSchema(status='success', code='hedge', description='ok', data=[hedge_data])
    except Exception as e:
        return exception_handler(e)

@hedgessrouter.get("/{hedgeid}",response_model=ResponseSchema)
async def get_hedge_data(hedgeid: int):
    try:
        hedge = await AlgoHedge(settings.Broker,settings.UserId)
        hedge_data = await hedge.get_hedge(hedgeid)
        return ResponseSchema(status='success', code='spread', description='ok', data=[hedge_data])
    except Exception as e:
        return exception_handler(e)

@hedgessrouter.post("/createhedge",response_model=ResponseSchema)
async def create_hedge_data(hedge: HedgesSchemaIn):
    try:
        algoHedges = await AlgoHedge(settings.Broker,settings.UserId)
        hedge_data = await algoHedges.create_hedge(hedge)
        return ResponseSchema(status='success', code='hedge', description='ok', data=[hedge_data])
    except Exception as e:
        return exception_handler(e)

@hedgessrouter.put("/updatehedge",response_model=ResponseSchema)
async def update_hedge_data(spread: HedgesSchemaOut):
    try:
        algoHedges = await AlgoHedge(settings.Broker,settings.UserId)
        spread_data = await algoHedges.update(spread)
        return ResponseSchema(status='success', code='hedge', description='ok', data=[spread_data])
    except Exception as e:
        return exception_handler(e)


@hedgessrouter.delete("/deletehedge",response_model=ResponseSchema)
async def delete_hedge_data(hedgeid: int):
    try:
        algoHedges = await AlgoHedge(settings.Broker,settings.UserId)
        spread_data = await algoHedges.delete(hedgeid)
        return ResponseSchema(status='success', code='hedge', description='ok', data=[spread_data])
    except Exception as e:
        return exception_handler(e)