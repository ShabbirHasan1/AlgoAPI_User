from fastapi.encoders import jsonable_encoder
from commons_telegram import *
from respositories import *
import pandas as pd
import asyncio
import datetime



class AlgoSpread:
    def __init__(self,broker,userid):
        super().__init__()
        self.broker = broker
        self.userid = userid
        self.SpreadsRepository = None


    async def async_init(self):
        self.SpreadsRepository = await get_SpreadsRepository()
        return self

    def __await__(self):
        return self.async_init().__await__()

    async def get_spreads_strategy(self, strategy):
        try:
            spreads = await self.SpreadsRepository.fetch_by_strategy(strategy)
            if len(spreads) == 0:
                raise DataNotFoundException(f"Spread data not found {strategy}")
            # return [SpreadsSchemaOut(**record.__dict__) for record in spreads]
            return jsonable_encoder(spreads)
        except Exception as e:
            await log_with_bot('e', e)
            raise e

    async def get_spreads_strategy_status(self, strategy,status):
        try:
            spreads = await self.SpreadsRepository.fetch_by_strategy_status(strategy,status)
            if len(spreads) == 0:
                raise DataNotFoundException(f"Spread data not found {strategy}")
            # return [SpreadsSchemaOut(**record.__dict__) for record in spreads]
            return jsonable_encoder(spreads)
        except Exception as e:
            await log_with_bot('e', e)
            raise e

    async def get_spread(self, spreadid):
        try:
            spread_data = await self.SpreadsRepository.fetch_by_spreadid(spreadid)
            if spread_data is None:
                raise DataNotFoundException(f"Spread data not found")
            # return SpreadsSchemaOut(**spread_data.__dict__)
            return jsonable_encoder(spread_data)
        except Exception as e:
            await log_with_bot('e', e)
            raise e

    async def get_spreads_all(self):
        try:
            spreads = await self.SpreadsRepository.fetch_all()
            if len(spreads) == 0:
                raise DataNotFoundException(f"Spread data not found")

            # return [SpreadsSchemaOut(**record.__dict__) for record in spreads]
            return jsonable_encoder(spreads)
        except Exception as e:
            await log_with_bot('e', e)
            raise e

    async def calculate_margin(self, spread):
        pass

    async def update(self, spread):
        try:
            spread_data = await self.SpreadsRepository.update(spread)
            if spread_data is None:
                raise DataNotFoundException(f"Spread data not found")
            # return SpreadsSchemaOut(**spread_data.__dict__)
            return jsonable_encoder(spread_data)

        except Exception as e:
            await log_with_bot('e', e)
            raise e

    async def delete(self, spreadid):
        try:
            spread_data = await self.SpreadsRepository.delete(spreadid)
            if spread_data is None:
                raise DataNotFoundException(f"Spread data not found {spreadid}")
            # return SpreadsSchemaOut(**spread_data.__dict__)
            return jsonable_encoder(spread_data)

        except Exception as e:
            await log_with_bot('e', e)
            raise e

    async def create(self,spread):
        try:
            spread_data = await self.SpreadsRepository.create(spread)
            # return SpreadsSchemaOut(**spread_data.__dict__)
            return jsonable_encoder(spread_data)

        except Exception as e:
            await log_with_bot('e', e)
            raise e

    async def create_credit_spread(self,signal):
        pass
        # leg1CreateOrder = CreateOrderSchema(strategy="string",
        #                                     exchange="NSE",
        #                                     segment="nse_cm",
        #                                     symbol="string",
        #                                     productType="CNC",
        #                                     orderType="L",
        #                                     orderPurpose="Entry",
        #                                     transactionType="B",
        #                                     quantity=0,
        #                                     orderPrice=0,
        #                                     triggerPrice=0,
        #                                     validity="DAY",
        #                                     amo="NO",
        #                                     tag=""
        #                                     )
        #
        # leg2CreateOrder = CreateOrderSchema(strategy="string",
        #                                     exchange="NSE",
        #                                     segment="nse_cm",
        #                                     symbol="string",
        #                                     productType="CNC",
        #                                     orderType="L",
        #                                     orderPurpose="Entry",
        #                                     transactionType="B",
        #                                     quantity=0,
        #                                     orderPrice=0,
        #                                     triggerPrice=0,
        #                                     validity="DAY",
        #                                     amo="NO",
        #                                     tag=""
        #                                     )
        #
        # leg1Details = await self.algoTrade.entry(leg1CreateOrder)
        # leg2Details = await self.algoTrade.entry(leg2CreateOrder)
        #
        # await self.create(spread)


    async def create_debit_spread(self,signal):
        pass

    async def create_naked_spread(self,signal):
        algoTrade = AlgoTrade(self.broker,self.userid)

        # leg1CreateOrder = CreateOrderSchema(strategy=signal.get('strategy'),
        #                                     exchange=signal.get('exchange'),
        #                                     segment=signal.get('segment'),
        #                                     symbol=signal.get('symbol'),
        #                                     productType=signal.get('productType'),
        #                                     orderType=signal.get('orderType'),
        #                                     orderPurpose=signal.get('orderPurpose'),
        #                                     transactionType=signal.get('transactionType'),
        #                                     quantity=signal.get('quantity'),
        #                                     orderPrice=signal.get('orderPrice'),
        #                                     triggerPrice=signal.get('triggerPrice'),
        #                                     validity=signal.get('validity'),
        #                                     amo=signal.get('amo'),
        #                                     tag=signal.get('tag')
        #                                     )

        leg1Details = await algoTrade.entry(signal)

        spread_data = SpreadsSchemaIn(Broker=self.broker,
                                      UserId=self.userid,
                                      Date=str(datetime.date.today()),
                                      Symbol=signal.get('symbol'),
                                      Status="Active",
                                      ExpiryDate="2023-12-31",
                                      ExpiryType="Weekly_Expiry",
                                      ProductType=signal.get('productType'),
                                      Exchange=signal.get('exchange'),
                                      Segment=signal.get('segment'),
                                      TradeType="Systematic",
                                      Trend="Buy",
                                      Spot_Price=150.0,
                                      Strike=160.0,
                                      Leg1_Strike=0,
                                      Leg1_Side='Buy',
                                      Leg1_Symbol=signal.get('symbol'),
                                      Leg1_Qty=signal.get('quantity'),
                                      Leg1_BuyPrice=0,
                                      Leg1_BuyOrderId=leg1Details['data'][0].get('nOrdNo'),
                                      Leg1_SellPrice=0,
                                      Leg1_SellOrderId=0,
                                      Leg1_Sl_Price=0,
                                      Leg1_Sl_OrderId=0,
                                      Leg1_Tg_Price=0,
                                      Leg1_Tg_OrderId=0,
                                      Leg1_Pnl=0,
                                      Leg2_Strike=0,
                                      Leg2_Side=None,
                                      Leg2_Symbol='xxx',
                                      Leg2_Qty=0,
                                      Leg2_BuyPrice=0,
                                      Leg2_BuyOrderId=0,
                                      Leg2_SellPrice=0,
                                      Leg2_SellOrderId=0,
                                      Leg2_Sl_Price=0,
                                      Leg2_Sl_OrderId=0,
                                      Leg2_Tg_Price=0,
                                      Leg2_Tg_OrderId=0,
                                      Leg2_Pnl=0,
                                      Trade_StartTime=str(datetime.datetime.now().replace(microsecond=0)),
                                      Trade_EndTime=str(datetime.datetime.now().replace(microsecond=0)),
                                      Total_Premium=250.0,
                                      Total_Sl=17.0,
                                      LastPrice=155.0,
                                      LastPriceDate=str(datetime.datetime.now().replace(microsecond=0)),
                                      MarketValue=750.0,
                                      Strategy=signal.get('strategy'),
                                      Instrument=signal.get('instrument'),
                                      Pyramid=1,
                                      UnderlyingSymbol=signal.get('underlyingSymbol'),
                                      TradeDuration=signal.get('tradeDuration'),
                                      SpreadNumber=1,
                                      SpreadType="NakedBuy",
                                      SpreadStatus="Full",
                                      Pnl=150.0,
                                      Charges=5.0,
                                      PnlNet=145.0,
                                      Remarks="This is a dummy record",
                                      )

        # spread_data = SpreadsSchemaIn(Broker=self.broker,
        #                               UserId=self.userid,
        #                               Date=str(datetime.date.today()),
        #                               Symbol=signal.get('symbol'),
        #                               Status="Active",
        #                               ExpiryDate="2023-12-31",
        #                               ExpiryType="Weekly_Expiry",
        #                               ProductType=signal.get('productType'),
        #                               Exchange=signal.get('exchange'),
        #                               Segment=signal.get('segment'),
        #                               TradeType="Systematic",
        #                               Trend="Buy",
        #                               Spot_Price=150.0,
        #                               Strike=160.0,
        #                               Leg1_Strike=leg1Details.get(''),
        #                               Leg1_Side=leg1Details.get(''),
        #                               Leg1_Symbol=leg1Details.get(''),
        #                               Leg1_Qty=leg1Details.get(''),
        #                               Leg1_BuyPrice=leg1Details.get(''),
        #                               Leg1_BuyOrderId=leg1Details.get(''),
        #                               Leg1_SellPrice=leg1Details.get(''),
        #                               Leg1_SellOrderId=leg1Details.get(''),
        #                               Leg1_Sl_Price=leg1Details.get(''),
        #                               Leg1_Sl_OrderId=leg1Details.get(''),
        #                               Leg1_Tg_Price=leg1Details.get(''),
        #                               Leg1_Tg_OrderId=leg1Details.get(''),
        #                               Leg1_Pnl=leg1Details.get(''),
        #                               Leg2_Strike=leg1Details.get(''),
        #                               Leg2_Side=leg1Details.get(''),
        #                               Leg2_Symbol=leg1Details.get(''),
        #                               Leg2_Qty=leg1Details.get(''),
        #                               Leg2_BuyPrice=leg1Details.get(''),
        #                               Leg2_BuyOrderId=leg1Details.get(''),
        #                               Leg2_SellPrice=leg1Details.get(''),
        #                               Leg2_SellOrderId=leg1Details.get(''),
        #                               Leg2_Sl_Price=leg1Details.get(''),
        #                               Leg2_Sl_OrderId=leg1Details.get(''),
        #                               Leg2_Tg_Price=leg1Details.get(''),
        #                               Leg2_Tg_OrderId=leg1Details.get(''),
        #                               Leg2_Pnl=leg1Details.get(''),
        #                               Trade_StartTime=str(datetime.datetime.now().replace(microsecond=0)),
        #                               Trade_EndTime=str(datetime.datetime.now().replace(microsecond=0)),
        #                               Total_Premium=250.0,
        #                               Total_Sl=17.0,
        #                               LastPrice=155.0,
        #                               LastPriceDate=str(datetime.datetime.now().replace(microsecond=0)),
        #                               MarketValue=750.0,
        #                               Strategy=signal.get('strategy'),
        #                               Instrument=signal.get('instrument'),
        #                               Pyramid=1,
        #                               UnderlyingSymbol=signal.get('underlyingSymbol'),
        #                               TradeDuration=signal.get('tradeDuration'),
        #                               SpreadNumber=1,
        #                               SpreadType="NakedBuy",
        #                               SpreadStatus="Full",
        #                               Pnl=150.0,
        #                               Charges=5.0,
        #                               PnlNet=145.0,
        #                               Remarks="This is a dummy record",
        #                               )

        spread = await self.create(spread_data)
        return spread

    async def create_strangle_spread(self,signal):
            pass


