from tkinter import ttk, messagebox
from tkinter import *

from Search import Search
from PageController import PageController
from connection import *


class RoomType:
    def __init__(self, win):
        self.command = 'SELECT * FROM roomtype'
        self.roomtype_table = ttk.Treeview(win, height=10)
        # self.fields = ['name', 'type', 'cost', 'beds_count', 'breakfast', 'busy']

        self.AddBtn = Button(win, text='Добавить')
        self.EditBtn = Button(win, text='Редактировать', width=15)
        self.DeleteBtn = Button(win, text='Удалить', width=15)

        self.l_name = Label(win, text="Тип", justify=RIGHT)
        self.l_description = Label(win, text="Описание")

        self.e_name = Entry(win, width=20)
        self.e_description = Entry(win, width=20)

        self.initUI(win)

    def initUI(self, win):
        PageController(win, 'SELECT COUNT(*) FROM roomtype', self.roomtype_table, self.command)

        self.roomtype_table["columns"] = ("1", "2", "3")
        self.roomtype_table["show"] = 'headings'

        self.roomtype_table.column("1", width=50)
        self.roomtype_table.column("2", width=100)
        self.roomtype_table.column("3", width=700)

        self.roomtype_table.heading("1", text="Ид")
        self.roomtype_table.heading("2", text="Тип")
        self.roomtype_table.heading("3", text="Описание")

        self.AddBtn['command'] = self.AddRoom
        self.EditBtn['command'] = self.UpdateRoom
        self.DeleteBtn['command'] = self.DeleteRoom

    def create(self):
        cur.execute("SELECT * FROM roomtype LIMIT 5 OFFSET 0")
        rows = cur.fetchall()
        for row in rows:
            self.roomtype_table.insert("", "end", values=row)

        self.roomtype_table.grid(row=0, column=1, columnspan=10)

        self.l_name.grid(row=3, column=1, sticky='w')
        self.l_description.grid(row=4, column=1, sticky='w')

        self.e_name.grid(row=3, column=2, sticky='w')
        self.e_description.grid(row=4, column=2, sticky='w')

        self.AddBtn.grid(row=10, column=2)
        self.EditBtn.grid(row=10, column=1)
        self.DeleteBtn.grid(row=11, column=1)

    def Destroy(self):
        self.roomtype_table.destroy()

        self.l_name.destroy()
        self.l_description.destroy()

        self.e_name.destroy()
        self.e_description.destroy()

        self.AddBtn.destroy()
        self.EditBtn.destroy()
        self.DeleteBtn.destroy()

    def AddRoom(self):
        try:
            command = "INSERT INTO roomtype VALUES(Null, '{0}', '{1}')".format(
                self.e_name, self.e_description
            )
            cur.execute(command)
            conn.commit()
        except:
            messagebox.showinfo('Ошибка', 'Не удалось добавить данные')

    def UpdateRoom(self):
        _id = self.roomtype_table.item(self.roomtype_table.selection(), 'values')[0]
        command = "UPDATE roomtype SET " \
                  "name='{0}', type={1} WHERE id={2}".format(
            self.e_name.get(), self.e_description.get(), _id
        )
        try:
            cur.execute(command)
        except:
            messagebox.showinfo('Ошибка', 'Не удалось обновить данные')
        conn.commit()

    def DeleteRoom(self):
        _id = self.roomtype_table.item(self.roomtype_table.selection(), 'values')[0]
        command = "DELETE FROM roomtype WHERE id={0}".format(_id)
        try:
            cur.execute(command)
        except:
            messagebox.showinfo('Ошибка', 'Не удалось обновить данные')
        conn.commit()



