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
        qr.add_data(self.generate_code())
        qr.make(fit=True)
        img = qr.make_image()
        pic_path = os.path.join(os.path.dirname(__file__), "../../static/qrpic/") + self.gen_pic_name()
        img.save(pic_path)

    def on_message(self, message):
        print(str(message))
        if len(message) == 32:
            self.write_message(message)
            print("send message")
            self.close()

    def on_close(self):
        self.close()
        print("close")
