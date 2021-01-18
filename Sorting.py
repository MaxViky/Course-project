from tkinter import ttk, END

from PageController import PageController
from connection import cur


class Sorting():
    def __init__(self, win, query, count, table, fieldRU, fieldEN):
        self.win = win
        self.queryOld = query
        self.queryNew = query
        self.table = table
        self.fieldsRU = fieldRU
        self.fieldsEN = fieldEN
        self.count = count

        self.fieldsRU.append('Отмена')
        self.fieldsEN.append('Отмена')
        self.field = ''

        self.combosorting = ttk.Combobox(win, width=17, values=self.fieldsRU)
        self.combosorting.bind('<<ComboboxSelected>>', self.sort)

        self.Create()

    def Create(self):
        self.combosorting.grid(row=1, column=1)

    def sort(self, event):
        try:
            self.table.delete(*self.table.get_children())
            for i in range(0, len(self.fieldsRU)):
                if self.combosorting.get() == self.fieldsRU[i]:
                    self.field = self.fieldsEN[i]
            if self.field != 'Отмена':
                self.query = self.query + ' ORDER BY {0} '.format(self.field)
            else:
                cur.execute(self.query)
                self.combosorting.delete(0, END)

            query = self.query

            cur.execute(query + ' LIMIT 5 OFFSET 0')
            rows = cur.fetchall()
            for row in rows:
                self.table.insert("", "end", values=row)
        except:
            pass
        return query
