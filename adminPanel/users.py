from tkinter import *
from tkinter import ttk

from PageController import PageController
from Search import Search
from Sorting import Sorting
from connection import cur


class Users:
    def __init__(self, win):
        self.command = 'SELECT username, role FROM users'
        self.users_table = ttk.Treeview(win, height=10)

        self.fieldsRU = ['Имя', 'Права']
        self.fieldsEN = ['username', 'role']

        self.initUI(win)

    def initUI(self, win):
        cur.execute("SELECT * FROM users LIMIT 5 OFFSET 0")
        rows = cur.fetchall()
        for row in rows:
            self.users_table.insert("", "end", values=row)

        PageController(win, 'SELECT COUNT(*) FROM users', self.users_table, self.command)
        Search(win, self.command, self.users_table, self.fieldsRU, self.fieldsEN)
        Sorting(win, self.command, self.users_table, self.fieldsRU, self.fieldsEN)

        self.users_table["columns"] = ("1", "2", "3")
        self.users_table["show"] = 'headings'

        self.users_table.column("2", width=200)
        self.users_table.column("3", width=100)

        self.users_table.heading("2", text="Имя")
        self.users_table.heading("3", text="Права")

    def create(self):
        self.users_table.grid(row=0, column=1, columnspan=20, sticky='w')
