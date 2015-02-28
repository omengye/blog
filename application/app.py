import os.path
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

from application.urls import urls
from application.cron import Cron

define("port", default=8000, help="run on the given port", type=int)
define("period", default=300000, help="delete qr code pic by millisecond", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            cookie_secret="test",
            template_path=os.path.join(os.path.dirname(__file__), "../templates"),
            static_path=os.path.join(os.path.dirname(__file__), "../static")
        )

        tornado.web.Application.__init__(self, urls, **settings)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    tornado.ioloop.PeriodicCallback(Cron.del_qr_cron, options.period).start()
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
