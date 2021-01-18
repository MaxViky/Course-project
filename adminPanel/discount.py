from tkinter import ttk, messagebox, filedialog
from tkinter import *

from Search import Search
from PageController import PageController
from Sorting import Sorting
from connection import *


class Discount():
    def __init__(self, win):
        self.command = "SELECT discounts.id, room, name, discount FROM discounts INNER JOIN rooms " \
                       "on discounts.room = rooms.id"

        self.discount_table = ttk.Treeview(win, height=10)

        self.fieldsRU = ['Комната', 'Размер скидки']
        self.fieldsEN = ['room', 'discount']

        self.AddBtn = Button(win, text='Добавить')
        self.EditBtn = Button(win, text='Редактировать', width=15)
        self.DeleteBtn = Button(win, text='Удалить', width=15)

        self.l_room = Label(win, text='Комната')
        self.l_discount = Label(win, text='Скидка')

        cur.execute('SELECT id, name FROM rooms')
        self.e_room = ttk.Combobox(win, width=17, values=["{} - {}".format(*row) for row in cur.fetchall()])
        self.e_discount = Entry(win, width=20)

        self.initUI(win)

    def initUI(self, win):
        PageController(win, 'SELECT COUNT(*) FROM discounts', self.discount_table, self.command)
        Search(win, self.command, self.discount_table, self.fieldsRU, self.fieldsEN)
        Sorting(win, self.command, self.discount_table, self.fieldsRU, self.fieldsEN)

        self.discount_table["columns"] = ("1", "2", "3", "4")
        self.discount_table["show"] = 'headings'

        self.discount_table.column("1", width=50)
        self.discount_table.column("2", width=200)
        self.discount_table.column("3", width=200)
        self.discount_table.column("4", width=100)

        self.discount_table.heading("1", text="Ид")
        self.discount_table.heading("2", text="Номер комнаты")
        self.discount_table.heading("3", text="Название")
        self.discount_table.heading("4", text="Скидка")

        self.discount_table.bind('<ButtonRelease>', self.fillField)

        self.AddBtn['command'] = self.Add
        self.EditBtn['command'] = self.Update
        self.DeleteBtn['command'] = self.Delete

    def create(self):
        cur.execute("SELECT discounts.id, room, name, discount FROM discounts INNER JOIN rooms "
                    "on discounts.room = rooms.id LIMIT 5 OFFSET 0")
        rows = cur.fetchall()
        for row in rows:
            self.discount_table.insert("", "end", values=row)

        self.discount_table.grid(row=0, column=1, columnspan=20, sticky='w')

        self.l_room.grid(row=3, column=1, sticky='w')
        self.l_discount.grid(row=4, column=1, sticky='w')

        self.e_room.grid(row=3, column=2, sticky='w')
        self.e_discount.grid(row=4, column=2, sticky='w')

        self.AddBtn.grid(row=5, column=2)
        self.EditBtn.grid(row=5, column=1)
        self.DeleteBtn.grid(row=6, column=1)

    def Add(self):
        try:
            room = self.e_room.get().split(" - ")[0]

            command = "INSERT INTO discounts VALUES(Null, {0}, {1})".format(
                room, self.e_discount.get()
            )
            cur.execute(command)
            conn.commit()

            self.discount_table.delete(*self.discount_table.get_children())

            cur.execute(self.command + " LIMIT 5 OFFSET 0")
            rows = cur.fetchall()
            for row in rows:
                self.discount_table.insert("", "end", values=row)
        except:
            messagebox.showinfo('Ошибка', 'Не удалось добавить данные')

    def Update(self):
        try:
            room = self.e_room.get().split(" - ")[0]

            _id = self.discount_table.item(self.discount_table.selection(), 'values')[0]
            command = "UPDATE discounts SET " \
                      "room={0}, discount={1} WHERE id={2}".format(
                room, self.e_discount.get(), _id
            )
            cur.execute(command)

            self.discount_table.delete(*self.discount_table.get_children())

            cur.execute(self.command + " LIMIT 5 OFFSET 0")
            rows = cur.fetchall()
            for row in rows:
                self.discount_table.insert("", "end", values=row)

        except:
            messagebox.showinfo('Ошибка', 'Не удалось обновить данные')
        conn.commit()

    def Delete(self):
        _id = self.discount_table.item(self.discount_table.selection(), 'values')[0]
        command = "DELETE FROM discounts WHERE id={0}".format(_id)
        try:
            cur.execute(command)
            cur.execute(self.command + " LIMIT 5 OFFSET 0")
            rows = cur.fetchall()
            for row in rows:
                self.discount_table.insert("", "end", values=row)

        except:
            messagebox.showinfo('Ошибка', 'Не удалось обновить данные')
        conn.commit()

    def fillField(self, event):
        try:
            self.e_room.delete(0, END)
            self.e_discount.delete(0, END)

            _id = self.discount_table.item(self.discount_table.selection(), 'values')[0]
            list = cur.execute('SELECT * FROM discounts WHERE id={0}'.format(_id)).fetchone()

            self.e_room.insert(0, list[1])
            self.e_discount.insert(0, list[2])
        except:
            pass
