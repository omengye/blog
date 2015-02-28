import os

from application.utils import Utils


class Cron(object):

    @staticmethod
    def del_qr_cron():
        try:
            time_before = Utils.epoch_before_sec(-300)  # 删除5分钟前生成的qr code图像
            pics_path = os.path.join(os.path.dirname(__file__), "../static/qrpic")
            for pic in os.listdir(pics_path):
                if len(pic) == 49:
                    pic_create_time = pic.split("_")[0]
                    if str(time_before) >= pic_create_time:
                        pic_path = os.path.join(pics_path, pic)
                        os.remove(pic_path)
                        print("cron job delete qr pic")
        except OSError:
            print("delete qr qr pic error")



