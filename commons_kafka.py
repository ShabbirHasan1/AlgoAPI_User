from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import json
from commons_telegram import *


async def initialize_kafka():
    try:
        settings.kafka_producer = await create_producer()
        await settings.kafka_producer.start()

        settings.kafka_consumer = await create_consumer('Group_Events_API')
        await settings.kafka_consumer.start()

    except Exception as e:
        await log_with_bot('e', e)


async def create_producer():
    try:
        return AIOKafkaProducer(bootstrap_servers=settings.KAFKA_URL,
                                key_serializer=lambda v: json.dumps(v, default=str).encode('utf-8'),
                                value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')
                                )
    except Exception as e:
        await log_with_bot('e', e)


async def create_consumer(consumerGroupId='defualt-group'):
    try:
        consumerGroupId = consumerGroupId + '_' + settings.InstanceId + '_' + str(os.getpid())

        return AIOKafkaConsumer("Events",
                                bootstrap_servers=settings.KAFKA_URL,
                                auto_offset_reset='earliest',
                                enable_auto_commit=True,
                                group_id=consumerGroupId,
                                key_deserializer=lambda v: json.loads(v.decode('utf-8')),
                                value_deserializer=lambda v: json.loads(v.decode('utf-8'))
                                )
    except Exception as e:
        await log_with_bot('e', e)


async def consume_messages_kafka():
    try:
        async for msg in settings.kafka_consumer:
            await log_with_bot('i', f"Kafka - {SystemDateTime()} : {msg.value}")
    except Exception as e:
        await log_with_bot('e', e)

    finally:
        await settings.kafka_consumer.stop()


async def consume_messages_last_n(n):
    try:
        msgs = []
        # Get the latest offset for the topic
        partitions = set(settings.kafka_consumer.assignment())  # Convert frozenset to set
        await settings.kafka_consumer.seek_to_end(*partitions)
        end_offsets = await settings.kafka_consumer.end_offsets(partitions)

        # Calculate the starting offset for consuming
        start_offset = max(0, end_offsets[partitions.pop()] - n)  # Use pop to get an element from set

        # Seek to the starting offset
        settings.kafka_consumer.seek(partitions.pop(), start_offset)  # Use pop to get an element from set

        # Consume messages
        async for msg in settings.kafka_consumer:
            msgs.append(msg)

        return msgs

    except Exception as e:
        await log_with_bot('e', e)

    finally:
        await settings.kafka_consumer.stop()
