import secrets
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse
import logging
import logging.config
import inspect
import aiohttp

from config import *

# Add a basic HTTP authentication
security = HTTPBasic()


class DataNotFoundException(Exception):
    pass


# Custom exception handler
def exception_handler(e):
    if isinstance(e, DataNotFoundException):
        status_code = 404
        code = 'data-not-found'
    else:
        status_code = 500
        code = 'internal-server-error'

    return JSONResponse(
        status_code=status_code,
        content={"status": 'error', "code": code, "description": str(e), "data": []}
    )


def SystemDateTime():
    return datetime.datetime.now()


def symbol_price_round(n):
    # Smaller multiple
    a = (n // 0.05) * 0.05
    # Larger multiple
    b = a + 0.05
    # Return of closest of two
    return round((b if n - a > b - n else a), 2)


def get_calling_function_name():
    frame = inspect.currentframe().f_back
    previous_frame = frame.f_back
    calling_function_name = previous_frame.f_code.co_name
    return calling_function_name


def initialize_logger():
    logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
    settings.logger = logging.getLogger(__name__)


def initialize_settings():
    settings.KAFKA_URL = str(settings.MASTER_HOST) + ':' + str(settings.KAFKA_PORT)
    settings.MYSQL_URL = str(settings.MASTER_HOST) + ':' + str(settings.MYSQL_PORT)
    settings.REDIS_URL = str(settings.MASTER_HOST) + ':' + str(settings.REDIS_PORT)


def is_running_in_docker():
    """Check if code is running inside a Docker container."""
    # Check if the /proc/self/cgroup file exists
    return os.path.exists('/proc/self/cgroup')


def convert_epoch_to_datetime(epoch):
    base = datetime.datetime(1980, 1, 1)  # start of your epoch
    tm = base + datetime.timedelta(seconds=epoch)  # add on a number of seconds
    return tm


def log(level, message):
    UserId = 'ALGO'
    # UserId = str(settings.DataUserId)
    # func_name = get_calling_function_name()
    message = str(UserId) + ' : ' + str(message)

    if level == 'i':
        settings.logger.info(message)
    if level == 'e':
        settings.logger.error(message)
    if level == 'c':
        settings.logger.critical(message)
    if level == 'w':
        settings.logger.warning(message)


def validate_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    # encode the credentials to compare
    input_user_name = credentials.username.encode("utf-8")
    input_password = credentials.password.encode("utf-8")

    correct_username_bytes = settings.ApiUser.encode("utf-8")
    current_password_bytes = settings.ApiPassword.encode("utf-8")

    is_username = secrets.compare_digest(input_user_name, correct_username_bytes)
    is_password = secrets.compare_digest(input_password, current_password_bytes)

    if not (is_username and is_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials",
                            headers={"WWW-Authenticate": "Basic"})

    return credentials.username


class ApiMasterProxy:
    def __init__(self):
        self.base_url = 'http://' + settings.API_MASTER_URL
        self.users_url = '/users'

    async def get(self, path, params=None):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}{path}"
            async with session.get(url, params=params) as response:
                return await response.json()


class ApiDataProxy:
    def __init__(self):
        self.base_url = 'http://' + settings.API_DATA_URL
        self.quotes_url = '/quotes'

    async def get(self, path, params=None):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}{path}"
            async with session.get(url, params=params) as response:
                return await response.json()


class ApiBrokerProxy:
    def __init__(self, broker):
        if broker == 'Zerodha':
            self.base_url = 'http://' + settings.API_ZERODHA_URL
        elif broker == 'Kotak':
            self.base_url = 'http://' + settings.API_KOTAKNEO_URL
        elif broker == 'IIFL':
            self.base_url = 'http://' + settings.API_IIFL_URL
        elif broker == 'Fyers':
            self.base_url = 'http://' + settings.API_FYERS_URL
        elif broker == 'Finvasia':
            self.base_url = 'http://' + settings.API_FINVASIA_URL
        else:
            self.base_url = None

        self.funds_url = '/funds'
        self.quotes_url = '/quotes'

    async def get(self, path, params=None):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}{path}"
            async with session.get(url, params=params) as response:
                return await response.json()

    async def post(self, path, data=None, json=None):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}{path}"
            async with session.post(url, data=data, json=json) as response:
                return await response.json()

    async def put(self, path, data=None, json=None):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}{path}"
            async with session.put(url, data=data, json=json) as response:
                return await response.json()

    async def delete(self, path, params=None):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}{path}"
            async with session.delete(url, params=params) as response:
                return await response.json()


class ApiStrategyProxy:
    def __init__(self):
        self.base_url = 'http://' + settings.API_STRATEGY_URL

    async def get(self, path, params=None):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}{path}"
            async with session.get(url, params=params) as response:
                return await response.json()

    async def post(self, path, data=None, json=None):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}{path}"
            async with session.post(url, data=data, json=json) as response:
                return await response.json()

    async def put(self, path, data=None, json=None):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}{path}"
            async with session.put(url, data=data, json=json) as response:
                return await response.json()

    async def delete(self, path, params=None):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}{path}"
            async with session.delete(url, params=params) as response:
                return await response.json()


