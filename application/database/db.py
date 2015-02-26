import asyncio
from aiopg.sa import create_engine

db_engine = create_engine(user='postgres',
                          database='test',
                          host='127.0.0.1',
                          password='root')


def run(sql):
    @asyncio.coroutine
    def go():
        engine = yield from db_engine

        with (yield from engine) as conn:
            yield from conn.execute(sql)

    loop_run(go())


def run_with_return(sql):
    result = []

    @asyncio.coroutine
    def go_with_return():
        engine = yield from db_engine

        with (yield from engine) as conn:
            res = yield from conn.execute(sql)
            for row in res:
                result.append(row)

    loop_run(go_with_return())
    return result


def loop_run(go):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(go())
