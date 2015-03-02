import asyncio
from aiopg.sa import create_engine

from application import modules
from application import utils

db_engine = create_engine(user='postgres',
                          database='test',
                          host='127.0.0.1',
                          password='root')


def commit_save_update(article_sql, article_id, tag_names):
    @asyncio.coroutine
    def go():
        engine = yield from db_engine

        with (yield from engine) as conn:
            tr = yield from conn.begin()
            yield from conn.execute(article_sql)
            yield from conn.execute(modules.tags.delete().where(modules.tags.c.article_id == article_id))
            for tag_name in tag_names:
                yield from conn.execute(modules.tags.insert().values(
                    id=utils.Utils.generate_uuid(),
                    tag_name=tag_name,
                    article_id=article_id))
            yield from tr.commit()

    loop_run(go)


def commit_delete(article_sql, article_ids):
    @asyncio.coroutine
    def go_delete():
        engine = yield from db_engine

        with (yield from engine) as conn:
            tr = yield from conn.begin()
            yield from conn.execute(article_sql)
            yield from conn.execute(modules.tags.delete().where(modules.tags.c.article_id.in_(article_ids)))
            yield from tr.commit()

    loop_run(go_delete)


def run(sql):
    @asyncio.coroutine
    def go():
        engine = yield from db_engine

        with (yield from engine) as conn:
            yield from conn.execute(sql)

    loop_run(go)


def run_with_return(sql):
    result = []

    @asyncio.coroutine
    def go_with_return():
        engine = yield from db_engine

        with (yield from engine) as conn:
            res = yield from conn.execute(sql)
            result.extend(res)

    loop_run(go_with_return)
    return result


def loop_run(go):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(go())
