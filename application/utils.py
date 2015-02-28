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
