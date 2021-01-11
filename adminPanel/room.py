from tkinter import ttk, messagebox, filedialog
from tkinter import *

from Search import Search
from PageController import PageController
from connection import *


class Room:
    def __init__(self, win):
        self.command = 'SELECT * FROM rooms'
        self.room_table = ttk.Treeview(win, height=10)
        self.fieldsRU = ['Название', 'Тип', 'Стоимость', 'Кроватей', 'Стоимость завтрака', 'Занят']
        self.fieldsEN = ['name', 'type', 'cost', 'beds_count', 'breakfast', 'busy']

        self.AddBtn = Button(win, text='Добавить')
        self.EditBtn = Button(win, text='Редактировать', width=15)
        self.DeleteBtn = Button(win, text='Удалить', width=15)
        self.ChoiceImage = Button(win, text='...', width=5)

        self.l_name = Label(win, text="Название", justify=RIGHT)
        self.l_type = Label(win, text="Тип")
        self.l_cost = Label(win, text="Стоимость")
        self.l_beds = Label(win, text="Кроватей")
        self.l_breakfast = Label(win, text="Стоимость завтрака")
        self.l_busy = Label(win, text="Занят")
        self.l_photo = Label(win, text="Фото")

        self.e_name = Entry(win, width=20)
        self.e_type = ttk.Combobox(win, width=17)
        self.e_cost = Entry(win, width=20)
        self.e_beds = Entry(win, width=20)
        self.e_breakfast = Entry(win, width=20)
        self.e_busy = ttk.Combobox(win, width=17)
        self.e_photo = Entry(win, width=20)

        self.initUI(win)

    def initUI(self, win):
        PageController(win, 'SELECT COUNT(*) FROM rooms', self.room_table, self.command)
        Search(win, self.command, self.room_table, self.fieldsRU, self.fieldsEN)

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

        self.room_table.bind('<ButtonRelease>', self.fillField)

        cur.execute('SELECT id, type FROM roomtype')
        self.e_type.configure(values=["{} - {}".format(*row) for row in cur.fetchall()])

        self.e_busy['values'] = ['Да', 'Нет']

        self.AddBtn['command'] = self.Add
        self.EditBtn['command'] = self.Update
        self.DeleteBtn['command'] = self.Delete
        self.ChoiceImage['command'] = self.Browse

    def create(self):
        cur.execute("SELECT * FROM rooms LIMIT 5 OFFSET 0")
        rows = cur.fetchall()
        for row in rows:
            self.room_table.insert("", "end", values=row)

        self.room_table.grid(row=0, column=1, columnspan=20, sticky='w')

        self.l_name.grid(row=3, column=1, sticky='w')
        self.l_type.grid(row=4, column=1, sticky='w')
        self.l_cost.grid(row=5, column=1, sticky='w')
        self.l_beds.grid(row=6, column=1, sticky='w')
        self.l_breakfast.grid(row=7, column=1, sticky='w')
        self.l_busy.grid(row=8, column=1, sticky='w')
        self.l_photo.grid(row=9, column=1, sticky='w')

        self.e_name.grid(row=3, column=2, sticky='w')
        self.e_type.grid(row=4, column=2, sticky='w')
        self.e_cost.grid(row=5, column=2, sticky='w')
        self.e_beds.grid(row=6, column=2, sticky='w')
        self.e_breakfast.grid(row=7, column=2, sticky='w')
        self.e_busy.grid(row=8, column=2, sticky='w')
        self.e_photo.grid(row=9, column=2, sticky='w')

        self.AddBtn.grid(row=10, column=2)
        self.EditBtn.grid(row=10, column=1)
        self.DeleteBtn.grid(row=11, column=1)
        self.ChoiceImage.grid(row=9, column=3)

    def Add(self):
        try:
            type = self.e_type.get().split(" - ")[0]
            busy = self.e_busy.selection_get()

            if busy == 'Да':
                busy = 1
            else:
                busy = 0

            command = "INSERT INTO rooms VALUES(Null, '{0}', {1}, {2}, {3}, {4}, {5}, '{6}')".format(
                self.e_name.get(), type, self.e_cost.get(),
                self.e_beds.get(), self.e_breakfast.get(), busy, self.e_photo.get()
            )
            cur.execute(command)
            conn.commit()

            self.room_table.delete(*self.room_table.get_children())

            cur.execute("SELECT * FROM rooms LIMIT 5 OFFSET 0")
            rows = cur.fetchall()
            for row in rows:
                self.room_table.insert("", "end", values=row)
        except:
            messagebox.showinfo('Ошибка', 'Не удалось добавить данные')

    def Update(self):
        try:
            type = self.e_type.get().split(" - ")[0]

            busy = self.e_busy.selection_get()

            if busy == 'Да':
                busy = 1
            else:
                busy = 0

            _id = self.room_table.item(self.room_table.selection(), 'values')[0]
            command = "UPDATE rooms SET " \
                      "name='{0}', type={1}, cost={2}, bed_count={3}, breakfast={4}, busy={5}, photo='{6}' WHERE id={7}".format(
                self.e_name.get(), type, self.e_cost.get(),
                self.e_beds.get(), self.e_breakfast.get(), busy, self.e_photo.get(), _id
            )
            cur.execute(command)

            self.room_table.delete(*self.room_table.get_children())

            cur.execute("SELECT * FROM rooms LIMIT 5 OFFSET 0")
            rows = cur.fetchall()
            for row in rows:
                self.room_table.insert("", "end", values=row)

        except:
            messagebox.showinfo('Ошибка', 'Не удалось обновить данные')
        conn.commit()

    def Delete(self):
        _id = self.room_table.item(self.room_table.selection(), 'values')[0]
        command = "DELETE FROM rooms WHERE id={0}".format(_id)
        try:
            cur.execute(command)

            cur.execute("SELECT * FROM rooms LIMIT 5 OFFSET 0")
            rows = cur.fetchall()
            for row in rows:
                self.room_table.insert("", "end", values=row)

        except:
            messagebox.showinfo('Ошибка', 'Не удалось обновить данные')
        conn.commit()

    def Browse(self):
        file = filedialog.askopenfilename()
        self.e_photo.delete(0, END)
        self.e_photo.insert(0, file)

    def fillField(self, event):
        try:
            self.e_name.delete(0, END)
            self.e_type.delete(0, END)
            self.e_cost.delete(0, END)
            self.e_beds.delete(0, END)
            self.e_breakfast.delete(0, END)
            self.e_busy.delete(0, END)
            self.e_photo.delete(0, END)

            _id = self.room_table.item(self.room_table.selection(), 'values')[0]
            list = cur.execute('SELECT * FROM rooms WHERE id={0}'.format(_id)).fetchone()

            self.e_name.insert(0, list[1])
            self.e_type.insert(0, list[2])
            self.e_cost.insert(0, list[3])
            self.e_beds.insert(0, list[4])
            self.e_breakfast.insert(0, list[5])
            self.e_busy.insert(0, list[6])
            self.e_photo.insert(0, list[7])
        except:
            pass