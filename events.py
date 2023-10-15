from fastapi import APIRouter, Request
from sse_starlette.sse import EventSourceResponse
import asyncio

from commons_telegram import *

eventsrouter = APIRouter()

EVENT_STREAM_DELAY = 1  # second
EVENT_STREAM_RETRY_TIMEOUT = 15000  # milisecond

COUNTER = 0


def get_event():
    global COUNTER
    COUNTER += 1
    return COUNTER, COUNTER < 21

@eventsrouter.get("/")
async def event_stream(request: Request):
    async def event_generator():
        while True:
            if await request.is_disconnected():
                await log_with_bot('w',f"Request disconnected : {request}")
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