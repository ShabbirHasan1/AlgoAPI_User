from fastapi import APIRouter
from services import *

spreadsrouter = APIRouter()


@spreadsrouter.get("/", response_model=ResponseSchema)
async def get_spreads():
    spreads = {"message": "Spreads!"}
    return ResponseSchema(status='success', code='spread', description='ok', data=[spreads])


@spreadsrouter.get("/all", response_model=ResponseSchema)
async def get_spreads_all():
    try:
        spread = await AlgoSpread(settings.Broker, settings.UserId)
        spreads = await spread.get_spreads_all()
        return ResponseSchema(status='success', code='spread', description='ok', data=spreads)
    except Exception as e:
        return exception_handler(e)


@spreadsrouter.get("/strategy/{strategy}", response_model=ResponseSchema)
async def get_spreads_strategy_data(strategy: str):
    try:
        spread = await AlgoSpread(settings.Broker, settings.UserId)
        spreads = await spread.get_spreads_strategy(strategy)
        return ResponseSchema(status='success', code='spread', description='ok', data=spreads)
    except Exception as e:
        return exception_handler(e)


@spreadsrouter.get("/strategy/{strategy}/{status}", response_model=ResponseSchema)
async def get_spreads_strategy_status_data(strategy: str, status: str):
    try:
        spread = await AlgoSpread(settings.Broker, settings.UserId)
        spreads = await spread.get_spreads_strategy_status(strategy, status)
        return ResponseSchema(status='success', code='spread', description='ok', data=spreads)
    except Exception as e:
        return exception_handler(e)


@spreadsrouter.get("/{spreadid}", response_model=ResponseSchema)
async def get_spread_data(spreadid: int):
    try:
        spread = await AlgoSpread(settings.Broker, settings.UserId)
        spread_data = await spread.get_spread(spreadid)
        return ResponseSchema(status='success', code='spread', description='ok', data=[spread_data])
    except Exception as e:
        return exception_handler(e)


@spreadsrouter.post("/createspread", response_model=ResponseSchema)
async def create_spread_data(spread: SpreadsSchemaIn):
    try:
        algoSpreads = await AlgoSpread(settings.Broker, settings.UserId)
        spread_data = await algoSpreads.create(spread)
        return ResponseSchema(status='success', code='spread', description='ok', data=[spread_data])
    except Exception as e:
        return exception_handler(e)


@spreadsrouter.put("/updatespread", response_model=ResponseSchema)
async def update_spread_data(spread: SpreadsSchemaOut):
    try:
        algoSpreads = await AlgoSpread(settings.Broker, settings.UserId)
        spread_data = await algoSpreads.update(spread)
        return ResponseSchema(status='success', code='spread', description='ok', data=[spread_data])
    except Exception as e:
        return exception_handler(e)


@spreadsrouter.delete("/deletespread", response_model=ResponseSchema)
async def delete_spread_data(spreadid: int):
    try:
        algoSpreads = await AlgoSpread(settings.Broker, settings.UserId)
        spread_data = await algoSpreads.delete(spreadid)
        return ResponseSchema(status='success', code='spread', description='ok', data=[spread_data])
    except Exception as e:
        return exception_handler(e)
