from commons_telegram import *
from respositories import *
import pandas as pd
import asyncio


class AlgoUser:
    def __init__(self,broker,userid):
        self.broker = broker
        self.userid = userid

    async def login(self):
        try:
            pass
        except Exception as e:
            await log_with_bot('e', e)

    async def get_positionBook(self):
        try:
            pass
        except Exception as e:
            await log_with_bot('e', e)

    async def get_orderBook(self):
        try:
            pass
        except Exception as e:
            await log_with_bot('e', e)

    async def get_tradeBook(self):
        try:
            pass
        except Exception as e:
            await log_with_bot('e', e)
class AlgoMaster:
    def __init__(self):
        pass

    async def get_user_data(self, broker, userid):
        try:
            masterProxy = ApiMasterProxy()
            path = '/users'
            path = path + '/' + broker + '/' + userid.upper()
            response = await masterProxy.get(path)
            return response
        except Exception as e:
            await log_with_bot('e', e)


class AlgoSpreads:
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
            spread_data = await self.SpreadsRepository.fetch_by_strategy(strategy)
            return spread_data
        except Exception as e:
            await log_with_bot('e', e)

    async def get_spreads_all(self):
        try:
            spread_data = await self.SpreadsRepository.fetch_all()
            return spread_data
        except Exception as e:
            await log_with_bot('e', e)


class AlgoHedges:
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
            hedge_data = await self.HedgesRepository.fetch_by_strategy(strategy)
            return hedge_data
        except Exception as e:
            await log_with_bot('e', e)

    async def get_hedges_all(self):
        try:
            hedge_data = await self.HedgesRepository.fetch_all()
            return hedge_data
        except Exception as e:
            await log_with_bot('e', e)


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
            plfundsrisk_data = await self.PLFundsRiskRepository.fetch_by_date(date)
            return plfundsrisk_data
        except Exception as e:
            await log_with_bot('e', e)

    async def get_plfundsrisks_all(self):
        try:
            plfundsrisk_data = await self.PLFundsRiskRepository.fetch_all()
            return plfundsrisk_data
        except Exception as e:
            await log_with_bot('e', e)


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
            pldatesummary_data = await self.PLDateSummaryRepository.fetch_by_date(date)
            return pldatesummary_data
        except Exception as e:
            await log_with_bot('e', e)

    async def get_pldatesummarys_all(self):
        try:
            pldatesummary_data = await self.PLDateSummaryRepository.fetch_all()
            return pldatesummary_data
        except Exception as e:
            await log_with_bot('e', e)


class AlgoStrategy:
    async def get_strategy_data(self, strategy):
        try:
            strategyProxy = ApiStrategyProxy()
            path = '/strategies'
            path = path + '/' + strategy.upper()
            response = await strategyProxy.get(path)
            return response
        except Exception as e:
            await log_with_bot('e', e)


class AlgoData:
    def __init__(self):
        pass

    async def get_quote_live(self, symbol):
        try:
            dataProxy = ApiDataProxy()
            path = '/quotes/live'
            path = path + '/' + symbol.upper()
            response = await dataProxy.get(path)
            return response
        except Exception as e:
            await log_with_bot('e', e)

    async def get_quote_list(self, symbols):
        try:
            dataProxy = ApiDataProxy()
            path = '/quotes/list'
            path = path + '/' + symbols.upper()
            response = await dataProxy.get(path)
            return response
        except Exception as e:
            await log_with_bot('e', e)

    async def get_quote_ohlc(self, timeframe, symbol):
        try:
            dataProxy = ApiDataProxy()
            path = '/quotes/ohlc'
            path = path + '/' + timeframe + '/' + symbol.upper()
            response = await dataProxy.get(path)
            return response
        except Exception as e:
            await log_with_bot('e', e)


class AlgoBroker:
    def __init__(self, broker):
        self.broker = broker

    async def get_quote_live(self, symbol):
        try:
            brokerProxy = ApiBrokerProxy(self.broker)
            path = '/quotes/live'
            path = path + '/' + symbol.upper()
            response = await brokerProxy.get(path)
            return response
        except Exception as e:
            await log_with_bot('e', e)

    async def get_quote_list(self, symbols):
        try:
            brokerProxy = ApiBrokerProxy(self.broker)
            path = '/quotes/list'
            path = path + '/' + symbols.upper()
            response = await brokerProxy.get(path)
            return response
        except Exception as e:
            await log_with_bot('e', e)

    async def get_quote_ohlc(self, timeframe, symbol):
        try:
            brokerProxy = ApiBrokerProxy(self.broker)
            path = '/quotes/ohlc'
            path = path + '/' + timeframe + '/' + symbol.upper()
            response = await brokerProxy.get(path)
            return response
        except Exception as e:
            await log_with_bot('e', e)
