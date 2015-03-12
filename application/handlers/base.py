import tornado.web
import tornado.websocket
import sqlalchemy as sa

from application.utils import Utils
from application import modules
from application.database import db, service


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        uid = self.get_argument("uid", None)
        token = self.get_argument("token", None)
        if uid is None or token is None or len(uid) != 32 or len(token) != 32:
            self.render("index.html")
        else:
            sql = sa.select([modules.login.c.login_time]).select_from(modules.login).where(
                modules.login.c.id == str(token))
            login_time = db.run_with_return(sql)
            sql1 = sa.select([modules.authors.c.author]).select_from(modules.authors).where(
                modules.authors.c.id == str(uid))
            author = db.run_with_return(sql1)
            if not login_time or not author:
                self.write("token or user error")
            elif Utils.interval_sec(login_time[0][0]) >= 10:
                self.write("token lose efficacy")
            else:
                author = author[0][0]
                login_time = login_time[0][0]
                print(author, login_time)
                author_uid = author + "." + uid
                self.set_secure_cookie(name="author", value=author_uid, expires_days=1)
                self.render("index.html")


class EditorHandler(tornado.web.RequestHandler):
    def get(self):
        article_id = self.get_argument("article_id", None)
        article = None
        tags = ""
        if article_id is None:
            self.render("editor.html", article=article, tags=tags)
        elif Utils.no_special_symbol(article_id) is False or len(article_id) != 32:
            self.write("404")
        else:
            get_return = []
            sql = sa.select("*").select_from(modules.articles).where(modules.articles.c.id == str(article_id))
            try:
                get_return = db.run_with_return(sql)
            except IOError:
                print("get article error")
            if get_return:
                article = modules.Articles(uuid=get_return[0][0], author_id=get_return[0][1], title=get_return[0][2],
                                           markdown=get_return[0][3], html=get_return[0][4],
                                           publish_time=get_return[0][5], update_time=get_return[0][6])
                tags_sql = sa.select([modules.tags.c.tag_name]).select_from(modules.tags).where(
                    modules.tags.c.article_id == article.id)
                get_tags = None
                try:
                    get_tags = db.run_with_return(tags_sql)
                except IOError:
                    print("get tags error")
                if get_tags:
                    for tag in get_tags:
                        tags = tags + tag[0] + ","
                    self.render("editor.html", article=article, tags=tags)
            else:
                self.write("404")

    def post(self):
        html = self.get_argument("test-editormd-html-code", "")
        code = self.get_argument("test-editormd-markdown-doc", "")
        title = self.get_argument("title", None)
        tags = self.get_argument("tags", None)
        article_id = self.get_argument("article_id", None)
        publish_time = self.get_argument("publish_time", None)
        author_bytes = self.get_secure_cookie("author")
        if title is None:
            self.write("title input error")
        elif author_bytes is None:
            self.write("login error")
        author_uid = author_bytes.decode("utf-8")
        uid = author_uid.split(".")[1]

        article = None

        # save article
        if article_id is None and publish_time is None:
            article = modules.Articles(uuid=None, author_id=uid, title=title, markdown=code, html=html,
                                       publish_time=None, update_time=None)
        # update article
        elif article_id is not None and publish_time is not None:
            article = modules.Articles(uuid=article_id, author_id=uid, title=title, markdown=code, html=html,
                                       publish_time=publish_time, update_time=None)

        tag_list = []
        if tags is not None:
            tag_list = tags.split(",")

        if article is not None:
            service.save_or_update(article, tag_list)

