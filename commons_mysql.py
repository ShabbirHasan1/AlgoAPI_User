from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from commons import *
from models import *

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://" + settings.DataBaseUser + ':' + settings.DataBasePassword + '@' + settings.MASTER_HOST + ':' + str(
    settings.MYSQL_PORT) + '/' + settings.UserDataBaseName
engine_algo_livetrades = create_engine(SQLALCHEMY_DATABASE_URL, echo=False, echo_pool=False, logging_name='sqlalchemy')


SessionLocal = sessionmaker(autocommit=False)
SessionLocal.configure(binds={SpreadsModel: engine_algo_livetrades,
                              HedgesModel: engine_algo_livetrades,
                              PLFundsRisk: engine_algo_livetrades,
                              PLDateSummary: engine_algo_livetrades})

async def get_mysql_conn_livetrades():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
