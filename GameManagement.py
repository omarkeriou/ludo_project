from threading import Lock, Thread
from RoomManagement import *
from RegisterManagement import *
from Database import *

class GameManagementMeta(type):
    _instances = {}
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class GameManagement(metaclass=GameManagementMeta):
    def __init__(self):
        self.RoomManagement = RoomManagement()
        self.RegisterManagement = RegisterManagement()
        self.Database= Database()
        self.Test_Database()

    def Test_Database(self):
        self.Database.insert_list([['Om','vvvvv',28,'Tun',147,1410],['Osm','vvvvv',28,'Tun',147,1410],['hgfd','vvvvv',8,'Tu',1440,140]])
        a=self.Database.select_list()
        for i in a:
            print(i)
        b=self.Database.select_one([['hgfd','vvvvv']])
        print(b)
        self.Database.insert_one([['omar', 'vvzgv',15,'Sui',1,-1]])
        self.Database.delete_one([['hgfd','vvvvv']])
        a=self.Database.select_list()
        for i in a:
            print(i)


    def register(self, user):
        self.RegisterManagement.register(user)
        self.update(user)

    def login(self, user):
        self.RegisterManagement.login(user)
        self.update(user)

    def unregister(self, user):
        self.RegisterManagement.unregister(user)
        self.update(user)
        return 1

    def update(self, user):
        if self.RoomManagement.is_joined(user):
            user.list_of_Methods = [user.play, user.QuitRoom, user.closeWindow]
        elif self.RegisterManagement.is_logged_in(user):
            user.list_of_Methods = [user.join, user.unregister, user.chooseRoom, user.quit, user.closeWindow]
        else:
            user.list_of_Methods = [user.register, user.login, user.quit, user.edit_profile, user.closeWindow]

    def join(self, user):
        self.RoomManagement.join(user)
        self.update(user)

    def unjoin(self, user):
        self.RoomManagement.unjoin(user)
        self.update(user)


    def quit(self,user):
        if self.RoomManagement.is_joined(user) == True:
            self.unjoin()
            self.closeWindow()
        else:
            self.closeWindow()
        self.update(user)
        return 1

    def closeWindow(self):
        print("Window closed")