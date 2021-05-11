from threading import Lock, Thread

class Ludo_SchedulerMeta(type):
    _instances = {}
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class Ludo_Scheduler(metaclass=Ludo_SchedulerMeta):
    def __init__(self):
        self.List_of_Rooms=[]

    def addRoom(self,room_to_add):
        self.List_of_Rooms.append(room_to_add)
    def removeRoom(self,room_to_remove):
        self.List_of_Rooms.remove(room_to_remove)
