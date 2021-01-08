from tkinter import ttk
from tkinter import *

from connection import cur


class Search:
    def __init__(self, win, query, table, command1):
        self.query = query
        self.table = table
        self.field1 = ttk.Combobox(win, value=command1)
        # self.field2 = ttk.Combobox(win, value=command2)

        self.e_search1 = Entry(win)
        self.e_search2 = Entry(win)

        self.e_search1.bind('<Key>', self.search)
        self.Create()

    def Create(self):
        self.field1.grid(row=3, column=4)
        # self.field2.grid(row=4, column=4)
        self.e_search1.grid(row=3, column=5, columnspan=4)
        self.e_search2.grid(row=4, column=5, columnspan=4)

    def search(self, event):
        self.table.delete(*self.table.get_children())
        cur.execute(self.query + ' WHERE [{0}] LIKE "%{1}%" LIMIT 5 OFFSET 0'.format(self.field1.get(), self.e_search1.get()))
        rows = cur.fetchall()
        for row in rows:
            self.table.insert("", "end", values=row)
