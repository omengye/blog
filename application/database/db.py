from sqlalchemy import create_engine

from application import modules
from application import utils

db_engine = create_engine(
    "postgresql+psycopg2://postgres:root@127.0.0.1:5432/test"
)


def commit_save_update(article_sql, article_id, tag_names):
    with db_engine.connect() as conn:
        tr = conn.begin()
        conn.execute(article_sql)
        conn.execute(modules.tags.delete().where(modules.tags.c.article_id == article_id))
        for tag_name in tag_names:
            conn.execute(modules.tags.insert().values(
                id=utils.Utils.generate_uuid(),
                tag_name=tag_name,
                article_id=article_id))
        tr.commit()


def commit_delete(article_sql, article_ids):
    with db_engine.connect() as conn:
        tr = conn.begin()
        conn.execute(article_sql)
        conn.execute(modules.tags.delete().where(modules.tags.c.article_id.in_(article_ids)))
        tr.commit()


def run(sql):
    with db_engine.connect() as conn:
        conn.execute(sql)


def run_with_return(sql):
    result = []
    with db_engine.connect() as conn:
        res = conn.execute(sql)
        for raw in res:
            result.append(raw)
    return result
