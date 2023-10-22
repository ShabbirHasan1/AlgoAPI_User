from fastapi import APIRouter
from services import *

pldatesummarysrouter = APIRouter()

@pldatesummarysrouter.get("/",response_model=ResponseSchema)
async def get_pldatesummarys_all():
    try:
        pldatesummary = await AlgoPLDateSummary()
        pldatesummarys = await pldatesummary.get_pldatesummarys_all()
        return ResponseSchema(status='success', code='pldatesummary', description='ok', data=pldatesummarys)
    except Exception as e:
        return exception_handler(e)

@pldatesummarysrouter.get("/{date}",response_model=ResponseSchema)
async def get_pldatesummarys_data(date: str):
    try:
        pldatesummary = await AlgoPLDateSummary()
        pldatesummary_data = await pldatesummary.get_pldatesummarys_data(date)
        return ResponseSchema(status='success', code='pldatesummary', description='ok', data=[pldatesummary_data])
    except Exception as e:
        return exception_handler(e)