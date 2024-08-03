import datetime
import time

from commons_kafka import *
from services import *
from taskscheduler import *
import aiohttp

initialize_logger()
initialize_telegram()



async def main():

    try:
        # broker = 'Kotak'
        # userid = 'XWQF2'
        # kotak = AlgoBroker(broker, userid)

        await upate_plfundsrisk()



        # spreads = await AlgoSpread()
        #
        # spread_data = SpreadsSchemaIn(
        #     Broker="Kotak",
        #     UserId="XWQF2",
        #     Date=str(datetime.date.today()),
        #     Symbol="TCS",
        #     Status="Active",
        #     ExpiryDate="2023-12-31",
        #     ExpiryType="Weekly_Expiry",
        #     ProductType="CNC",
        #     Exchange="NSE",
        #     Segment="NSE",
        #     TradeType="Systematic",
        #     Trend="Buy",
        #     Spot_Price=150.0,
        #     Strike=160.0,
        #     Leg1_Strike=170.0,
        #     Leg1_Side="Buy",
        #     Leg1_Symbol="TCS",
        #     Leg1_Qty=10,
        #     Leg1_BuyPrice=15.0,
        #     Leg1_BuyOrderId=1001,
        #     Leg1_SellPrice=20.0,
        #     Leg1_SellOrderId=1002,
        #     Leg1_Sl_Price=10.0,
        #     Leg1_Sl_OrderId=1003,
        #     Leg1_Tg_Price=25.0,
        #     Leg1_Tg_OrderId=1004,
        #     Leg1_Pnl=100.0,
        #     Leg2_Strike=150.0,
        #     Leg2_Side="Sell",
        #     Leg2_Symbol="xxx",
        #     Leg2_Qty=5,
        #     Leg2_BuyPrice=10.0,
        #     Leg2_BuyOrderId=2001,
        #     Leg2_SellPrice=5.0,
        #     Leg2_SellOrderId=2002,
        #     Leg2_Sl_Price=7.0,
        #     Leg2_Sl_OrderId=2003,
        #     Leg2_Tg_Price=12.0,
        #     Leg2_Tg_OrderId=2004,
        #     Leg2_Pnl=50.0,
        #     Trade_StartTime=str(datetime.datetime.now().replace(microsecond=0)),
        #     Trade_EndTime=str(datetime.datetime.now().replace(microsecond=0)),
        #     Total_Premium=250.0,
        #     Total_Sl=17.0,
        #     LastPrice=155.0,
        #     LastPriceDate=str(datetime.datetime.now().replace(microsecond=0)),
        #     MarketValue=750.0,
        #     Strategy="Test1",
        #     Instrument="Case",
        #     Pyramid=1,
        #     UnderlyingSymbol="TCS",
        #     TradeDuration="Positional",
        #     SpreadNumber=1,
        #     SpreadType="NakedBuy",
        #     SpreadStatus="Full",
        #     Pnl=150.0,
        #     Charges=5.0,
        #     PnlNet=145.0,
        #     Remarks="This is a dummy record",
        # )

        # spread_data_dict = {
        #     "Broker": "Kotak",
        #     "UserId": "XWQF2",
        #     "Date": str(datetime.date.today()),
        #     "Symbol": "TCS",
        #     "Status": "Active",
        #     "ExpiryDate": "2023-12-31",
        #     "ExpiryType": "Weekly_Expiry",
        #     "ProductType": "CNC",
        #     "Exchange": "NSE",
        #     "Segment": "NSE",
        #     "TradeType": "Systematic",
        #     "Trend": "Buy",
        #     "Spot_Price": 150.0,
        #     "Strike": 160.0,
        #     "Leg1_Strike": 170.0,
        #     "Leg1_Side": "Buy",
        #     "Leg1_Symbol": "TCS",
        #     "Leg1_Qty": 10,
        #     "Leg1_BuyPrice": 15.0,
        #     "Leg1_BuyOrderId": 1001,
        #     "Leg1_SellPrice": 20.0,
        #     "Leg1_SellOrderId": 1002,
        #     "Leg1_Sl_Price": 10.0,
        #     "Leg1_Sl_OrderId": 1003,
        #     "Leg1_Tg_Price": 25.0,
        #     "Leg1_Tg_OrderId": 1004,
        #     "Leg1_Pnl": 100.0,
        #     "Leg2_Strike": 150.0,
        #     "Leg2_Side": "Sell",
        #     "Leg2_Symbol": "xxx",
        #     "Leg2_Qty": 5,
        #     "Leg2_BuyPrice": 10.0,
        #     "Leg2_BuyOrderId": 2001,
        #     "Leg2_SellPrice": 5.0,
        #     "Leg2_SellOrderId": 2002,
        #     "Leg2_Sl_Price": 7.0,
        #     "Leg2_Sl_OrderId": 2003,
        #     "Leg2_Tg_Price": 12.0,
        #     "Leg2_Tg_OrderId": 2004,
        #     "Leg2_Pnl": 50.0,
        #     "Trade_StartTime": str(datetime.datetime.now().replace(microsecond=0)),
        #     "Trade_EndTime": str(datetime.datetime.now().replace(microsecond=0)),
        #     "Total_Premium": 250.0,
        #     "Total_Sl": 17.0,
        #     "LastPrice": 155.0,
        #     "LastPriceDate": str(datetime.datetime.now().replace(microsecond=0)),
        #     "MarketValue": 750.0,
        #     "Strategy": "Test1",
        #     "Instrument": "Case",
        #     "Pyramid": 1,
        #     "UnderlyingSymbol": "TCS",
        #     "TradeDuration": "Positional",
        #     "SpreadNumber": 1,
        #     "SpreadType": "NakedBuy",
        #     "SpreadStatus": "Full",
        #     "Pnl": 150.0,
        #     "Charges": 5.0,
        #     "PnlNet": 145.0,
        #     "Remarks": "This is a dummy record"
        # }

        # resp =  await spreads.create_spread(spread_data)
        # print(resp.TradeId)



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

        # while True:
        #     start_time = datetime.datetime.now()
        #     order ={
        #             "strategy": "Test1",
        #             "exchange": "NSE",
        #             "segment": "nse_cm",
        #             "symbol": "ITC",
        #             "productType": "CNC",
        #             "orderType": "MKT",
        #             "orderPurpose": "Entry",
        #             "transactionType": "B",
        #             "quantity": 1,
        #             "orderPrice": 430,
        #             "triggerPrice": 430,
        #             "validity": "DAY",
        #             "amo": "NO",
        #             "tag": ""
        #         }
        #
        #     # t = threading.Thread(target=lambda: asyncio.run(kotak.create_order(order)))
        #     # t.start()
        #
        #     response = await kotak.create_order(order)
        #     end_time = datetime.datetime.now()
        #     time_taken = (end_time - start_time).microseconds/ 1000
        #     print(time_taken,response)
        #     break

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

