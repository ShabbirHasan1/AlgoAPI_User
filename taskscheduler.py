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
async def upate_plfundsrisk():

    if settings.Broker == 'Finvasia':

        algoBroker = AlgoBroker(settings.Broker, settings.UserId)
        funds_data = await algoBroker.get_funds_data()
        funds_data = funds_data.get('data', [{}])[0]

        plFundsRisk_data = PLFundsRiskSchema(
            Broker=settings.Broker,
            UserId=settings.UserId,
            DateTime=str(datetime.datetime.now().replace(microsecond=0)),
            StartOfTheDayBalance=funds_data.get('AvailableMargin',0.0),
            AvailableBalance=funds_data.get('AvailableMargin',0.0),
            UtilizedBalance=2000.0,
            UtilizationPercentage=20.0,
            UnrealizedProfit=500.0,
            RealizedProfit=300.0,
            PnlAmount=800.0,
            PnlPercentage=8.0,
            RiskAmount=200.0,
            RiskPercentage=2.0
        )

        plFundsRisk = await AlgoPLFundsRisk(settings.Broker, settings.UserId)
        response = await plFundsRisk.create(plFundsRisk_data)

        await  log_with_bot('i',f"PLFundsRisks Updated  : {funds_data.get('AvailableMargin',0.0)}")

# @TaskScheduler.scheduled_job('cron', hour=15, minute=25)
# async def cron_task():
#     await signal_generate_SIP_INV()

if master_host == '65.2.91.59':
    TaskScheduler.add_job(upate_plfundsrisk, 'interval',  seconds=900, start_date=settings.MarketOpenTime,end_date=settings.MarketCloseTime)