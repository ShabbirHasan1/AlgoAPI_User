from fastapi import APIRouter
from services import *

pldatesummarysrouter = APIRouter()

@pldatesummarysrouter.get("/",response_model=ResponseSchema)
async def get_pldatesummary():
    plDateSummarys = {"message": "PLDataSummarys!"}
    return ResponseSchema(status='success', code='spread', description='ok', data=[plDateSummarys])


@pldatesummarysrouter.get("/all",response_model=ResponseSchema)
async def get_pldatesummary_all():
    try:
        plDateSummary = await AlgoPLDateSummary(settings.Broker,settings.UserId)
        plDateSummarys = await plDateSummary.get_pldatesummarys_all()
        return ResponseSchema(status='success', code='pldatesummary', description='ok', data=plDateSummarys)
    except Exception as e:
        return exception_handler(e)

@pldatesummarysrouter.get("/{date}",response_model=ResponseSchema)
async def get_pldatesummary_data(date: str):
    try:
        plDateSummary = await AlgoPLDateSummary(settings.Broker,settings.UserId)
        plDateSummary_data = await plDateSummary.get_pldatesummarys_data(date)
        return ResponseSchema(status='success', code='pldatesummary', description='ok', data=[plDateSummary_data])
    except Exception as e:
        return exception_handler(e)


@pldatesummarysrouter.post("/createpldatesummary",response_model=ResponseSchema)
async def create_spread_data(pldatesummary: PLDateSummarySchema):
    try:
        plDateSummary = await AlgoPLDateSummary(settings.Broker,settings.UserId)
        plDateSummary_data = await plDateSummary.create(pldatesummary)
        return ResponseSchema(status='success', code='pldatesummary', description='ok', data=[plDateSummary_data])
    except Exception as e:
        return exception_handler(e)

@pldatesummarysrouter.put("/updatepldatesummary",response_model=ResponseSchema)
async def update_spread_data(pldatesummary: PLDateSummarySchema):
    try:
        plDateSummary = await AlgoPLDateSummary(settings.Broker,settings.UserId)
        plDateSummary_data = await plDateSummary.update(pldatesummary)
        return ResponseSchema(status='success', code='pldatesummary', description='ok', data=[plDateSummary_data])
    except Exception as e:
        return exception_handler(e)


@pldatesummarysrouter.delete("/deletepldatesummary",response_model=ResponseSchema)
async def delete_spread_data(broker: str,userid: str, date: str):
    try:
        plDateSummary = await AlgoPLDateSummary(settings.Broker,settings.UserId)
        plDateSummary_data = await plDateSummary.delete(broker,userid,date)
        return ResponseSchema(status='success', code='pldatesummary', description='ok', data=[plDateSummary_data])
    except Exception as e:
        return exception_handler(e)