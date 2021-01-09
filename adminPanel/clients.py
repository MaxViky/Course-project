import sqlite3 as sql
from tkinter import ttk, messagebox, filedialog
from tkinter import *

from Search import Search
from PageController import PageController
from connection import *


class Clients:
    def __init__(self, win):
        self.command = 'SELECT * FROM clients'
        self.client_table = ttk.Treeview(win, height=10)
        self.fields = ['name', 'type', 'cost', 'beds_count', 'breakfast', 'busy']

        self.AddBtn = Button(win, text='Добавить')
        self.EditBtn = Button(win, text='Редактировать', width=15)
        self.DeleteBtn = Button(win, text='Удалить', width=15)
        self.ChoiceImage = Button(win, text='...', width=5)

        self.l_name = Label(win, text="ФИО", justify=RIGHT)
        self.l_phone = Label(win, text="Телефон")
        self.l_passport = Label(win, text="Паспорт")
        self.l_photo = Label(win, text="Фото")

        self.e_name = Entry(win, width=20)
        self.e_phone = Entry(win, width=20)
        self.e_passport = Entry(win, width=20)
        self.e_photo = Entry(win, width=20)
        self.initUI(win)

    def initUI(self, win):
        PageController(win, 'SELECT COUNT(*) FROM clients', self.client_table, self.command)
        # Search(win, self.command, self.room_table, self.fields)

        self.client_table["columns"] = ("1", "2", "3", "4", "5")
        self.client_table["show"] = 'headings'

        self.client_table.column("1", width=50)
        self.client_table.column("2", width=200)
        self.client_table.column("3", width=100)
        self.client_table.column("4", width=100)
        self.client_table.column("5", width=50)

        self.client_table.heading("1", text="Ид")
        self.client_table.heading("2", text="ФИО")
        self.client_table.heading("3", text="Телефон")
        self.client_table.heading("4", text="Паспорт")
        self.client_table.heading("5", text="Фото")

        self.AddBtn['command'] = self.AddRoom
        self.EditBtn['command'] = self.UpdateRoom
        self.DeleteBtn['command'] = self.DeleteRoom
        self.ChoiceImage['command'] = self.Browse

    def create(self):
        cur.execute("SELECT * FROM clients LIMIT 5 OFFSET 0")
        rows = cur.fetchall()
        for row in rows:
            self.client_table.insert("", "end", values=row)

        self.client_table.grid(row=0, column=1, columnspan=20)

        self.l_name.grid(row=3, column=1, sticky='w')
        self.l_phone.grid(row=4, column=1, sticky='w')
        self.l_passport.grid(row=5, column=1, sticky='w')
        self.l_photo.grid(row=6, column=1, sticky='w')

        self.e_name.grid(row=3, column=2, sticky='w')
        self.e_phone.grid(row=4, column=2, sticky='w')
        self.e_passport.grid(row=5, column=2, sticky='w')
        self.e_photo.grid(row=6, column=2, sticky='w')

        self.AddBtn.grid(row=7, column=2)
        self.EditBtn.grid(row=7, column=1)
        self.DeleteBtn.grid(row=8, column=1)
        self.ChoiceImage.grid(row=6, column=3)

    def AddRoom(self):
        try:
            command = "INSERT INTO clients VALUES(Null, '{0}', '{1}', '{2}', '{3}')".format(
                self.e_name.get(), self.e_phone, self.e_passport, self.e_photo.get()
            )
            cur.execute(command)
            conn.commit()
        except:
            messagebox.showinfo('Ошибка', 'Не удалось добавить данные')

    def UpdateRoom(self):
        _id = self.client_table.item(self.client_table.selection(), 'values')[0]
        command = "UPDATE clients SET " \
                  "name='{0}', phone={1}, passport={2}, photo='{3}' WHERE id={4}".format(
            self.e_name.get(), self.e_phone, self.e_passport, self.e_photo.get(), _id
        )
        try:
            cur.execute(command)
        except:
            messagebox.showinfo('Ошибка', 'Не удалось обновить данные')
        conn.commit()

    def DeleteRoom(self):
        _id = self.client_table.item(self.client_table.selection(), 'values')[0]
        command = "DELETE FROM clients WHERE id={0}".format(_id)
        try:
            cur.execute(command)
        except:
            messagebox.showinfo('Ошибка', 'Не удалось обновить данные')
        conn.commit()

    def Browse(self):
        file = filedialog.askopenfilename()
        self.e_photo.delete(0, END)
        self.e_photo.insert(0, file)