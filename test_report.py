import datetime
import time

from commons_kafka import *
from services import *
import aiohttp

initialize_logger()
initialize_telegram()



async def main():

    try:
        broker = 'Kotak'
        userid = 'XWQF2'
        kotak = AlgoBroker(broker, userid)

        # while True:
        #     order = {
        #         "orderid": 231104000006347,
        #         "amo": "NO"
        #     }
        #
        #     kotak = AlgoBroker(broker, userid)
        #     print(await kotak.cancel_order(order))
        #
        #     break
        #     # time.sleep(1)

        while True:
            start_time = datetime.datetime.now()
            order ={
                    "strategy": "Test1",
                    "exchange": "NSE",
                    "segment": "nse_cm",
                    "symbol": "ITC",
                    "productType": "CNC",
                    "orderType": "MKT",
                    "orderPurpose": "Entry",
                    "transactionType": "B",
                    "quantity": 1,
                    "orderPrice": 430,
                    "triggerPrice": 430,
                    "validity": "DAY",
                    "amo": "NO",
                    "tag": ""
                }

            # t = threading.Thread(target=lambda: asyncio.run(kotak.create_order(order)))
            # t.start()

            response = await kotak.create_order(order)
            end_time = datetime.datetime.now()
            time_taken = (end_time - start_time).microseconds/ 1000
            print(time_taken,response)
            break
            # time.sleep(1)

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

