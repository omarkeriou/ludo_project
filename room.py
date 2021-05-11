from LudoScheduler import Ludo_Scheduler
class room:
    __id=0
    def __init__(self,max=4):
        self.number=room.__id
        room.__id+=1
        self.numberOfPlayer=0
        self.free=True
        self.joinable=False
        self.max=max
        self.GameScheduler=Ludo_Scheduler()

    def add_Player(self):
        if self.numberOfPlayer< self.max and self.joinable:
            self.numberOfPlayer+=1
        else:
            self.free=False
            self.joinable=False
            self.GameScheduler.addRoom(self)

    def removePlayer(self):
        if self.numberOfPlayer>0:
            self.numberOfPlayer-=1
            self.free=True
        else:
            self.GameScheduler.removeRoom(self)


    def startPlaying(self):
        if self.free==False:
            self.joinable = False


    def stopPlaying(self):
        self.joinable = True




