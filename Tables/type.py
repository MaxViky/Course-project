from tkinter import ttk, messagebox
from tkinter import *

from UI import UI
from connection import *


class RoomType:
    def __init__(self, win):
        self.command = 'SELECT * FROM roomtype'
        self.roomtype_table = ttk.Treeview(win, height=10)

        self.fieldsRU = ['Тип', 'Описание']
        self.fieldsEN = ['type', 'discription']

        self.AddBtn = Button(win, text='Добавить')
        self.EditBtn = Button(win, text='Редактировать', width=15)
        self.DeleteBtn = Button(win, text='Удалить', width=15)

        self.l_name = Label(win, text="Тип", justify=RIGHT)
        self.l_description = Label(win, text="Описание")

        self.e_name = Entry(win, width=20)
        self.e_description = Entry(win, width=50)

        self.initUI(win)

    def initUI(self, win):
        UI(win, self.command, 'SELECT COUNT(*) FROM roomtype', self.roomtype_table, self.fieldsRU, self.fieldsEN)

        self.roomtype_table["columns"] = ("1", "2", "3")
        self.roomtype_table["show"] = 'headings'

        self.roomtype_table.column("1", width=50)
        self.roomtype_table.column("2", width=100)
        self.roomtype_table.column("3", width=700)

        self.roomtype_table.heading("1", text="Ид")
        self.roomtype_table.heading("2", text="Тип")
        self.roomtype_table.heading("3", text="Описание")

        self.roomtype_table.bind('<ButtonRelease>', self.fillField)

        self.AddBtn['command'] = self.Add
        self.EditBtn['command'] = self.Update
        self.DeleteBtn['command'] = self.Delete

    def create(self):
        cur.execute("SELECT * FROM roomtype LIMIT 5 OFFSET 0")
        rows = cur.fetchall()
        for row in rows:
            self.roomtype_table.insert("", "end", values=row)

        self.roomtype_table.grid(row=0, column=1, columnspan=20, sticky='w')

        self.l_name.grid(row=3, column=1, sticky='w')
        self.l_description.grid(row=4, column=1, sticky='w')

        self.e_name.grid(row=3, column=2, sticky='w')
        self.e_description.grid(row=4, column=2, sticky='w')

        self.AddBtn.grid(row=10, column=2)
        self.EditBtn.grid(row=10, column=1)
        self.DeleteBtn.grid(row=11, column=1)

    def Add(self):
        try:
            command = "INSERT INTO roomtype VALUES(Null, '{0}', '{1}')".format(
                self.e_name, self.e_description
            )
            cur.execute(command)
            conn.commit()

            self.roomtype_table.delete(*self.roomtype_table.get_children())

            cur.execute("SELECT * FROM rooms LIMIT 5 OFFSET 0")
            rows = cur.fetchall()
            for row in rows:
                self.roomtype_table.insert("", "end", values=row)
        except:
            messagebox.showinfo('Ошибка', 'Не удалось добавить данные')

    def Update(self):
        try:
            _id = self.roomtype_table.item(self.roomtype_table.selection(), 'values')[0]
            command = "UPDATE roomtype SET " \
                      "name='{0}', type={1} WHERE id={2}".format(
                self.e_name.get(), self.e_description.get(), _id
            )
            cur.execute(command)

            self.roomtype_table.delete(*self.roomtype_table.get_children())

            cur.execute("SELECT * FROM rooms LIMIT 5 OFFSET 0")
            rows = cur.fetchall()
            for row in rows:
                self.roomtype_table.insert("", "end", values=row)

        except:
            messagebox.showinfo('Ошибка', 'Не удалось обновить данные')
        conn.commit()

    def Delete(self):
        answer = messagebox.askyesno(
            title="Удаление",
            message="Удалить тип комнаты?")
        if answer:
            _id = self.roomtype_table.item(self.roomtype_table.selection(), 'values')[0]
            command = "DELETE FROM roomtype WHERE id={0}".format(_id)
            try:
                cur.execute(command)
            except:
                messagebox.showinfo('Ошибка', 'Не удалось обновить данные')
            conn.commit()

    def fillField(self, event):

        self.e_name.delete(0, END)
        self.e_description.delete(0, END)

        _id = self.roomtype_table.item(self.roomtype_table.selection(), 'values')[0]
        cur.execute('SELECT * FROM roomtype WHERE id={0}'.format(_id))
        list = cur.fetchone()
        self.e_name.insert(0, list[1])
        self.e_description.insert(0, list[2])


