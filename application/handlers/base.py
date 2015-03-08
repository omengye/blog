import tornado.web
import tornado.websocket
import sqlalchemy as sa

from application.utils import Utils
from application import modules
from application.database import db


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
                self.set_secure_cookie(name="author", value=author, expires_days=1)
                self.render("index.html")


class EditorHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("editor.html")

    def post(self):
        html = self.get_argument("test-editormd-html-code", None)
        code = self.get_argument("test-editormd-markdown-doc", None)
        title = self.get_argument("title", None)
        tags = self.get_argument("tags", None)
        print(html)
