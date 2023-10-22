from fastapi import APIRouter
from services import *

plfundsrisksrouter = APIRouter()


@plfundsrisksrouter.get("/",response_model=ResponseSchema)
async def get_plfundsrisks_all():
    try:
        plfundsrisk = await AlgoPLFundsRisk()
        plfundsrisks= await plfundsrisk.get_plfundsrisks_all()

        return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=plfundsrisks)
    except Exception as e:
        return exception_handler(e)


@plfundsrisksrouter.get("/{date}",response_model=ResponseSchema)
async def get_plfundsrisks_data(date: str):
    try:
        plfundsrisk = await AlgoPLFundsRisk()
        plfundsrisk_data = await plfundsrisk.get_plfundsrisks_data(date)
        return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=[plfundsrisk_data])
    except Exception as e:
        return exception_handler(e)