class AlgoHedge:
    def __init__(self,broker,userid):
        super().__init__()
        self.broker = broker
        self.userid = userid
        self.HedgesRepository = None

    async def async_init(self):
        self.HedgesRepository = await get_HedgesRepository()
        return self

    def __await__(self):
        return self.async_init().__await__()

    async def get_hedges_strategy(self, strategy):
        try:
            hedges = await self.HedgesRepository.fetch_by_strategy(strategy)
            if len(hedges) == 0:
                raise DataNotFoundException(f"Hedge data not found")
            # return [HedgesSchemaOut(**record.__dict__) for record in hedges]
            return jsonable_encoder(hedges)
        except Exception as e:
            await log_with_bot('e', e)
            raise e
    async def get_hedges_strategy_status(self, strategy,status):
        try:
            hedges = await self.HedgesRepository.fetch_by_strategy_status(strategy,status)
            if len(hedges) == 0:
                raise DataNotFoundException(f"Hedge data not found")
            # return [HedgesSchemaOut(**record.__dict__) for record in hedges]
            return jsonable_encoder(hedges)
        except Exception as e:
            await log_with_bot('e', e)
            raise e

    async def get_hedge(self, hedgeid):
        try:
            hedge_data = await self.HedgesRepository.fetch_by_hedgeid(hedgeid)
            if hedge_data is None:
                raise DataNotFoundException(f"Hedge data not found")
            # return HedgesSchemaOut(**hedge_data.__dict__)
            return jsonable_encoder(hedge_data)
        except Exception as e:
            await log_with_bot('e', e)
            raise e

    async def get_hedges_all(self):
        try:
            hedges = await self.HedgesRepository.fetch_all()
            if len(hedges) == 0:
                raise DataNotFoundException(f"Hedge data not found")
            # return [HedgesSchemaOut(**record.__dict__) for record in hedges]
            return jsonable_encoder(hedges)
        except Exception as e:
            await log_with_bot('e', e)
            raise e


    async def update(self, hedge):
        try:
            hedge_data = await self.HedgesRepository.update(hedge)
            if hedge_data is None:
                raise DataNotFoundException(f"Hedge data not found")
            # return HedgesSchemaOut(**hedge_data.__dict__)
            return jsonable_encoder(hedge_data)
        except Exception as e:
            await log_with_bot('e', e)
            raise e

    async def delete(self, hedgeid):
        try:
            hedge_data = await self.HedgesRepository.delete(hedgeid)
            if hedge_data is None:
                raise DataNotFoundException(f"Hedge data not found {hedgeid}")
            # return HedgesSchemaOut(**hedge_data.__dict__)
            return jsonable_encoder(hedge_data)
        except Exception as e:
            await log_with_bot('e', e)
            raise e

    async def create(self,hedge):
        try:
            hedge_data = await self.HedgesRepository.create(hedge)
            # return HedgesSchemaOut(**hedge_data.__dict__)
            return jsonable_encoder(hedge_data)
        except Exception as e:
            await log_with_bot('e', e)
            raise e


