from fastapi import APIRouter
from services import *

plfundsrisksrouter = APIRouter()


@plfundsrisksrouter.get("/",response_model=ResponseSchema)
async def get_plfundsrisks():
    plFundsRisk = {"message": "PLFundsRisks!"}
    return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=[plFundsRisk])


@plfundsrisksrouter.get("/all",response_model=ResponseSchema)
async def get_plfundsrisks_all():
    try:
        plFundsRisk = await AlgoPLFundsRisk()
        plFundsRisks= await plFundsRisk.get_plfundsrisks_all()

        return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=plFundsRisks)
    except Exception as e:
        return exception_handler(e)


@plfundsrisksrouter.get("/{date}",response_model=ResponseSchema)
async def get_plfundsrisks_data(date: str):
    try:
        plFundsRisk = await AlgoPLFundsRisk()
        plFundsRisk_data = await plFundsRisk.get_plfundsrisks_data(date)
        return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=[plFundsRisk_data])
    except Exception as e:
        return exception_handler(e)