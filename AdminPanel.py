import sqlite3 as sql
from tkinter import *
from adminPanel.room import Room


class AdminMenu:
    def __init__(self):
        self.win = Tk()
        self.menu = Menu()
        self.file_menu = Menu(font=("Comic Sans MS", 12), tearoff=0)
        self.create()

    def create(self):
        self.win.title('Панель администратора')
        self.win.geometry('800x650')
        self.file_menu.add_command(label="Комнаты", command=self.createRoom)
        self.file_menu.add_command(label="Клиенты")
        self.file_menu.add_command(label="Бронирование")
        self.file_menu.add_command(label="Типы комнат")
        self.file_menu.add_command(label="Скидки")
        self.file_menu.add_command(label="Пользователи")
        self.file_menu.add_separator()

        self.menu.add_cascade(label="Таблицы", font=("Comic Sans MS", 12), menu=self.file_menu)
        self.menu.add_cascade(label="Информация", font=("Comic Sans MS", 12))
        self.win.configure(menu=self.menu)
        self.win.mainloop()

    def createRoom(self):
        self.room = Room(self.win)
        self.room.create()

    def createClient(self):
        self.room.destroy()

    def createReserv(self):
        self.room.destroy()

    def createType(self):
        self.room.destroy()

    def createDiscount(self):
        self.room.destroy()

    def createUser(self):
        self.room.destroy()
