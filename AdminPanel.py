from tkinter import *

from adminPanel.clients import Clients
from adminPanel.room import Room
from adminPanel.type import RoomType


class AdminMenu:
    def __init__(self):
        self.win = Tk()
        self.frame = Frame(self.win)
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
        self.frame.grid(row=0, column=0)
        self.win.mainloop()


    def CreateRoom(self):
        try:
            for widget in self.frame.winfo_children():
                widget.destroy()
        except:
            pass
        self.room = Room(self.frame)
        self.room.create()

    def CreateClient(self):
        try:
            for widget in self.frame.winfo_children():
                widget.destroy()
        except:
            pass
        self.clients = Clients(self.frame)
        self.clients.create()

    def CreateReserv(self):
        pass

    def CreateType(self):
        try:
            for widget in self.frame.winfo_children():
                widget.destroy()
        except:
            pass
        self.roomtype = RoomType(self.frame)
        self.roomtype.create()

    def CreateDiscount(self):
        pass

    def CreateUser(self):
        pass


AdminMenu()
