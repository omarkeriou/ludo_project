from threading import Lock, Thread

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
        self.__List_of_Players_registered = []
        self.__number_of_Players_registered = 0
        self.__List_of_Players_logged_in=[]
        self.__number_of_Players_registered = 0

    def register(self, user):
        if user not in self.__List_of_Players_registered:
            self.__RegisterPlayer(user)
            print("Player", user.name, "registered")
            return 1
        else:
            print("Player", user.name, "is already registered")
            return 0
    def login(self, user):
        if user in self.__List_of_Players_registered:
            self.__login_Player(user)
            print("Player", user.name, "logged in")
            return 1
        else:
            print("Player", user.name, "is already logged in")
            return 0
    def unregister(self, user):
        if user in self.__List_of_Players_registered:
            self.__removePlayer(user)
            print("Player", user.name, "unregistered")
            return 1
        else:
            print("This player is not registered")
            return 0
    def __RegisterPlayer(self, user):
        self.__List_of_Players_registered.append(user)
        self.__number_of_Players_registered += 1
        self.__List_of_Players_logged_in.append(True)
    def __removePlayer(self, user):
        idx=self.__List_of_Players_registered.index(user)
        self.__List_of_Players_registered.pop(idx)
        self.__number_of_Players_registered -= 1
        self.__logout_Player(user)
    def __login_Player(self, user):
        idx=self.__List_of_Players_registered.index(user)
        self.__List_of_Players_logged_in[idx]=True
        self.__number_of_Players_logged_in += 1
    def __logout_Player(self,user):
        idx=self.__List_of_Players_registered.index(user)
        self.__List_of_Players_logged_in[idx]=False
        self.__number_of_Players_logged_in -= 1
    def is_logged_in(self,user):
        idx = self.__List_of_Players_registered.index(user)
        return self.__List_of_Players_logged_in[idx]


