# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
import sqlalchemy as sa
import datetime

from application.database import db
from application.utils import Utils
from application import modules

metadata = sa.MetaData()

authors = sa.Table(
    "authors", metadata,
    sa.Column("id", sa.String(32), primary_key=True),
    sa.Column("author", sa.String(512), nullable=False),
    sa.Column("email", sa.String(512), nullable=True),
    sa.Column("passwd", sa.String(512), nullable=False)
)

tbl = sa.Table('tbl', metadata,
               sa.Column('id', sa.Integer, primary_key=True),
               sa.Column('val', sa.String(255)))

tags = sa.Table(
    "tags", metadata,
    sa.Column("id", sa.String(32), primary_key=True),
    sa.Column("tag_name", sa.String(512), nullable=True),
    sa.Column("article_id", sa.String(32), nullable=True)
)

login = sa.Table(
    "login", metadata,
    sa.Column("id", sa.String(32), primary_key=True),
    sa.Column("uid", sa.String(32), nullable=True),
    sa.Column("login_time", sa.String(19), nullable=True)
)

engine = create_engine(
    "postgresql+psycopg2://postgres:root@127.0.0.1:5432/test"
)

# sql = sa.select([authors.c.author, authors.c.passwd]).select_from(
# authors).where(authors.c.email == "test@root.com")
#
# with engine.connect() as conn:
# res = conn.execute(sql)
# for raw in res:
# print(raw)

# sql = sa.select("1").select_from(login).where(
#     login.c.id == "18c97c3598dd4dfaa5968efb888d6a3c")
#
# get_return = db.run_with_return(sql)
# print(get_return)

# time = "2015-03-05T00:21:40"
# time1 = "2015-03-05T00:22:40"
#
# [year, time] = time.split("T")
# print([year, time])
#
# t = datetime.datetime.now()
# before = t + datetime.timedelta(seconds=0)
# delay_time = before.strftime("%Y-%m-%dT%H:%M:%S")
# print(delay_time)
#
# result = Utils.interval_sec("2015-03-06T01:01:00")
# print(result)

article = modules.Articles(uuid=Utils.generate_uuid(), author_id="098f6bcd4621d373cade4e832627b4f6", title="defef",
                           markdown="", html="", publish_time=Utils.time_now(), update_time=None)

sql = modules.articles.insert().values(id=article.id, author_id=article.author_id,
                                       title=article.title, markdown=article.markdown, html=article.html,
                                       publish_time=article.publish_time)
db.run(sql)
