import json
from fastapi import APIRouter, Request
from sse_starlette.sse import EventSourceResponse
import asyncio
from commons_telegram import *

streamsrouter = APIRouter()

EVENT_STREAM_DELAY = 1  # second
EVENT_STREAM_RETRY_TIMEOUT = 15000  # milisecond

COUNTER = 0

LOGFILE = f"LogFiles/AlgoAPI_User_LogFile.log"

def get_event():
    global COUNTER
    COUNTER += 1
    return COUNTER, COUNTER < 21



@streamsrouter.get("/stream-logs")
async def straem_logs(request: Request):
    async def logGenerator():
        with open(LOGFILE, "r") as log_file:
            log_file.seek(0, os.SEEK_END)
            while True:
                if await request.is_disconnected():
                    await log_with_bot('w', f"Request disconnected : {request}")
                    break

                line = log_file.readline()
                if not line:
                    await asyncio.sleep(EVENT_STREAM_DELAY)
                    continue
                yield {line}


    return EventSourceResponse(logGenerator())


@streamsrouter.get("/stream-events")
async def stream_events(request: Request):
    async def event_generator():
        while True:
            if await request.is_disconnected():
                await log_with_bot('w', f"Request disconnected : {request}")
                break

            # Checks for new messages and return them to client if any
            counter, exists = get_event()
            if exists:
                yield {
                    "event": "new_event",
                    "id": "event_id",
                    "retry": EVENT_STREAM_RETRY_TIMEOUT,
                    "data": f"Counter value {counter}",
                }
            else:
                yield {
                    "event": "end_event",
                    "id": "event_id",
                    "retry": EVENT_STREAM_RETRY_TIMEOUT,
                    "data": "End of the stream",
                }

            await asyncio.sleep(EVENT_STREAM_DELAY)

    return EventSourceResponse(event_generator())
