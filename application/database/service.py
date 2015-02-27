from blog.application import modules
from blog.application import utils
from blog.application.database import db


def delete_by_ids(article_ids):
    try:
        if type(article_ids) is list and utils.Utils.not_empty(article_ids[0]):
            sql = modules.articles.delete().where(modules.articles.c.id.in_(article_ids))
            db.commit_delete(sql, article_ids)
    except IOError:
        print("delete ids is error")


def save_or_update(clazz, tag_names):
    try:
        sql = ""
        article_id = ""
        if clazz.__class__.__name__ == "Articles":
            # update article
            if utils.Utils.not_empty(clazz.id):
                sql = modules.articles.update().values(author_id=clazz.author_id, title=clazz.title,
                                                       markdown=clazz.markdown, html=clazz.html,
                                                       update_time=utils.Utils.time_now()).where(
                    modules.articles.c.id == clazz.id)
                article_id = clazz.id
            # save article
            else:
                article_id = utils.Utils.generate_uuid()
                sql = modules.articles.insert().values(id=article_id, author_id=clazz.author_id,
                                                       title=clazz.title, markdown=clazz.markdown, html=clazz.html,
                                                       publish_time=utils.Utils.time_now())

        db.commit_save_update(sql, article_id, tag_names)
    except IOError:
        print("{} save or update is error".format(clazz.__class__.__name__))

