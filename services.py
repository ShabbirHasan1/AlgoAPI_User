import datetime
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from commons_telegram import *
from respositories import *
import pandas as pd
import asyncio




class AlgoSpread:
    def __init__(self):
        super().__init__()
        self.SpreadsRepository = None

    async def async_init(self):
        self.SpreadsRepository = await get_SpreadsRepository()
        return self

    def __await__(self):
        return self.async_init().__await__()

    async def get_spreads_data(self, strategy):
        try:
            spreads = await self.SpreadsRepository.fetch_by_strategy(strategy)
            if len(spreads) == 0:
                raise DataNotFoundException(f"Spread data not found {strategy}")
            return [SpreadsSchemaOut(**record.__dict__) for record in spreads]
        except Exception as e:
            await log_with_bot('e', e)
            raise e

    async def get_spreads_all(self):
        try:
            spreads = await self.SpreadsRepository.fetch_all()
            if len(spreads) == 0:
                raise DataNotFoundException(f"Spread data not found")

            return [SpreadsSchemaOut(**record.__dict__) for record in spreads]

        except Exception as e:
            await log_with_bot('e', e)
            raise e

    async def create_spread(self,spread):
        try:
            spread_data = await self.SpreadsRepository.create(spread)
            return SpreadsSchemaOut(**spread_data.__dict__)

        except Exception as e:
            await log_with_bot('e', e)
            raise e

    async def create_credit_spread(self,spread):
        algoTrade = AlgoTrade()
        algoSpread = AlgoSpread()

        leg1Details = algoTrade.entry()
        leg2Details = algoTrade.entry()

        await algoSpread.create_spread(spread)


    async def create_debit_spread(self,spread):
        pass

    async def create_naked_spread(self,spread):
        pass

    async def create_strangle_spread(self,spread):
        pass


class AlgoHedge:
    def __init__(self):
        super().__init__()
        self.HedgesRepository = None

    async def async_init(self):
        self.HedgesRepository = await get_HedgesRepository()
        return self

    def __await__(self):
        return self.async_init().__await__()

    async def get_hedges_data(self, strategy):
        try:
            hedges = await self.HedgesRepository.fetch_by_strategy(strategy)
            if len(hedges) == 0:
                raise DataNotFoundException(f"Hedge data not found")
            return [HedgesSchemaOut(**record.__dict__) for record in hedges]
        except Exception as e:
            await log_with_bot('e', e)
            raise e

    async def get_hedges_all(self):
        try:
            hedges = await self.HedgesRepository.fetch_all()
            if len(hedges) == 0:
                raise DataNotFoundException(f"Hedge data not found")
            return [HedgesSchemaOut(**record.__dict__) for record in hedges]
        except Exception as e:
            await log_with_bot('e', e)
            raise e

    async def create_hedge(self,spread):
        try:
            hedge_data = await self.HedgesRepository.create(spread)
            return HedgesSchemaOut(**hedge_data.__dict__)

        except Exception as e:
            await log_with_bot('e', e)
            raise e


class AlgoPLFundsRisk:
    def __init__(self):
        super().__init__()
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
            return [PLFundsRiskSchema(**record.__dict__) for record in plfundsrisks]
        except Exception as e:
            await log_with_bot('e', e)
            raise e


    async def get_plfundsrisks_all(self):
        try:
            plfundsrisks = await self.PLFundsRiskRepository.fetch_all()
            if len(plfundsrisks) == 0:
                raise DataNotFoundException(f"PLFundsRisk data not found")
            return [PLFundsRiskSchema(**record.__dict__) for record in plfundsrisks]
        except Exception as e:
            await log_with_bot('e', e)
            raise e


class AlgoPLDateSummary:
    def __init__(self):
        super().__init__()
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
            return [PLDateSummarySchema(**record.__dict__) for record in pldatesummarys]
        except Exception as e:
            await log_with_bot('e', e)
            raise e


    async def get_pldatesummarys_all(self):
            try:
                pldatesummarys= await self.PLDateSummaryRepository.fetch_all()
                if len(pldatesummarys) == 0:
                    raise DataNotFoundException(f"PLDateSummary data not found")
                return [PLDateSummarySchema(**record.__dict__) for record in pldatesummarys]
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

        entryDetails = self.algoBroker.create_order(order)
        return entryDetails
    async def exit(self,order):
        exitDetails = self.algoBroker.create_order(order)
        return exitDetails


class AlgoUser():
    def __init__(self, broker, userid):
        self.broker = broker
        self.userid = userid

    async def execute_signals(self,signallist):

        for signal in signallist:
            activeSpreads = AlgoSpread.get_spreads_data(signal)
            for spread in activeSpreads:
                print(spread)



