import math
from tkinter import ttk
from tkinter import *

from connection import cur


class UI():
    def __init__(self, win, command, count, table, fieldsRU, fieldsEN):
        self.count = count
        self.table = table
        self.command = command
        self.query = command
        self.fieldsRU = fieldsRU
        self.fieldsEN = fieldsEN

        self.fieldsRU.append('Отмена')
        self.fieldsEN.append('Отмена')
        self.combosorting = ttk.Combobox(win, width=17, values=self.fieldsRU)

        self.field1 = ttk.Combobox(win, value=self.fieldsRU)
        self.field2 = ttk.Combobox(win, value=self.fieldsRU)

        self.str1 = ''
        self.str2 = ''

        self.e_search1 = Entry(win)
        self.e_search2 = Entry(win)

        self.note = 0
        self.page = 1
        cur.execute(self.count)
        self.pageCount = math.ceil(cur.fetchone()[0]/5)
        self.nextPage = Button(win, text='->')
        self.previousPage = Button(win, text='<-')

        self.pageInfo = Label(win)

        self.CreateWidgets()
        self.PlaceWidget()

    def CreateWidgets(self):

        self.combosorting.bind('<<ComboboxSelected>>', self.sort)
        self.e_search1.bind('<KeyRelease>', self.search)
        self.e_search2.bind('<KeyRelease>', self.search)

        self.nextPage['command'] = self.Next
        self.previousPage['command'] = self.Previous
        self.pageInfo['text'] = '{0}-{1}'.format(self.page, self.pageCount)

    def PlaceWidget(self):
        self.combosorting.grid(row=1, column=1)

        self.field1.grid(row=3, column=4)
        self.field2.grid(row=4, column=4)
        self.e_search1.grid(row=3, column=5, columnspan=4)
        self.e_search2.grid(row=4, column=5, columnspan=4)

        self.nextPage.grid(row=1, column=5)
        self.pageInfo.grid(row=1, column=4)
        self.previousPage.grid(row=1, column=3)

    def sort(self, event):
        try:
            self.query = self.command
            self.table.delete(*self.table.get_children())
            for i in range(0, len(self.fieldsRU)):
                if self.combosorting.get() == self.fieldsRU[i]:
                    self.field = self.fieldsEN[i]
            if self.field != 'Отмена':
                self.query += ' ORDER BY {0}'.format(self.field)
            else:
                self.query = self.command

            cur.execute(self.query + ' LIMIT 5 OFFSET 0')
            rows = cur.fetchall()
            for row in rows:
                self.table.insert("", "end", values=row)
        except:
            pass

    def search(self, event):
        try:
            for i in range(0, len(self.fieldsRU)):
                if self.field1.get() == self.fieldsRU[i]:
                    self.str1 = self.fieldsEN[i]
                if self.field2.get() == self.fieldsRU[i]:
                    self.str2 = self.fieldsEN[i]

            self.table.delete(*self.table.get_children())

            self.query = self.command
            if self.str2 == '':
                self.query += ' WHERE {0} LIKE "%{1}%"'.format(self.str1, self.e_search1.get())
            elif self.str1 == '':
                self.query += ' WHERE {0} LIKE "%{1}%"'.format(self.str2, self.e_search2.get())
            else:
                self.query += ' WHERE {0} LIKE "%{1}%" AND [{2}] LIKE "%{3}%"'\
                            .format(self.str1, self.e_search1.get(), self.str2, self.e_search2.get())
            cur.execute(self.query + 'LIMIT 5 OFFSET 0')
            rows = cur.fetchall()
            for row in rows:
                self.table.insert("", "end", values=row)
        except:
            pass

    def Next(self):
        if self.page < self.pageCount:
            self.page += 1
            self.note += 5

            self.pageInfo['text'] = '{0}-{1}'.format(self.page, self.pageCount)

            self.table.delete(*self.table.get_children())
            cur.execute(self.query + ' LIMIT 5 OFFSET {0}'.format(self.note))
            rows = cur.fetchall()
            for row in rows:
                self.table.insert("", "end", values=row)

    def Previous(self):
        if self.page > 1:
            self.page -= 1
            self.note -= 5

            self.pageInfo['text'] = '{0}-{1}'.format(self.page, self.pageCount)

            self.table.delete(*self.table.get_children())
            cur.execute(self.query + ' LIMIT 5 OFFSET {0}'.format(self.note))
            rows = cur.fetchall()
            for row in rows:
                self.table.insert("", "end", values=row)