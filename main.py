import threading
import time
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum


from commons_kafka import *
from spreads import *
from hedges import *
from plfundsrisks import *
from pldatesummarys import *
from tasks import *
from webhooks import *
from streams import *


app = FastAPI(title=f"AlgoAPI_User_{settings.Broker}_{settings.UserId}" , version="1.0")
router = APIRouter()
router.include_router(spreadsrouter, prefix="/spreads", tags=["Spreads"])
router.include_router(hedgessrouter, prefix="/hedges", tags=["Hedges"])
router.include_router(plfundsrisksrouter, prefix="/plfundsrisks", tags=["PLFundsRisks"])
router.include_router(pldatesummarysrouter, prefix="/pldatesummarys", tags=["PLDateSummarys"])
router.include_router(tasksrouter, prefix="/tasks", tags=["Tasks"])
router.include_router(webhooksrouter, prefix="/webhooks", tags=["WebHooks"])
router.include_router(streamsrouter, prefix="/streams", tags=["Streams"])


app.include_router(router)
handler = Mangum(app)

# Define CORS configuration
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:3000",
    "http://192.168.1.99",
    "http://192.168.1.99:3000",
    "http://65.2.91.59",
    "http://65.2.91.59:33000",
    "http://65.2.91.59:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

initialize_logger()
initialize_telegram()


@app.on_event("startup")
async def startup_event():
    try:
        await log_with_bot('i', f"API User Server Started...{os.getpid()}")
        await initialize_kafka()
        asyncio.create_task(consume_messages_kafka())

    except Exception as e:
        await log_with_bot('e', e)


@app.on_event("shutdown")
async def shutdown_event():
    try:
        await settings.kafka_producer.stop()
        await settings.kafka_consumer.stop()

        await log_with_bot('i', f"API User Server Stopped...{os.getpid()}")

    except Exception as e:
        await log_with_bot('e', e)


@app.get("/")
async def root(username: str = Depends(validate_credentials)):
    return {"AlgoAPI_User is Alive : " + str(username)}



async def trigger_task_scheduler():
    await initialize_kafka()
    asyncio.create_task(consume_messages_kafka())

    await log_with_bot('i', f"Tasks Scheduler Started...{os.getpid()}")

    # start the scheduler
    TaskScheduler.start()
    # Keep the script running
    await asyncio.Event().wait()


if __name__ == "__main__":

    if is_running_in_docker():
        if not (settings.MarketOpenTime < datetime.datetime.now() < settings.MarketCloseTime):
            time.sleep(55)

    t = threading.Thread(target=asyncio.run, args=(trigger_task_scheduler(),))
    t.start()

    uvicorn.run("main:app",
                host=str(settings.API_HOST),
                port=int(settings.API_PORT),
                log_config="logging.conf",
                workers=settings.API_WORKERS)
