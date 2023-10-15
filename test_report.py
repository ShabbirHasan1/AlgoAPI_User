from commons_kafka import *
from services import *
import aiohttp

initialize_logger()
initialize_telegram()



async def main():

    try:

        pass

        # screenerList = await get_screener_stocks_chartink('kgl-mtf-up-v1')
        # print(screenerList)

        # await initialize_kafka()
        # ats = AlgoTradeSignal()
        # tasks = []
        # screenerList = await get_screener_stocks_chartink('kgl-mtf-up-v1')
        # for item in screenerList:
        #     task = asyncio.create_task(ats.signal_generate_SIP_INV_MTP_POS(item['nsecode'], 'MTF_POS'))
        #     tasks.append(task)
        #
        # ts_list = await asyncio.gather(*tasks)
        #
        # for ts in ts_list:
        #     if ts is not None:
        #         Key = 'MTF_POS'
        #         Value = ts
        #         await settings.kafka_producer.send('TradeSignals', key=Key, value=Value)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(main())

