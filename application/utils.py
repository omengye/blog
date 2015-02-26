import datetime
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
        return hashlib.md5(str(x))

    @staticmethod
    def not_empty(x):
        if x == "" or x is None:
            return False
        else:
            return True