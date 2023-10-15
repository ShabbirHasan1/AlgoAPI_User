from fastapi import APIRouter
from services import *

useraccountrouter = APIRouter()


@useraccountrouter.get("/{broker}/{userid}")
async def get_user_data(broker: str, userid: str):
    master = AlgoMaster()
    user_data = await master.get_user_data(broker,userid)
    return user_data