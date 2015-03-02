# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
import sqlalchemy as sa

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

engine = create_engine(
    "postgresql+psycopg2://postgres:root@127.0.0.1:5432/test"
)

sql = sa.select([authors.c.author, authors.c.passwd]).select_from(
    authors).where(authors.c.email == "test@root.com")

with engine.connect() as conn:
    res = conn.execute(sql)
    for raw in res:
        print(raw)

