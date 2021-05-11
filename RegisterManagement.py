from threading import Lock, Thread

def index2d(list2d,value):
    for i, x in enumerate(list2d):
        if value in x:
            return (i, x.index(value))[0]
    return None

class RegisterManagementMeta(type):
    _instances = {}
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class RegisterManagement(metaclass=RegisterManagementMeta):
    def __init__(self):
        self.__List_of_Players = []


    def register(self, user):
        if not self.is_registered(user):
            self.__RegisterPlayer(user)
            print("Player", user.name, "registered")
            return 1
        else:
            print("Player", user.name, "is already registered")
            return 0
    def login(self, user):
        if self.is_registered(user):
            self.__login_Player(user)
            print("Player", user.name, "logged in")
            return 1
        else:
            print("Player", user.name, "is already logged in")
            return 0
    def unregister(self, user):
        if self.is_registered(user):
            self.__removePlayer(user)
            print("Player", user.name, "unregistered")
            return 1
        else:
            print("This player is not registered")
            return 0
    def __RegisterPlayer(self, user):
        self.__List_of_Players.append([user,True])

    def __removePlayer(self, user):
        list2d = self.__List_of_Players
        idx = index2d(list2d, user)
        self.__List_of_Players.pop(idx)

    def __login_Player(self, user):
        list2d=self.__List_of_Players
        idx=index2d(list2d,user)
        self.__List_of_Players[idx][1]=True
    def __logout_Player(self,user):
        list2d = self.__List_of_Players
        idx = index2d(list2d, user)
        self.__List_of_Players[idx][1] = False

    def is_logged_in(self,user):
        list2d=self.__List_of_Players
        idx=index2d(list2d,user)
        if idx==None:
            return False
        else:
            return self.__List_of_Players[idx][1]

    def is_registered(self,user):
        list2d=self.__List_of_Players
        idx=index2d(list2d,user)
        if idx==None:
            return False
        else:
            return True

