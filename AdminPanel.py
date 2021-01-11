from datetime import datetime
from tkinter import *

from adminPanel.clients import Clients
from adminPanel.discount import Discount
from adminPanel.reservation import Reservation
from adminPanel.room import Room
from adminPanel.type import RoomType
from connection import cur, conn


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
        file_menu.add_command(label="Бронирование", command=self.CreateReserv)
        file_menu.add_command(label="Типы комнат", command=self.CreateType)
        file_menu.add_command(label="Скидки", command=self.CreateDiscount)
        file_menu.add_command(label="Пользователи", command=self.CreateUser)
        file_menu.add_separator()

        menu.add_cascade(label="Таблицы", menu=file_menu)
        menu.add_cascade(label="Информация")
        self.win.configure(menu=menu)
        self.frame.grid(row=0, column=0)

        now = datetime.now().date().strftime('%d.%m.%Y')
        cur.execute('SELECT room, departure_date FROM reservation')
        date = cur.fetchall()
        for i in date:
            if i[1] < now:
                cur.execute('UPDATE rooms SET busy = 0 WHERE id={0}'.format(i[0]))
                conn.commit()

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
        try:
            for widget in self.frame.winfo_children():
                widget.destroy()
        except:
            pass
        self.reservation = Reservation(self.frame)
        self.reservation.create()

    def CreateType(self):
        try:
            for widget in self.frame.winfo_children():
                widget.destroy()
        except:
            pass
        self.roomtype = RoomType(self.frame)
        self.roomtype.create()

    def CreateDiscount(self):
        try:
            for widget in self.frame.winfo_children():
                widget.destroy()
        except:
            pass
        self.discount = Discount(self.frame)
        self.discount.create()

    def CreateUser(self):
        pass


AdminMenu()
