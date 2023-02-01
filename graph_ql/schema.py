import asyncio
import datetime
import graphene
import reactivex as rx
import reactivex.operators as ops
from reactivex.subject import BehaviorSubject
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
channel_layer = get_channel_layer()

class Query(graphene.ObjectType):
    test = graphene.String(name=graphene.String())

    def resolve_test(root, info, name):
       async_to_sync(channel_layer.group_send)("new_message", {"data": name})

class Mutatation(graphene.ObjectType):
     test_object = graphene.String()

class Subscription(graphene.ObjectType):
    test = graphene.String()
    test1 = graphene.String()

    async def subscribe_test1(root, info):
        channel_name = await channel_layer.new_channel()
        await channel_layer.group_add("new_message", channel_name)
        try:
            while True:
                message = await channel_layer.receive(channel_name)
                yield message["data"]
        finally:
            await channel_layer.group_discard("new_message", channel_name)

    async def subscribe_test(root, info):
        while True:
            yield datetime.datetime.now().isoformat()
            await asyncio.sleep(1)

schema = graphene.Schema(query=Query, mutation=Mutatation, subscription=Subscription)