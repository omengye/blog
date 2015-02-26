import asyncio
from aiopg.sa import create_engine


@asyncio.coroutine
def create_tables(engine):
    with (yield from engine) as conn:
        yield from conn.execute('DROP TABLE IF EXISTS articles')
        yield from conn.execute('DROP TABLE IF EXISTS authors')
        yield from conn.execute('DROP TABLE IF EXISTS tags')
        yield from conn.execute('''CREATE TABLE articles (
                                    id VARCHAR(32) PRIMARY KEY,
                                    author_id VARCHAR(32),
                                    title VARCHAR(512),
                                    markdown TEXT,
                                    html TEXT,
                                    publish_time VARCHAR(19),
                                    update_time VARCHAR(19))''')
        yield from conn.execute('''CREATE TABLE authors (
                                    id VARCHAR(32) PRIMARY KEY,
                                    author VARCHAR(512),
                                    email VARCHAR(512),
                                    passwd VARCHAR(512))''')
        yield from conn.execute('''CREATE TABLE tags (
                                    id VARCHAR(32) PRIMARY KEY,
                                    tag_name VARCHAR(512),
                                    article_id VARCHAR(32))''')


@asyncio.coroutine
def go():
    engine = yield from create_engine(user='postgres',
                                      database='test',
                                      host='127.0.0.1',
                                      password='root')

    yield from create_tables(engine)

loop = asyncio.get_event_loop()
loop.run_until_complete(go())
