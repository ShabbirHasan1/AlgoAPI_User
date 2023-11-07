from pydantic_settings import BaseSettings
from typing import Optional
from dotenv import load_dotenv
import os
import datetime

load_dotenv()


class Settings(BaseSettings):
    MYSQL_PORT: int = os.environ.get('MYSQL_PORT')
    REDIS_PORT: int = os.environ.get('REDIS_PORT')
    KAFKA_PORT: int = os.environ.get('KAFKA_PORT')
    API_HOST: str = os.environ.get('API_HOST')
    API_PORT: int = os.environ.get('API_PORT')
    API_WORKERS: int = os.environ.get('API_WORKERS')
    API_WORKERS: int = 2
    API_MASTER_PORT: int = os.environ.get('API_MASTER_PORT')
    API_DATA_PORT: int = os.environ.get('API_DATA_PORT')
    API_STRATEGY_PORT: int = os.environ.get('API_STRATEGY_PORT')
    API_USER_PORT: int = os.environ.get('API_USER_PORT')
    API_ZERODHA_PORT: int = os.environ.get('API_ZERODHA_PORT')
    API_IIFL_PORT: int = os.environ.get('API_IIFL_PORT')
    API_KOTAKNEO_PORT: int = os.environ.get('API_KOTAKNEO_PORT')
    API_FYERS_PORT: int = os.environ.get('API_FYERS_PORT')
    MASTER_HOST: str = os.environ.get('MASTER_HOST')
    DataBaseName: str = os.environ.get('DataBaseName')
    DataBaseUser: str = os.environ.get('DataBaseUser')
    DataBasePassword: str = os.environ.get('DataBasePassword')
    RedisUser: str = os.environ.get('RedisUser')
    RedisPassword: str = os.environ.get('RedisPassword')
    ApiUser: str = os.environ.get('ApiUser')
    ApiPassword: str = os.environ.get('ApiPassword')
    DataBroker: str = os.environ.get('DataBroker')
    DataUserId: str = os.environ.get('DataUserId')
    Broker: str = os.environ.get('Broker')
    UserId: str = os.environ.get('UserId')
    InstanceId: str = os.environ.get('InstanceId')
    TZ: str = os.environ.get('TZ')
    TelegramBotToken: str = os.environ.get('TelegramBotToken')
    TelegramChatId: str = os.environ.get('TelegramChatId')
    TelegramBot: Optional[str] = None
    logger: Optional[str] = None
    UserDataBaseName: str = str(DataBaseName) + '_' + str(Broker.lower()) + '_' + str(UserId.lower())
    KAFKA_URL: str = str(MASTER_HOST) + ':' + str(KAFKA_PORT)
    MYSQL_URL: str = str(MASTER_HOST) + ':' + str(MYSQL_PORT)
    REDIS_URL: str = str(MASTER_HOST) + ':' + str(REDIS_PORT)
    API_MASTER_URL: str = str(MASTER_HOST) + ':' + str(API_MASTER_PORT)
    API_STRATEGY_URL: str = str(MASTER_HOST) + ':' + str(API_STRATEGY_PORT)
    API_DATA_URL: str = str(MASTER_HOST) + ':' + str(API_DATA_PORT)
    API_USER_URL: str = str(MASTER_HOST) + ':' + str(API_USER_PORT)
    API_ZERODHA_URL: str = str(MASTER_HOST) + ':' + str(API_ZERODHA_PORT)
    API_IIFL_URL: str = str(MASTER_HOST) + ':' + str(API_IIFL_PORT)
    API_FYERS_URL: str = str(MASTER_HOST) + ':' + str(API_FYERS_PORT)
    API_KOTAKNEO_URL: str = str(MASTER_HOST) + ':' + str(API_KOTAKNEO_PORT)
    kafka_producer: Optional[str] = None
    kafka_consumer: Optional[str] = None
    redis_conn: Optional[str] = None
    mysql_conn: Optional[str] = None
    BrokerList: list = ['Zerodha', 'IIFL', 'Kotak']
    EquitySegmentList_NSE: list = ['NSE', 'NSECM', 'nse_cm']
    EquitySegmentList_BSE: list = ['BSE', 'BSECM', 'bse_cm']
    DerivativesSegmentList_NSE: list = ['NFO', 'NSEFO', 'nse_fo']
    DerivativesSegmentList_BSE: list = ['BFO', 'BSEFO', 'bse_fo']
    CurrencySegmentList_NSE: list = ['CDS', 'NSECD', 'cde_fo']
    CurrencySegmentList_BSE: list = ['BCD', 'BSECD', 'bcs_fo']
    CommoditySegmentList_MCX: list = ['MCX', 'MCXFO', 'mcx_fo']
    ExchangeSegmentList_NSE: list = EquitySegmentList_NSE + DerivativesSegmentList_NSE + CurrencySegmentList_NSE
    ExchangeSegmentList_BSE: list = EquitySegmentList_BSE + DerivativesSegmentList_BSE + CurrencySegmentList_BSE
    ExchangeSegmentList_MCX: list = CommoditySegmentList_MCX
    MarketOpenTime: datetime.datetime = datetime.datetime.now().replace(hour=9, minute=15, second=0, microsecond=0)
    MarketExitTime: datetime.datetime = datetime.datetime.now().replace(hour=15, minute=15, second=0, microsecond=0)
    MarketCloseTime: datetime.datetime = datetime.datetime.now().replace(hour=15, minute=30, second=0, microsecond=0)

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