class ApiUserProxy:
    def __init__(self):
        self.base_url = 'http://' + settings.API_USER_URL

    async def post(self, path, data=None, json=None):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}{path}"
            async with session.post(url, data=data, json=json) as response:
                return await response.json()





class AlgoData:
    def __init__(self):
        pass

    async def get_quote_live(self, symbol):
        dataProxy = ApiDataProxy()
        path = '/quotes/live'
        path = path + '/' + symbol.upper()
        response = await dataProxy.get(path)
        return response

    async def get_quote_list(self, symbols):
        dataProxy = ApiDataProxy()
        path = '/quotes/list'
        path = path + '/' + symbols.upper()
        response = await dataProxy.get(path)
        return response

    async def get_quote_ohlc(self, timeframe, symbol):
        dataProxy = ApiDataProxy()
        path = '/quotes/ohlc'
        path = path + '/' + timeframe + '/' + symbol.upper()
        response = await dataProxy.get(path)
        return response


class AlgoBroker:
    def __init__(self, broker,userid):
        self.broker = broker
        self.userid = userid

    async def get_quote_live(self, symbol):
        brokerProxy = ApiDataProxy()
        path = '/quotes/live'
        path = path + '/' + symbol.upper()
        response = await brokerProxy.get(path)
        return response

    async def get_quote_list(self, symbols):
        brokerProxy = ApiDataProxy()
        path = '/quotes/list'
        path = path + '/' + symbols.upper()
        response = await brokerProxy.get(path)
        return response

    async def get_quote_ohlc(self, timeframe, symbol):
        brokerProxy = ApiDataProxy()
        path = '/quotes/ohlc'
        path = path + '/' + timeframe + '/' + symbol.upper()
        response = await brokerProxy.get(path)
        return response

    async def create_order(self, order):
        brokerProxy = ApiBrokerProxy(self.broker)
        path = '/orders/createorder'
        path = path + '/' + self.broker + '/' + self.userid
        response = await brokerProxy.post(path,json=order)
        return response

    async def cancel_order(self, order):
        brokerProxy = ApiBrokerProxy(self.broker)
        path = '/orders/cancelorder'
        path = path + '/' + self.broker + '/' + self.userid
        response = await brokerProxy.post(path,json=order)
        return response

    async def modify_order(self, order):
        brokerProxy = ApiBrokerProxy(self.broker)
        path = '/orders/modifyorder'
        path = path + '/' + self.broker + '/' + self.userid
        response = await brokerProxy.post(path,json=order)
        return response

    async def get_funds_data(self):
        brokerProxy = ApiBrokerProxy(self.broker)
        path = '/funds'
        path = path + '/' + self.broker + '/' + self.userid
        response = await brokerProxy.get(path)
        return response


class AlgoStrategy:
    def __init__(self):
        pass

    async def get_strategies(self):
        dataProxy = ApiStrategyProxy()
        path = '/strategies'
        response = await dataProxy.get(path)
        return response

    async def get_strategy_data(self, strategy):
        dataProxy = ApiStrategyProxy()
        path = '/strategies'
        path = path + '/' + strategy.upper()
        response = await dataProxy.get(path)
        return response

    async def get_strategy_users(self, strategy):
        dataProxy = ApiStrategyProxy()
        path = '/strategies/users'
        path = path + '/' + strategy.upper()
        response = await dataProxy.get(path)
        return response


class AlgoMaster:
    def __init__(self):
        pass

    async def get_user_data(self, broker, userid):
        masterProxy = ApiMasterProxy()
        path = '/users'
        path = path + '/' + broker + '/' + userid.upper()
        response = await masterProxy.get(path)
        return response

    async def get_user_data_usertype(self, broker, userid, usertype):
        masterProxy = ApiMasterProxy()
        path = '/users/usertype'
        path = path + '/' + broker + '/' + userid.upper() + '/' + usertype
        response = await masterProxy.get(path)
        return response

    async def get_access_token_data(self, broker, userid):
        masterProxy = ApiMasterProxy()
        path = '/users/accesstokendata'
        path = path + '/' + broker + '/' + userid.upper()
        response = await masterProxy.get(path)
        return response

    async def get_data_token_data(self, broker, userid):
        masterProxy = ApiMasterProxy()
        path = '/users/datatokendata'
        path = path + '/' + broker + '/' + userid.upper()
        response = await masterProxy.get(path)
        return response

    async def get_access_token(self, broker, userid):
        masterProxy = ApiMasterProxy()
        path = '/users/accesstoken'
        path = path + '/' + broker + '/' + userid.upper()
        response = await masterProxy.get(path)
        return response

    async def get_data_token(self, broker, userid):
        masterProxy = ApiMasterProxy()
        path = '/users/datatoken'
        path = path + '/' + broker + '/' + userid.upper()
        response = await masterProxy.get(path)
        return response
