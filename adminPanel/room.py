import sqlite3 as sql
from tkinter import ttk
from tkinter import *
from connection import *


class Room:
    def __init__(self, win):
        self.room_table = ttk.Treeview(win, height=20)
        self.horizontalScrollBar = ttk.Scrollbar(win, orient="horizontal", command=self.room_table.xview)
        self.verticalScrollBar = ttk.Scrollbar(win, orient="vertical", command=self.room_table.yview)
        self.room_table.configure(yscrollcommand=self.verticalScrollBar.set, xscrollcommand=self.horizontalScrollBar.set)
        self.room_table["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
        self.room_table["show"] = 'headings'

        self.room_table.column("1", width=50)
        self.room_table.column("2", width=200)
        self.room_table.column("3", width=50)
        self.room_table.column("4", width=100)
        self.room_table.column("5", width=50)
        self.room_table.column("6", width=200)
        self.room_table.column("7", width=50)
        self.room_table.column("8", width=100)

        self.room_table.heading("1", text="Ид")
        self.room_table.heading("2", text="Название")
        self.room_table.heading("3", text="Тип")
        self.room_table.heading("4", text="Стоимость")
        self.room_table.heading("5", text="Кроватей")
        self.room_table.heading("6", text="Стоимость завтрака")
        self.room_table.heading("7", text="Занят")
        self.room_table.heading("8", text="Фото")
        self.selectbtn = Button(win, text='Редактировать')



    def create(self):
        cur.execute("SELECT * FROM rooms")
        rows = cur.fetchall()
        for row in rows:
            self.room_table.insert("", "end", values=row)
        self.room_table.grid(row=0, column=1)
        self.verticalScrollBar.grid(row=0, column=0)
        self.horizontalScrollBar.grid(row=1, column=1)
        self.selectbtn['command'] = self.select
        self.selectbtn.grid(row=2, column=1)

    def destroy(self):
        self.room_table.destroy()
        self.horizontalScrollBar.destroy()
        self.verticalScrollBar.destroy()

    def select(self):
        for x in self.room_table.selection():
            print([self.room_table.item(x)['values']])


