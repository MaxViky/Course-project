from tkinter import *

from adminPanel.clients import Clients
from adminPanel.room import Room
from adminPanel.type import RoomType


class AdminMenu:
    def __init__(self):
        self.win = Tk()
        self.win.title('Панель администратора')
        self.win.geometry('800x650')
        self.Create()

    def Create(self):
        menu = Menu(self.win)
        file_menu = Menu(menu, tearoff=0)

        file_menu.add_command(label="Комнаты", command=self.CreateRoom)
        file_menu.add_command(label="Клиенты", command=self.CreateClient)
        file_menu.add_command(label="Бронирование")
        file_menu.add_command(label="Типы комнат", command=self.CreateType)
        file_menu.add_command(label="Скидки")
        file_menu.add_command(label="Пользователи")
        file_menu.add_separator()

        menu.add_cascade(label="Таблицы", menu=file_menu)
        menu.add_cascade(label="Информация")
        self.win.configure(menu=menu)
        self.win.mainloop()

    def CreateRoom(self):
        try:
            self.roomtype.Destroy()
            self.clients.Destroy()
        except:
            pass
        self.room = Room(self.win)
        self.room.create()

    def CreateClient(self):
        try:
            self.room.Destroy()
            self.roomtype.Destroy()
        except:
            pass
        self.clients = Clients(self.win)
        self.clients.create()

    def CreateReserv(self):
        self.room.Destroy()

    def CreateType(self):
        try:
            self.room.Destroy()
            self.clients.Destroy()
        except:
            pass
        self.roomtype = RoomType(self.win)
        self.roomtype.create()

    def CreateDiscount(self):
        self.room.Destroy()

    def CreateUser(self):
        self.room.Destroy()


AdminMenu()
