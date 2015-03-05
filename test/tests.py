# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
import sqlalchemy as sa

from application.database import db

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
#     res = conn.execute(sql)
#     for raw in res:
#         print(raw)

sql = sa.select("1").select_from(login).where(
    login.c.id == "18c97c3598dd4dfaa5968efb888d6a3c")

get_return = db.run_with_return(sql)
print(get_return)
