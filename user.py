from abc import ABC, abstractmethod
from GameManagement import *
from types import FunctionType



class user():
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.nationality = ""
        self.GameManager=GameManagement()
        # self.registered=False
        # self.is_playing=False
        # self.logged_in=False
        self.list_of_Methods=[self.register,self.login,self.quit,self.edit_profile,self.closeWindow]

    def show_all_available_methods(self):
        return print([i.__name__ for i in self.list_of_Methods])
    def register(self):
        if self.register in self.list_of_Methods:
            if self.GameManager.register(self):
                return 1
            else:
                return 0
        else:
            raise ("no access to register")
    def login(self):
        if self.login in self.list_of_Methods:
            if self.GameManager.login(self):

                return 1
            else:
                return 0
        else:
            raise ("no access to login")
    def edit_profile(self):
        if self.edit_profile in self.list_of_Methods:
            ...
    def join(self):
        if self.join in self.list_of_Methods:
            if self.GameManager.join(self):
                return 1
            else:
                return 0
    def quit(self):
        if self.quit in self.list_of_Methods:
            self.GameManager.quit()
        else:
            return 0
    def unregister(self):
        if self.unregister in self.list_of_Methods:
            if self.GameManager.unregister(self):
                return 1
            else:
                return 0
    def chooseRoom(self):
        if self.chooseRoom in self.list_of_Methods:
            self.GameManager.choose()
    def play(self):
        if self.play in self.list_of_Methods:
            print("play")
            return 1
    def closeWindow(self):
        if self.closeWindow in self.list_of_Methods:
            self.GameManager.closeWindow()
    def OpenWindow(self):
        print("Window opened")
    def QuitRoom(self):
        if self.QuitRoom in self.list_of_Methods:
            self.GameManager.unjoin(self)





