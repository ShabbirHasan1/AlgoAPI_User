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

async def get_scriptid_redis(broker, segment, scriptname):
    try:
        scriptID = None
        async for redis in get_redis_conn():
            scriptID = await redis.hget('Master_' + broker + '_ScriptName_' + segment, scriptname)
        return scriptID
    except Exception as e:
        await log_with_bot("e", str(e) + ' : ' + str(scriptname))

async def get_quote_redis(symbol):
    try:
        segment, symbol = symbol.split(':')

        latest_tick = None
        async for redis in get_redis_conn():
            brokerList = settings.BrokerList
            for broker in brokerList:
                scriptID = await get_scriptid_redis(broker, segment, symbol.upper())
                if scriptID is None:
                    scriptID = 0

                if scriptID != 0:
                    latest_ticks = await redis.zrevrange(f'TickData_{broker}:{scriptID}', 0, 0)
                    if len(latest_ticks) > 0:
                        latest_tick = json.loads(latest_ticks[0])
                        return latest_tick

        return latest_tick

    except Exception as e:
        await log_with_bot('e', e)




