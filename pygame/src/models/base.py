import pymysql


class BaseModel(object):
    def __init__(self):
        if self.__class__.__name__ == "BaseModel":
            raise RuntimeError("BaseModel cannot have instance")
        else:
            db = pymysql.connect(host="127.0.0.1", user="root", password="root", database="Game")
