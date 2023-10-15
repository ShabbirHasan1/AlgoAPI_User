from fastapi import APIRouter
from services import *

hedgessrouter = APIRouter()


@hedgessrouter.get("/")
async def get_hedges_all():
    hedge = await AlgoHedges()
    hedge_data = await hedge.get_hedges_all()
    return hedge_data

@hedgessrouter.get("/{strategy}")
async def get_hedge_data(strategy: str):
    hedge = await AlgoHedges()
    hedge_data = await hedge.get_hedges_data(strategy)
    return hedge_data