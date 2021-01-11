import math
from tkinter import *
from connection import cur


class PageController:
    def __init__(self, win, count, table, command):
        self.count = count
        self.table = table
        self.command = command

        self.note = 0
        self.page = 1

        self.pageCount = math.ceil(cur.execute(self.count).fetchone()[0] / 5)
        self.nextPage = Button(win, text='->')
        self.previousPage = Button(win, text='<-')
        self.pageInfo = Label(win)

        self.pageInfo['text'] = '{0}-{1}'.format(self.page, self.pageCount)

        self.InitUI()

    def InitUI(self):
        self.nextPage['command'] = self.Next
        self.previousPage['command'] = self.Previous

        self.nextPage.grid(row=1, column=5)
        self.pageInfo.grid(row=1, column=4)
        self.previousPage.grid(row=1, column=3)

    def Next(self):
        if self.page < self.pageCount:
            self.page += 1
            self.note += 5

            self.pageInfo['text'] = '{0}-{1}'.format(self.page, self.pageCount)

            self.table.delete(*self.table.get_children())
            cur.execute(self.command + ' LIMIT 5 OFFSET {0}'.format(self.note))
            rows = cur.fetchall()
            for row in rows:
                self.table.insert("", "end", values=row)

    def Previous(self):
        if self.page > 1:
            self.page -= 1
            self.note -= 5

            self.pageInfo['text'] = '{0}-{1}'.format(self.page, self.pageCount)

            self.table.delete(*self.table.get_children())
            cur.execute(self.command + ' LIMIT 5 OFFSET {0}'.format(self.note))
            rows = cur.fetchall()
            for row in rows:
                self.table.insert("", "end", values=row)