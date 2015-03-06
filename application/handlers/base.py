import tornado.web
import tornado.websocket


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        uid = self.get_argument("uid", None)
        token = self.get_argument("token", None)
        if uid is None or token is None:
            self.render("index.html")
        else:

            print(uid, token)