class AlgoPLFundsRisk:
    def __init__(self,broker,userid):
        super().__init__()
        self.broker = broker
        self.userid = userid
        self.PLFundsRiskRepository = None

    async def async_init(self):
        self.PLFundsRiskRepository = await get_PLFundsRiskRepository()
        return self

    def __await__(self):
        return self.async_init().__await__()

    async def get_plfundsrisks_data(self, date):
        try:
            plfundsrisks = await self.PLFundsRiskRepository.fetch_by_date(date)
            if len(plfundsrisks) == 0:
                raise DataNotFoundException(f"PLFundsRisk data not found : {date}")
            # return [PLFundsRiskSchema(**record.__dict__) for record in plfundsrisks]
            return jsonable_encoder(plfundsrisks)
        except Exception as e:
            await log_with_bot('e', e)
            raise e


    async def get_plfundsrisks_all(self):
        try:
            plfundsrisks = await self.PLFundsRiskRepository.fetch_all()
            if len(plfundsrisks) == 0:
                raise DataNotFoundException(f"PLFundsRisk data not found")
            # return [PLFundsRiskSchema(**record.__dict__) for record in plfundsrisks]
            return jsonable_encoder(plfundsrisks)
        except Exception as e:
            await log_with_bot('e', e)
            raise e


