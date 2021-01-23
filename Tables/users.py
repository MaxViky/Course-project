from tkinter import *
from tkinter import ttk

from UI import UI
from connection import cur


class Users:
    def __init__(self, win):
        self.command = 'SELECT id, username, role FROM users'
        self.users_table = ttk.Treeview(win, height=10)

        self.fieldsRU = ['Имя', 'Права']
        self.fieldsEN = ['username', 'role']

        self.initUI(win)

    def initUI(self, win):
        UI(win, self.command, 'SELECT COUNT(*) FROM users', self.users_table, self.fieldsRU, self.fieldsEN)

        cur.execute("SELECT * FROM users LIMIT 5 OFFSET 0")
        rows = cur.fetchall()
        for row in rows:
            self.users_table.insert("", "end", values=row)

        self.users_table["columns"] = ("1", "2", "3")
        self.users_table["show"] = 'headings'

        self.users_table.column("1", width=50)
        self.users_table.column("2", width=100)
        self.users_table.column("3", width=50)

        self.users_table.heading("1", text="Ид")
        self.users_table.heading("2", text="Имя")
        self.users_table.heading("3", text="Права")

    def create(self):
        self.users_table.grid(row=0, column=1, columnspan=20, sticky='w')
