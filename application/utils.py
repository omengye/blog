import datetime
import time
import uuid
import re
import hashlib


class Utils(object):
    @staticmethod
    def time_now():
        return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    @staticmethod
    def generate_uuid():
        str_uuid = str(uuid.uuid4())
        return str_uuid.replace('-', '')

    @staticmethod
    def no_special_symbol(x):
        if re.match('^[A-Za-z0-9_.@]+$', str(x)):
            return True
        else:
            return False

    @staticmethod
    def md5_pass(x):
        m = hashlib.md5()
        m.update(str(x).encode('UTF-8'))
        return m.hexdigest()

    @staticmethod
    def not_empty(x):
        if x == "" or x is None:
            return False
        else:
            return True

    @staticmethod
    def epoch_before_sec(x):
        t = datetime.datetime.now()
        before = t + datetime.timedelta(seconds=x)
        e_time = time.mktime(before.timetuple())  # 把时间转换成Epoch秒数
        return e_time

    @staticmethod
    def interval_sec(x):
        def time_split(token_time):
            [date_year, date_time] = token_time.split("T")
            [year, month, day] = date_year.split("-")
            [hour, minu, sec] = date_time.split(":")
            unix_time = datetime.datetime(year=int(year), month=int(month), day=int(day), hour=int(hour),
                                          minute=int(minu), second=int(sec))
            return time.mktime(unix_time.timetuple())

        unix_time_now = Utils.epoch_before_sec(0)
        unix_time_tooken = time_split(x)

        return unix_time_now - unix_time_tooken


