import sqlite3 as sql
from tkinter import *
from adminPanel.room import Room


class AdminMenu:
    def __init__(self):
        self.win = Tk()
        self.win.title('Панель администратора')
        self.win.geometry('800x650')
        self.Create()

    def Create(self):
        menu = Menu(self.win)
        file_menu = Menu(menu, font=("Comic Sans MS", 12), tearoff=0)

        file_menu.add_command(label="Комнаты", command=self.CreateRoom)
        file_menu.add_command(label="Клиенты")
        file_menu.add_command(label="Бронирование")
        file_menu.add_command(label="Типы комнат")
        file_menu.add_command(label="Скидки")
        file_menu.add_command(label="Пользователи")
        file_menu.add_separator()

        menu.add_cascade(label="Таблицы", font=("Comic Sans MS", 12), menu=file_menu)
        menu.add_cascade(label="Информация", font=("Comic Sans MS", 12))
        self.win.configure(menu=menu)
        self.win.mainloop()

    def CreateRoom(self):
        self.room = Room(self.win)
        self.room.create()

    def CreateClient(self):
        self.room.Destroy()

    def CreateReserv(self):
        self.room.Destroy()

    def CreateType(self):
        self.room.Destroy()

    def CreateDiscount(self):
        self.room.Destroy()

    def CreateUser(self):
        self.room.Destroy()

AdminMenu()