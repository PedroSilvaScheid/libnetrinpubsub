import json
import datetime

def msg_handler(channel, redis_connection):
    sub = redis_connection.pubsub()
    sub.subscribe(channel)
    while True:
        try:
            msg = sub.get_message()
            if msg:
                if msg['type'] == 'message':
                    msg_data = json.loads(msg['data'].decode('utf-8'))
                    print(msg_data)
        except Exception as Error:
            print(Error)


async def requirement_tokens_to_netrinsolver(item: Item, redis_connection):

    payload = {
        "Nome": f"{item}"
    }
    async with httpx.AsyncClient() as client:
        response = await client.post('http://127.0.0.1:8000/item', json=payload, timeout=None)

    try:
        response_json = response.json()
        status_code = str(response.status_code)
        if status_code == "200":
            timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H.%M.%S")
            hash_key = f"{timestamp}"
            redis_connection.hset(hash_key, mapping=response_json)
            redis_connection.expire(hash_key, 300)
            return response_json
        return {"message": f"Problema Na Busca{status_code}"}
    except Exception as error:
        return {"message": f"Problema Na Busca:{error}"}