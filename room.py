class room:
    __id=0
    def __init__(self):
        self.number=room.__id
        room.__id+=1
        self.numberOfPlayer=0
        self.free=True
        self.max=4

    def add_Player(self):
        if self.numberOfPlayer< self.max:
            self.numberOfPlayer+=1
        else:
            self.free=False
    def removePlayer(self):
        if self.numberOfPlayer>0:
            self.numberOfPlayer-=1
            self.free=True



