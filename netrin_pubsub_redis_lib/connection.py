from redis import  Redis


def connection(host, port, db):
    redis_connection = Redis(host=host, port=port, db=db)
    return redis_connection
