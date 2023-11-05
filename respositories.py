from sqlalchemy.orm import Session
from sqlalchemy import func, and_, distinct
from sqlalchemy import cast, DateTime

from models import *
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

    async def create(self, spreadsdata: SpreadsSchemaIn):
        spread_model = SpreadsModel(**spreadsdata.__dict__)
        self.db.add(spread_model)
        self.db.commit()
        self.db.refresh(spread_model)
        return spread_model

    async def update(self, spreadsdata: SpreadsSchemaOut):
        db_spreads = self.db.query(SpreadsModel).filter_by(SpreadId=spreadsdata.SpreadId).one()
        spreadsdata_dict = spreadsdata.__dict__
        for field, value in spreadsdata_dict.items():
            setattr(db_spreads, field, value)
        self.db.commit()
        self.db.refresh(db_spreads)
        return db_spreads

    async def modify(self, spreadsdata: SpreadsSchemaOut):
        self.db.merge(spreadsdata)  # This will handle both update and create operations
        self.db.commit()
        self.db.refresh(spreadsdata)
        return spreadsdata

    async def delete(self, spreadid):
        db_spreads = self.db.query(SpreadsModel).filter_by(SpreadId=spreadid).one_or_none()
        if db_spreads:
            self.db.delete(db_spreads)
            self.db.commit()
            return db_spreads

    async def fetch_all(self):
        return self.db.query(SpreadsModel).all()

    async def fetch_by_strategy(self, strategy: str):
        return self.db.query(SpreadsModel).filter_by(Strategy=strategy).all()

    async def fetch_by_strategy_status(self, strategy: str,status: str):
        return self.db.query(SpreadsModel).filter_by(Strategy=strategy,Status=status).all()

    async def fetch_by_spreadid(self, spreadid: int):
        return self.db.query(SpreadsModel).filter_by(SpreadId=spreadid).first()


class HedgesRepository:
    def __init__(self):
        self.db = None

    async def async_init(self):
        async for db in get_mysql_conn_livetrades():
            self.db = db
            return self

    def __await__(self):
        return self.async_init().__await__()

    async def create(self, hedgesdata: HedgesSchemaIn):
        hedge_model = HedgesModel(**hedgesdata.__dict__)
        self.db.add(hedge_model)
        self.db.commit()
        self.db.refresh(hedge_model)
        return hedge_model

    async def update(self, hedgesdata: HedgesSchemaOut):
        db_hedges = self.db.query(HedgesModel).filter_by(HedgeId=hedgesdata.HedgeId).one()
        hedgesdata_dict = hedgesdata.__dict__
        for field, value in hedgesdata_dict.items():
            setattr(db_hedges, field, value)
        self.db.commit()
        self.db.refresh(db_hedges)
        return db_hedges


    async def modify(self, hedgedata: HedgesSchemaOut):
        self.db.merge(hedgedata)  # This will handle both update and create operations
        self.db.commit()
        self.db.refresh(hedgedata)
        return hedgedata

    async def delete(self, hedgeid):
        db_hedges = self.db.query(HedgesModel).filter_by(HedgeId=hedgeid).one_or_none()
        if db_hedges:
            self.db.delete(db_hedges)
            self.db.commit()
            return db_hedges

    async def fetch_all(self):
        return self.db.query(HedgesModel).all()

    async def fetch_by_broker_userid(self, broker: str, user_id: str):
        return self.db.query(HedgesModel).filter_by(Broker=broker, UserId=user_id).first()

    async def fetch_by_strategy(self, strategy: str):
        return self.db.query(HedgesModel).filter_by(Strategy=strategy).all()

    async def fetch_by_strategy_status(self, strategy: str,status: str):
        return self.db.query(HedgesModel).filter_by(Strategy=strategy,Status=status).all()

    async def fetch_by_hedgeid(self, hedgeid: int):
        return self.db.query(HedgesModel).filter_by(HedgeId=hedgeid).first()


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
        db_data_summary = await self.db.query(PLDateSummaryModel).filter_by(Strategy=pldatesummarydata.Strategy,
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
        return self.db.query(PLDateSummaryModel).all()

    async def fetch_by_broker_userid(self, broker: str, user_id: str):
        return self.db.query(PLDateSummaryModel).filter_by(Broker=broker, UserId=user_id).first()

    async def fetch_by_strategy(self, strategy: str):
        return self.db.query(PLDateSummaryModel).filter_by(Strategy=strategy).all()

    async def fetch_by_date(self, date: str):
        return self.db.query(PLDateSummaryModel).filter_by(Date=date).all()


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
        db_pl_funds_risk = await self.db.query(PLFundsRiskModel).filter_by(Broker=plfundsriskdata.Broker,
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
        return self.db.query(PLFundsRiskModel).all()

    async def fetch_by_broker_userid(self, broker: str, user_id: str):
        return self.db.query(PLFundsRiskModel).filter_by(Broker=broker, UserId=user_id).first()

    async def fetch_by_strategy(self, strategy: str):
        return self.db.query(PLFundsRiskModel).filter_by(Strategy=strategy).all()

    async def fetch_by_date(self, date: str):
        return self.db.query(PLFundsRiskModel).filter(func.DATE(PLFundsRiskModel.DateTime) == date).all()

async def get_SpreadsRepository():
    return await SpreadsRepository()


async def get_HedgesRepository():
    return await HedgesRepository()


async def get_PLDateSummaryRepository():
    return await PLDateSummaryRepository()


async def get_PLFundsRiskRepository():
    return await PLFundsRiskRepository()
