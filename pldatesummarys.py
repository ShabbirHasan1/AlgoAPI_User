from fastapi import APIRouter
from services import *

pldatesummarysrouter = APIRouter()

@pldatesummarysrouter.get("/",response_model=ResponseSchema)
async def get_pldatesummarys():
    plDateSummarys = {"message": "PLDataSummarys!"}
    return ResponseSchema(status='success', code='spread', description='ok', data=[plDateSummarys])


@pldatesummarysrouter.get("/all",response_model=ResponseSchema)
async def get_pldatesummarys_all():
    try:
        plDateSummary = await AlgoPLDateSummary()
        plDateSummarys = await plDateSummary.get_pldatesummarys_all()
        return ResponseSchema(status='success', code='pldatesummary', description='ok', data=plDateSummarys)
    except Exception as e:
        return exception_handler(e)

@pldatesummarysrouter.get("/{date}",response_model=ResponseSchema)
async def get_pldatesummarys_data(date: str):
    try:
        plDateSummary = await AlgoPLDateSummary()
        plDateSummary_data = await plDateSummary.get_pldatesummarys_data(date)
        return ResponseSchema(status='success', code='pldatesummary', description='ok', data=[plDateSummary_data])
    except Exception as e:
        return exception_handler(e)