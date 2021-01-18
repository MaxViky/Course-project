from tkinter import ttk
from tkinter import *

from PageController import PageController
from connection import cur


class Search:
    def __init__(self, win, query, count, table, fieldsRU, fieldsEN):
        self.win = win
        self.query = query
        self.table = table
        self.fieldsRU = fieldsRU
        self.fieldsEN = fieldsEN
        self.count = count

        self.field1 = ttk.Combobox(self.win, value=fieldsRU)
        self.field2 = ttk.Combobox(self.win, value=fieldsRU)

        self.str1 = ''
        self.str2 = ''

        self.e_search1 = Entry(self.win)
        self.e_search2 = Entry(self.win)

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
            for i in range(0, len(self.fieldsRU)):
                if self.field1.get() == self.fieldsRU[i]:
                    self.str1 = self.fieldsEN[i]
                if self.field2.get() == self.fieldsRU[i]:
                    self.str2 = self.fieldsEN[i]

            self.table.delete(*self.table.get_children())

            if self.str2 == '':
                self.query = self.query + ' WHERE [{0}] LIKE "%{1}%"'.format(self.str1, self.e_search1.get())

            elif self.str1 == '':
                self.query = self.query + ' WHERE [{0}] LIKE "%{1}%"'.format(self.str2, self.e_search2.get())
            else:
                self.query = self.query + ' WHERE [{0}] LIKE "%{1}%" AND [{2}] LIKE "%{3}%"'\
                    .format(self.str1, self.e_search1.get(), self.str2, self.e_search2.get())
            query = self.query

            PageController(self.win, self.count, self.table, query)
        except:
            pass
