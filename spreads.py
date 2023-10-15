from fastapi import APIRouter
from services import *

spreadsrouter = APIRouter()


@spreadsrouter.get("/")
async def get_spreads_all():
    spread = await AlgoSpreads()
    spread_data = await spread.get_spreads_all()
    return spread_data

@spreadsrouter.get("/{strategy}")
async def get_spreads_data(strategy: str):
    spread = await AlgoSpreads()
    spread_data = await spread.get_spreads_data(strategy)
    return spread_data