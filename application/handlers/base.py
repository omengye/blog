import tornado.web
import tornado.websocket


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
