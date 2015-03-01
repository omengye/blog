import tornado.web
import tornado.websocket
import tornado.ioloop
import qrcode
import os.path

from application.utils import Utils


class Auth(tornado.websocket.WebSocketHandler):
    code = Utils.generate_uuid()
    qrpic_time = Utils.epoch_before_sec(0)

    @staticmethod
    def generate_code():
        return Auth.code

    @staticmethod
    def gen_pic_name():
        return str(Auth.qrpic_time) + "_" + Auth.code + ".png"


class CheckPageHandler(Auth):
    def get(self):
        self.render("ws.html", code=self.generate_code(), pic_name=self.gen_pic_name())


class CheckLoginHandler(tornado.web.RequestHandler):
    def get(self, par):
        par = str(par)
        if par is not None and Utils.no_special_symbol(par) and len(par) == 32:
            self.render("check.html", code=par)
        else:
            self.redirect("http://127.0.0.1:8000/")

    def post(self, par):
        print(par)
        email = self.get_argument("email", None)
        passwd = self.get_argument("md5_pass", None)
        print(email, passwd)
        self.finish("200")



class WebSocketHandler(Auth):
    def check_origin(self, origin):
        return True

    def open(self):
        print("WebSocket opened")

        qr = qrcode.QRCode(
            version=1,
            box_size=6,
            border=1,
        )
        qr.add_data("http://192.168.1.106:8000/check/" + self.generate_code())
        qr.make(fit=True)
        img = qr.make_image()
        pic_path = os.path.join(os.path.dirname(__file__), "../../static/qrpic/") + self.gen_pic_name()
        img.save(pic_path)

    def on_message(self, message):
        print(str(message))
        if len(message) == 32:
            self.write_message(message)
            print("send message")

    def on_close(self):
        self.close()
        print("close")
