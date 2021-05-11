from threading import Lock, Thread
from room import room
def index2d(list2d,value):
    for i, x in enumerate(list2d):
        if value in x:
            return (i, x.index(value))[0]
    return None

class RoomManagementMeta(type):
    _instances = {}
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class RoomManagement(metaclass=RoomManagementMeta):
    def __init__(self):
        self.__List_of_Players_joined_with_roomNumbers = []
        self.__List_of_Rooms=[room(),room()]


    def join(self, user):
        room=self.choose()
        if room.free:
            print(user.name, "joined")
            self.__addPlayer(user,room)
            return 1
        else:
            print("Sorry, the game is full")
            return 0

    def unjoin(self, user):
        if self.is_joined(user):
            self.__removePlayer(user)
            print("Player", user.name, "unjoined")
            return 1
        else:
            print("This player is not in the Room ")
            return 0

    def __addPlayer(self, user,room):
        room.add_Player()
        self.__List_of_Players_joined_with_roomNumbers.append([user,room])
    def __removePlayer(self,user):
        list2d=self.__List_of_Players_joined_with_roomNumbers
        idx=index2d(list2d,user)
        room=self.__List_of_Players_joined_with_roomNumbers[idx][1]
        room.removePlayer()
        self.__List_of_Players_joined_with_roomNumbers.pop(idx)

    def is_joined(self,user):
        list2d=self.__List_of_Players_joined_with_roomNumbers
        if index2d(list2d,user)==None:
            return False
        else:
            return True
    def choose(self):
        for i in self.__List_of_Rooms:
            if i.free:
                print("Room chosen")
                return i

    # def QuitRoom(self, user):
    #         print("Room quitted")
    #         user.is_playing=False
    #         user.update()
    #         return 1