class AlgoPLDateSummary:
    def __init__(self,broker,userid):
        super().__init__()
        self.broker = broker
        self.userid = userid
        self.PLDateSummaryRepository = None

    async def async_init(self):
        self.PLDateSummaryRepository = await get_PLDateSummaryRepository()
        return self

    def __await__(self):
        return self.async_init().__await__()

    async def get_pldatesummarys_data(self, date):
        try:
            pldatesummarys = await self.PLDateSummaryRepository.fetch_by_date(date)
            if len(pldatesummarys) == 0:
                raise DataNotFoundException(f"PLDateSummary data not found : {date}")
            # return [PLDateSummarySchema(**record.__dict__) for record in pldatesummarys]
            return jsonable_encoder(pldatesummarys)
        except Exception as e:
            await log_with_bot('e', e)
            raise e


    async def get_pldatesummarys_all(self):
            try:
                pldatesummarys= await self.PLDateSummaryRepository.fetch_all()
                if len(pldatesummarys) == 0:
                    raise DataNotFoundException(f"PLDateSummary data not found")
                # return [PLDateSummarySchema(**record.__dict__) for record in pldatesummarys]
                return jsonable_encoder(pldatesummarys)
            except Exception as e:
                await log_with_bot('e', e)
                raise e

class AlgoTrade:
    def __init__(self,broker,userid):
        super().__init__()
        self.broker = broker
        self.userid = userid
        self.algoBroker = AlgoBroker(self.broker, self.userid)

    async def async_init(self):
        return self

    def __await__(self):
        return self.async_init().__await__()

    async def entry(self,order):
        tradeDetails = {}
        mainOrderDetails = await self.algoBroker.create_order(order)
        # if mainOrderDetails is not None:
        #     print(mainOrderDetails)

        # slOrderDetails = await self.algoBroker.create_order(order)
        # if slOrderDetails is not None:
        #     print(slOrderDetails)
        #
        # tgOrderDetails = await self.algoBroker.create_order(order)
        # if tgOrderDetails is not None:
        #     print(tgOrderDetails)

        return mainOrderDetails

    async def exit(self,order):
        exitDetails = self.algoBroker.create_order(order)
        return exitDetails


class AlgoUser():
    def __init__(self, broker, userid):
        self.broker = broker
        self.userid = userid

    async def execute_signals(self,signallist):
        algoSpread = await AlgoSpread(self.broker,self.userid)

        for signal in signallist:
            await log_with_bot('i', f'signal : {signal}')

            resp = await algoSpread.create_naked_spread(signal)
            print(resp)



            # spread = await algoSpread.create_credit_spread(signal)
            #
            # # activeSpreads = await self.algoSpread.get_spreads_data(signal)
            # # for spread in activeSpreads:
            # #     print(spread)



