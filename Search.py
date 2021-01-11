from tkinter import ttk
from tkinter import *

from connection import cur


class Search:
    def __init__(self, win, query, table, filedsRU, filedsEN):
        self.query = query
        self.table = table
        self.filedsRU = filedsRU
        self.filedsEN = filedsEN

        self.field1 = ttk.Combobox(win, value=filedsRU)
        self.field2 = ttk.Combobox(win, value=filedsRU)

        self.str1 = ''
        self.str2 = ''

        self.e_search1 = Entry(win)
        self.e_search2 = Entry(win)

        self.e_search1.bind('<KeyRelease>', self.search)
        self.e_search2.bind('<KeyRelease>', self.search)

        self.Create()

    def Create(self):
        self.field1.grid(row=3, column=4)
        self.field2.grid(row=4, column=4)
        self.e_search1.grid(row=3, column=5, columnspan=4)
        self.e_search2.grid(row=4, column=5, columnspan=4)

    def search(self, event):
        try:
            for i in range(0, len(self.filedsRU)):
                if self.field1.get() == self.filedsRU[i]:
                    self.str1 = self.filedsEN[i]
                if self.field2.get() == self.filedsRU[i]:
                    self.str2 = self.filedsEN[i]

            self.table.delete(*self.table.get_children())
            if self.str2 == '':
                cur.execute(self.query + ' WHERE [{0}] LIKE "%{1}%" LIMIT 5 OFFSET 0'.format(self.str1, self.e_search1.get()))
                rows = cur.fetchall()
                for row in rows:
                    self.table.insert("", "end", values=row)
            elif self.str1 == '':
                cur.execute(self.query + ' WHERE [{0}] LIKE "%{1}%" LIMIT 5 OFFSET 0'.format(self.str2, self.e_search2.get()))
                rows = cur.fetchall()
                for row in rows:
                    self.table.insert("", "end", values=row)
            else:
                cur.execute(self.query + ' WHERE [{0}] LIKE "%{1}%" AND [{2}] LIKE "%{3}%" LIMIT 5 OFFSET 0'
                            .format(self.str1, self.e_search1.get(), self.str2, self.e_search2.get()))
                rows = cur.fetchall()
                for row in rows:
                    self.table.insert("", "end", values=row)
        except:
            pass
