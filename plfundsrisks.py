from fastapi import APIRouter
from services import *

plfundsrisksrouter = APIRouter()


@plfundsrisksrouter.get("/",response_model=ResponseSchema)
async def get_plfundsrisk():
    plFundsRisk = {"message": "PLFundsRisks!"}
    return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=[plFundsRisk])


@plfundsrisksrouter.get("/all",response_model=ResponseSchema)
async def get_plfundsrisk_all():
    try:
        plFundsRisk = await AlgoPLFundsRisk(settings.Broker,settings.UserId)
        plFundsRisks= await plFundsRisk.get_plfundsrisks_all()

        return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=plFundsRisks)
    except Exception as e:
        return exception_handler(e)


@plfundsrisksrouter.get("/{date}",response_model=ResponseSchema)
async def get_plfundsrisk_data(date: str):
    try:
        plFundsRisk = await AlgoPLFundsRisk(settings.Broker,settings.UserId)
        plFundsRisk_data = await plFundsRisk.get_plfundsrisks_data(date)
        return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=[plFundsRisk_data])
    except Exception as e:
        return exception_handler(e)


@plfundsrisksrouter.post("/createplfundsrisk",response_model=ResponseSchema)
async def create_spread_data(plfundsrisk: PLFundsRiskSchema):
    try:
        plFundsRisk = await AlgoPLFundsRisk(settings.Broker,settings.UserId)
        plFundsRisk_data = await plFundsRisk.create(plfundsrisk)
        return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=[plFundsRisk_data])
    except Exception as e:
        return exception_handler(e)

@plfundsrisksrouter.put("/updateplfundsrisk",response_model=ResponseSchema)
async def update_spread_data(plfundsrisk: PLFundsRiskSchema):
    try:
        plFundsRisk = await AlgoPLFundsRisk(settings.Broker,settings.UserId)
        plFundsRisk_data = await plFundsRisk.update(plfundsrisk)
        return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=[plFundsRisk_data])
    except Exception as e:
        return exception_handler(e)


@plfundsrisksrouter.delete("/deleteplfundsrisk",response_model=ResponseSchema)
async def delete_spread_data(broker: str,userid: str, datetime: str):
    try:
        plFundsRisk = await AlgoPLFundsRisk(settings.Broker,settings.UserId)
        plFundsRisk_data = await plFundsRisk.delete(broker,userid,datetime)
        return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=[plFundsRisk_data])
    except Exception as e:
        return exception_handler(e)