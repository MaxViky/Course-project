import sqlite3 as sql
from tkinter import ttk, messagebox, filedialog
from tkinter import *
from UI import UI
from connection import *


class Clients:
    def __init__(self, win):
        self.command = 'SELECT * FROM clients'
        self.client_table = ttk.Treeview(win, height=10)

        self.fieldsRU = ['ФИО', 'Телефон', 'Паспорт']
        self.fieldsEN = ['name', 'phone', 'passport']

        self.AddBtn = Button(win, text='Добавить')
        self.EditBtn = Button(win, text='Редактировать', width=15)
        self.DeleteBtn = Button(win, text='Удалить', width=15)
        self.ChoiceImage = Button(win, text='...', width=5)

        self.l_name = Label(win, text="ФИО", justify=RIGHT)
        self.l_phone = Label(win, text="Телефон")
        self.l_passport = Label(win, text="Паспорт")
        self.l_photo = Label(win, text="Фото")

        self.e_name = Entry(win, width=20)

        phone = StringVar()
        phone.trace('w', lambda name, index, mode, s=phone: self.phoneMask(s))

        self.e_phone = Entry(win, width=20, textvariable=phone)

        passport = StringVar()
        passport.trace('w', lambda name, index, mode, s=passport: self.passportMask(s))

        self.e_passport = Entry(win, width=20, textvariable=passport)

        self.e_photo = Entry(win, width=20)
        self.initUI(win)

    def initUI(self, win):
        UI(win, self.command, 'SELECT COUNT(*) FROM clients', self.client_table, self.fieldsRU, self.fieldsEN)

        cur.execute("SELECT * FROM clients LIMIT 5 OFFSET 0")
        rows = cur.fetchall()
        for row in rows:
            self.client_table.insert("", "end", values=row)
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

        self.client_table.bind('<ButtonRelease>', self.fillField)

        self.AddBtn['command'] = self.Add
        self.EditBtn['command'] = self.Update
        self.DeleteBtn['command'] = self.Delete
        self.ChoiceImage['command'] = self.Browse

    def create(self):

        self.client_table.grid(row=0, column=1, columnspan=20, sticky='w')

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

    def Add(self):
        try:
            command = "INSERT INTO clients VALUES(Null, '{0}', '{1}', '{2}', '{3}')".format(
                self.e_name.get(), self.e_phone.get(), self.e_passport.get(), self.e_photo.get()
            )
            cur.execute(command)
            conn.commit()

            self.client_table.delete(*self.client_table.get_children())
            cur.execute("SELECT * FROM clients LIMIT 5 OFFSET 0")
            rows = cur.fetchall()
            for row in rows:
                self.client_table.insert("", "end", values=row)
        except:
            messagebox.showinfo('Ошибка', 'Не удалось добавить данные')

    def Update(self):
        _id = self.client_table.item(self.client_table.selection(), 'values')[0]
        command = "UPDATE clients SET "\
                  "name='{0}', phone='{1}', passport='{2}', photo='{3}' WHERE id={4}".format(
            self.e_name.get(), self.e_phone.get(), self.e_passport.get(), self.e_photo.get(), _id
        )
        try:
            cur.execute(command)
            conn.commit()

            self.client_table.delete(*self.client_table.get_children())
            cur.execute("SELECT * FROM clients LIMIT 5 OFFSET 0")
            rows = cur.fetchall()
            for row in rows:
                self.client_table.insert("", "end", values=row)

        except:
            messagebox.showinfo('Ошибка', 'Не удалось обновить данные')
        conn.commit()

    def Delete(self):
        answer = messagebox.askyesno(
            title="Удаление",
            message="Удалить клиента?")
        if answer:
            _id = self.client_table.item(self.client_table.selection(), 'values')[0]
            command = "DELETE FROM clients WHERE id={0}".format(_id)
            try:
                cur.execute(command)
                conn.commit()

                self.client_table.delete(*self.client_table.get_children())

                cur.execute("SELECT * FROM clients LIMIT 5 OFFSET 0")
                rows = cur.fetchall()
                for row in rows:
                    self.client_table.insert("", "end", values=row)
            except:
                messagebox.showinfo('Ошибка', 'Не удалось обновить данные')

    def Browse(self):
        file = filedialog.askopenfilename()
        self.e_photo.delete(0, END)
        self.e_photo.insert(0, file)

    def phoneMask(self, argument):
        string = argument.get()
        if len(string) == 1:
            self.e_phone.insert(END, '(')
            self.e_phone.insert(0, '+')
        if len(string) == 6:
            self.e_phone.insert(END, ')-')
        if len(string) == 11:
            self.e_phone.insert(END, '-')
        if len(string) == 14:
            self.e_phone.insert(END, '-')
        if len(string) >= 17:
            self.e_phone.delete(17, END)

    def passportMask(self, argument):
        string = argument.get()
        if len(string) == 4:
            self.e_passport.insert(END, ' ')
        if len(string) >= 11:
            self.e_passport.delete(11, END)
            # +7(937)-251-12-24

    def fillField(self, event):
        try:
            self.e_name.delete(0, END)
            self.e_phone.delete(0, END)
            self.e_passport.delete(0, END)
            self.e_photo.delete(0, END)

            _id = self.client_table.item(self.client_table.selection(), 'values')[0]
            cur.execute('SELECT * FROM clients WHERE id={0}'.format(_id)).fetchone()
            list = cur.fetchone()
            self.e_name.insert(0, list[1])
            self.e_phone.insert(0, list[2])
            self.e_passport.insert(0, list[3])
            self.e_photo.insert(0, list[4])
        except:
            pass

