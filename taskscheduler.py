from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta, date

TaskScheduler = AsyncIOScheduler()


# # Schedule the task to run every 60 seconds
# TaskScheduler.add_job(print_hello,args=[1], trigger="interval", seconds=5)

# @TaskScheduler.scheduled_job('interval', seconds=5)
# async def interval_task():
#     print(f'interval task is run... {datetime.datetime.now()}')


# @TaskScheduler.scheduled_job('interval', seconds=60, start_date=settings.MarketOpenTime,end_date=settings.MarketCloseTime)
# async def interval_task():
#     try:
#         # Key = 'TriggerTime'
#         # Value = str(datetime.datetime.now())
#         # await settings.kafka_producer.send('TradeSignals', key=Key, value=Value)
#     except Exception as e:
#         await  log_with_bot('e', e)



# @TaskScheduler.scheduled_job('cron', hour=15, minute=25)
# async def cron_task():
#     await signal_generate_SIP_INV()
