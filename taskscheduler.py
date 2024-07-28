from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta, date
from services import *

TaskScheduler = AsyncIOScheduler()
master_host = os.getenv('MASTER_HOST')

# @TaskScheduler.scheduled_job('interval', seconds=180, start_date=settings.MarketOpenTime,end_date=settings.MarketCloseTime)
# async def interval_task_3mins():
#     await log_with_bot('i',f"Task-3Mins : {datetime.datetime.now()}")
#
# @TaskScheduler.scheduled_job('interval', seconds=300, start_date=settings.MarketOpenTime,end_date=settings.MarketCloseTime)
async def interval_task_5mins():
    await log_with_bot('i',f"Task-5Mins : {datetime.datetime.now()}")
#
# @TaskScheduler.scheduled_job('interval', seconds=900, start_date=settings.MarketOpenTime,end_date=settings.MarketCloseTime)
# async def interval_task_15mins():
#     await log_with_bot('i',f"Task-15Mins : {datetime.datetime.now()}")
#
# @TaskScheduler.scheduled_job('interval', seconds=3600, start_date=settings.MarketOpenTime,end_date=settings.MarketCloseTime)
# async def interval_task_60mins():
#     await log_with_bot('i',f"Task-60Mins : {datetime.datetime.now()}")


# @TaskScheduler.scheduled_job('cron', hour=15, minute=25)
# async def cron_task():
#     await signal_generate_SIP_INV()

if master_host == '65.2.91.59':
    TaskScheduler.add_job(interval_task_5mins, 'interval',  seconds=300, start_date=settings.MarketOpenTime,end_date=settings.MarketCloseTime)