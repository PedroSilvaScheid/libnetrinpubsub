from json import dumps

from redis_om import HashModel

def publish_item_to_pubsub(item, redis_connection):
    try:
        message = dumps(dict(item))
        message = str(message)
        data = redis_connection.publish('my_pubsub_channel', message)
        return data
    except Exception as Error:
        print(Error)

class Item(HashModel):
    Nome: str
    Url: str
    Key: str
    Priority: str

async def create_item(item: Item):
    try:
        item = item.dict()
        publish_item_to_pubsub(item)
    except Exception as Error:
        print(Error)
    return item