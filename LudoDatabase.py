import mysql.connector
from mysql.connector import errorcode
from threading import Lock
from MySQL_DB import MySQL_DB

class Ludo_DatabasetMeta(type):
    _instances = {}
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]



class Ludo_Database(metaclass=Ludo_DatabasetMeta):
    def __init__(self):
        self.List_of_Players=[]
        self.__DB= MySQL_DB(DB_name='Ludo_DB',user='root',password='Sarrounpw.1',Table_name='users')
        self.table={'Nickname':'varchar(14)',
                    'Password':'varchar(60)',
                    'Age':'int(3)',
                    'Nationality':'varchar(20)',
                    'Score':'int(4)',
                    'Trophies':'int(3)',
                    'PRIMARY KEY':'(Nickname,Password)'
                    }


    def list_to_Dict(self,Data_list):
        return [{list(self.table)[i]: Data_list[j][i] for i in range(len(Data_list[j]))} for j in range(len(Data_list))]
    def connect(self):
        self.__DB.connect()
        self.__DB.create_database()
        self.__DB.use_DB()
        self.__DB.create_Table(self.table)

    def select_Player_list(self):
        self.__DB.select_all()


    def insert_Player_list(self):
        self.__DB.insert_all(self.table)


    def get_List_of_all_Players(self):
        self.List_of_Players=self.__DB.getData()
        return self.list_to_Dict(self.List_of_Players)

    def set_List_of_all_Players(self,list):
        list_dct=self.list_to_Dict(list)
        self.List_of_Players=list_dct
        self.__DB.setData(self.List_of_Players)

    def load_Player(self):
        self.__DB.select_one(self.List_of_Players)


    def insert_Player(self):
        self.__DB.insert_one(self.table)

    def remove_Player(self):
        self.__DB.delete_one(self.List_of_Players)

