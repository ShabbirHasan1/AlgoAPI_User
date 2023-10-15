import aioredis
import json
from commons_telegram import *

import datetime


async def get_redis_conn():
    try:
        redis = await aioredis.from_url("redis://" + str(settings.MASTER_HOST),
                                        username=settings.RedisUser,
                                        password=settings.RedisPassword,
                                        decode_responses=True)
        try:
            yield redis
        finally:
            await redis.close()

    except Exception as e:
        await log_with_bot('e', e)


async def get_quote_redis(symbol):
    try:
        segment, symbol = symbol.split(':')

        exchange = 'NSE'
        if segment in settings.ExchangeSegmentList_NSE:
            exchange = 'NSE'
        elif segment in settings.ExchangeSegmentList_BSE:
            exchange = 'BSE'
        elif segment in settings.ExchangeSegmentList_MCX:
            exchange = 'MCX'

        latest_tick = None
        async for redis in get_redis_conn():
            brokerList = settings.BrokerList
            for broker in brokerList:
                scriptID = await redis.hget('Master_' + broker + '_ScriptName_' + exchange, symbol.upper())
                if scriptID != 0:
                    latest_ticks = await redis.zrevrange(f'TickData_{broker}:{scriptID}', 0, 0)
                    if len(latest_ticks) > 0:
                        latest_tick = json.loads(latest_ticks[0])
                        return latest_tick

        return latest_tick

    except Exception as e:
        await log_with_bot('e', e)


async def insert_ticks_redis(broker, ticks):
    try:
        async for redis in get_redis_conn():
            pipe = redis.pipeline()
            for tick in ticks:

                if broker == 'Kotak':
                    if 'ltt' in tick:
                        timestamp = int(datetime.datetime.strptime(tick['ltt'], '%d/%m/%Y %H:%M:%S').timestamp())
                        if timestamp < int(datetime.datetime.now().timestamp()):
                            serialized_tickdata = json.dumps(tick, default=str).encode('utf-8')
                            key = f"TickData_{broker}:{tick['tk']}"
                            pipe.zadd(key, {serialized_tickdata: timestamp})
                elif broker == 'IIFL':
                    timestamp = int(datetime.datetime.strptime(tick['ltt'], '%d/%m/%Y %H:%M:%S').timestamp())
                    serialized_tickdata = json.dumps(tick, default=str).encode('utf-8')
                    key = f"TickData_{broker}:{tick['ExchangeInstrumentID']}"
                    pipe.zadd(key, {serialized_tickdata: timestamp})

                elif broker == 'Zerodha':
                    timestamp = int(tick['timestamp'].timestamp())
                    serialized_tickdata = json.dumps(tick, default=str).encode('utf-8')
                    key = f"TickData_{broker}:{tick['instrument_token']}"
                    pipe.zadd(key, {serialized_tickdata: timestamp})

            await pipe.execute()

    except Exception as e:
        await log_with_bot('e', e)


async def get_scriptid_redis(broker, segment, scriptname):
    try:
        exchange = 'NSE'
        if segment in settings.ExchangeSegmentList_NSE:
            exchange = 'NSE'
        elif segment in settings.ExchangeSegmentList_BSE:
            exchange = 'BSE'
        elif segment in settings.ExchangeSegmentList_MCX:
            exchange = 'MCX'

        async for redis in get_redis_conn():
            scriptID = await redis.hget('Master_' + broker + '_ScriptName_' + exchange, scriptname)
            return scriptID
    except Exception as e:
        await log_with_bot("e", str(e) + ' : ' + str(scriptname))
