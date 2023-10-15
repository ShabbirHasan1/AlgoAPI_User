from fastapi import APIRouter
from services import *

pldatesummarysrouter = APIRouter()

@pldatesummarysrouter.get("/")
async def get_pldatesummarys_all():
    pldatesummary = await AlgoPLDateSummary()
    pldatesummary_data = await pldatesummary.get_pldatesummarys_all()
    return pldatesummary_data

@pldatesummarysrouter.get("/{date}")
async def get_pldatesummarys_data(date: str):
    pldatesummary = await AlgoPLDateSummary()
    pldatesummary_data = await pldatesummary.get_pldatesummarys_data(date)
    return pldatesummary_data