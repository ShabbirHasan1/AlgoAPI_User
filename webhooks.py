from fastapi import APIRouter, BackgroundTasks,Request

from services import *

webhooksrouter = APIRouter()


@webhooksrouter.post("/event/")
async def webhook_event(request: Request, background_tasks: BackgroundTasks):
    payload = await request.json()
    background_tasks.add_task(process_event, payload)
    return {"status_code": 200, "message": "Event received and being processed in the background"}


@webhooksrouter.post("/tradesignal/")
async def webhook_tradesignal(request: Request, background_tasks: BackgroundTasks):
    payload = await request.json()
    background_tasks.add_task(process_trade_signal, payload)
    return {"status_code": 200, "message": "Trade signal received and being processed in the background"}


async def process_event(event: dict):
    try:
        print(f"Event {event} processed.")
    except Exception as e:
        await log_with_bot('e',e)


async def process_trade_signal(tradesignal: dict):
    try:
        print(f"Trade signal {tradesignal} processed.")
    except Exception as e:
        await log_with_bot('e', e)
