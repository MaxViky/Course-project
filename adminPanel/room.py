import sqlite3 as sql
from tkinter import ttk, messagebox
from tkinter import *
import null
from connection import *


class Room:
    def __init__(self, win):
        self.room_table = ttk.Treeview(win, height=10)
        self.AddBtn = Button(win, text='Добавить')
        self.horizontalScrollBar = ttk.Scrollbar(win, orient="horizontal", command=self.room_table.xview)
        self.verticalScrollBar = ttk.Scrollbar(win, orient="vertical", command=self.room_table.yview)
        self.l_name = Label(win, text="Название", justify=RIGHT)
        self.l_type = Label(win, text="Тип")
        self.l_cost = Label(win, text="Стоимость")
        self.l_beds = Label(win, text="Кроватей")
        self.l_breakfast = Label(win, text="Стоимость завтрака")
        self.l_busy = Label(win, text="Занят")
        self.l_photo = Label(win, text="Фото")

        self.e_name = Entry(win)
        self.e_type = Entry(win)
        self.e_cost = Entry(win)
        self.e_beds = Entry(win)
        self.e_breakfast = Entry(win)
        self.e_busy = Entry(win)
        self.e_photo = Entry(win)

        self.initUI()

    def initUI(self):
        self.room_table.configure(yscrollcommand=self.verticalScrollBar.set,
                                  xscrollcommand=self.horizontalScrollBar.set)

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

        self.AddBtn['command'] = self.addRoom

    def create(self):
        cur.execute("SELECT * FROM rooms")
        rows = cur.fetchall()
        for row in rows:
            self.room_table.insert("", "end", values=row)

        self.room_table.grid(row=0, column=1, columnspan=10)
        self.verticalScrollBar.grid(row=0, column=0)
        self.horizontalScrollBar.grid(row=1, column=1, columnspan=10)

        self.l_name.grid(row=2, column=1)
        self.l_type.grid(row=3, column=1)
        self.l_cost.grid(row=4, column=1)
        self.l_beds.grid(row=5, column=1)
        self.l_breakfast.grid(row=6, column=1)
        self.l_busy.grid(row=7, column=1)
        self.l_photo.grid(row=8, column=1)

        self.e_name.grid(row=2, column=2)
        self.e_type.grid(row=3, column=2)
        self.e_cost.grid(row=4, column=2)
        self.e_beds.grid(row=5, column=2)
        self.e_breakfast.grid(row=6, column=2)
        self.e_busy.grid(row=7, column=2)
        self.e_photo.grid(row=8, column=2)

        self.AddBtn.grid(row=9, column=2)

    def destroy(self):
        self.room_table.destroy()
        self.horizontalScrollBar.destroy()
        self.verticalScrollBar.destroy()

    def addRoom(self):
        try:
            command = "INSERT INTO rooms VALUES(Null, '{0}', {1}, {2}, {3}, {4}, {5}, '{6}')".format(
                self.e_name.get(), self.e_type.get(), self.e_cost.get(),
                self.e_beds.get(), self.e_breakfast.get(), self.e_busy.get(), self.e_photo.get()
            )
            cur.execute(command)
            conn.commit()
        except:
            messagebox.showinfo('Ошибка', 'Не удалось добавить комнату')
        # row_id = self.room_table.focus()[1:]
