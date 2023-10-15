from fastapi import APIRouter
from services import *

plfundsrisksrouter = APIRouter()


@plfundsrisksrouter.get("/")
async def get_plfundsrisks_all():
    plfundsrisk = await AlgoPLFundsRisk()
    plfundsrisk_data = await plfundsrisk.get_plfundsrisks_all()
    return plfundsrisk_data


@plfundsrisksrouter.get("/{date}")
async def get_plfundsrisks_data(date: str):
    plfundsrisk = await AlgoPLFundsRisk()
    plfundsrisk_data = await plfundsrisk.get_plfundsrisks_data(date)
    return plfundsrisk_data
