from sqlalchemy.orm import Session
from sqlalchemy import func, and_, distinct
from sqlalchemy import cast, DateTime

from schemas import *

from commons_mysql import *


class SpreadsRepository:
    def __init__(self):
        self.db = None

    async def async_init(self):
        async for db in get_mysql_conn_livetrades():
            self.db = db
            return self

    def __await__(self):
        return self.async_init().__await__()

    async def create(self, spreadsdata: SpreadsSchema):
        self.db.add(spreadsdata)
        self.db.commit()
        self.db.refresh(spreadsdata)
        return spreadsdata

    async def update(self, spreadsdata: SpreadsSchema):
        db_spreads = await self.db.query(Spreads).filter_by(TradeId=spreadsdata.TradeId).one()
        for field, value in spreadsdata.items():
            setattr(spreadsdata, field, value)
        self.db.commit()
        self.db.refresh(db_spreads)
        return db_spreads

    async def modify(self, spreadsdata: SpreadsSchema):
        self.db.merge(spreadsdata)  # This will handle both update and create operations
        self.db.commit()
        self.db.refresh(spreadsdata)
        return spreadsdata

    async def fetch_all(self):
        return self.db.query(Spreads).all()

    async def fetch_by_strategy(self, strategy: str):
        return self.db.query(Spreads).filter_by(Strategy=strategy).all()

    async def fetch_by_tradeid(self, tradeid: int):
        return self.db.query(Spreads).filter_by(TradeId=tradeid).first()


class HedgesRepository:
    def __init__(self):
        self.db = None

    async def async_init(self):
        async for db in get_mysql_conn_livetrades():
            self.db = db
            return self

    def __await__(self):
        return self.async_init().__await__()

    async def create(self, hedgesdata: HedgesSchema):
        self.db.add(hedgesdata)
        self.db.commit()
        self.db.refresh(hedgesdata)
        return hedgesdata

    async def update(self, hedgesdata: HedgesSchema):
        db_hedges = await self.db.query(Hedges).filter_by(TradeId=hedgesdata.TradeId).one()
        for field, value in hedgesdata.items():
            setattr(hedgesdata, field, value)
        self.db.commit()
        self.db.refresh(db_hedges)
        return db_hedges

    async def modify(self, hedgedata: HedgesSchema):
        self.db.merge(hedgedata)  # This will handle both update and create operations
        self.db.commit()
        self.db.refresh(hedgedata)
        return hedgedata

    async def fetch_all(self):
        return self.db.query(Hedges).all()

    async def fetch_by_broker_userid(self, broker: str, user_id: str):
        return self.db.query(Hedges).filter_by(Broker=broker, UserId=user_id).first()

    async def fetch_by_strategy(self, strategy: str):
        return self.db.query(Hedges).filter_by(Strategy=strategy).all()

    async def fetch_by_tradeid(self, tradeid: int):
        return self.db.query(Hedges).filter_by(TradeId=tradeid).first()


class PLDateSummaryRepository:
    def __init__(self):
        self.db = None

    async def async_init(self):
        async for db in get_mysql_conn_livetrades():
            self.db = db
            return self

    def __await__(self):
        return self.async_init().__await__()

    async def create(self, pldatesummarydata: PLDateSummarySchema):
        self.db.add(pldatesummarydata)
        self.db.commit()
        self.db.refresh(pldatesummarydata)
        return pldatesummarydata

    async def update(self, pldatesummarydata: PLDateSummarySchema):
        db_data_summary = await self.db.query(PLDateSummary).filter_by(Strategy=pldatesummarydata.Strategy,
                                                                       Broker=pldatesummarydata.Broker,
                                                                       UserId=pldatesummarydata.UserId).one()
        for field, value in pldatesummarydata.items():
            setattr(pldatesummarydata, field, value)
        self.db.commit()
        self.db.refresh(db_data_summary)
        return db_data_summary

    async def modify(self, pldatesummarydata: PLDateSummarySchema):
        self.db.merge(pldatesummarydata)  # This will handle both update and create operations
        self.db.commit()
        self.db.refresh(pldatesummarydata)
        return pldatesummarydata

    async def fetch_all(self):
        return self.db.query(PLDateSummary).all()

    async def fetch_by_broker_userid(self, broker: str, user_id: str):
        return self.db.query(PLDateSummary).filter_by(Broker=broker, UserId=user_id).first()

    async def fetch_by_strategy(self, strategy: str):
        return self.db.query(PLDateSummary).filter_by(Strategy=strategy).all()

    async def fetch_by_date(self, date: str):
        return self.db.query(PLDateSummary).filter_by(Date=date).all()


class PLFundsRiskRepository:
    def __init__(self):
        self.db = None

    async def async_init(self):
        async for db in get_mysql_conn_livetrades():
            self.db = db
            return self

    def __await__(self):
        return self.async_init().__await__()

    async def create(self, plfundsriskdata: PLFundsRiskSchema):
        self.db.add(plfundsriskdata)
        self.db.commit()
        self.db.refresh(plfundsriskdata)
        return plfundsriskdata

    async def update(self, plfundsriskdata: PLFundsRiskSchema):
        db_pl_funds_risk = await self.db.query(PLFundsRisk).filter_by(Broker=plfundsriskdata.Broker,
                                                                      UserId=plfundsriskdata.UserId).one()
        for field, value in plfundsriskdata.items():
            setattr(plfundsriskdata, field, value)
        self.db.commit()
        self.db.refresh(db_pl_funds_risk)
        return db_pl_funds_risk

    async def modify(self, plfundsriskdata: PLFundsRiskSchema):
        self.db.merge(plfundsriskdata)  # This will handle both update and create operations
        self.db.commit()
        self.db.refresh(plfundsriskdata)
        return plfundsriskdata

    async def fetch_all(self):
        return self.db.query(PLFundsRisk).all()

    async def fetch_by_broker_userid(self, broker: str, user_id: str):
        return self.db.query(PLFundsRisk).filter_by(Broker=broker, UserId=user_id).first()

    async def fetch_by_strategy(self, strategy: str):
        return self.db.query(PLFundsRisk).filter_by(Strategy=strategy).all()

    async def fetch_by_date(self, date: str):
        return self.db.query(PLFundsRisk).filter(func.DATE(PLFundsRisk.DateTime) == date).all()

async def get_SpreadsRepository():
    return await SpreadsRepository()


async def get_HedgesRepository():
    return await HedgesRepository()


async def get_PLDateSummaryRepository():
    return await PLDateSummaryRepository()


async def get_PLFundsRiskRepository():
    return await PLFundsRiskRepository()
