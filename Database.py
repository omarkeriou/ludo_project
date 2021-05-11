from LudoDatabase import *

class DatabaseMeta(type):
    _instances = {}
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=DatabaseMeta):
    def __init__(self):
        self.Ludo_DataBase = Ludo_Database()
        self.connect()

    def connect(self):
        self.Ludo_DataBase.connect()

    def insert_list(self,list):
        self.Ludo_DataBase.set_List_of_all_Players(list)
        self.Ludo_DataBase.insert_Player_list()

    def select_list(self):
        self.Ludo_DataBase.select_Player_list()
        return self.Ludo_DataBase.get_List_of_all_Players()

    def select_one(self,user_data):
        self.Ludo_DataBase.set_List_of_all_Players(user_data)
        self.Ludo_DataBase.load_Player()
        return self.Ludo_DataBase.get_List_of_all_Players()[0]

    def insert_one(self,user_data):
        self.Ludo_DataBase.set_List_of_all_Players(user_data)
        self.Ludo_DataBase.insert_Player()
    def delete_one(self,user_data):
        self.Ludo_DataBase.set_List_of_all_Players(user_data)
        self.Ludo_DataBase.remove_Player()









