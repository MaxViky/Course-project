from tkinter import *
import sqlite3 as sql
from tkinter import messagebox

import null

conn = sql.connect("database/hostels.db")
cur = conn.cursor()
blue = '#42AAE8'
white = 'White'


class Reg:
    def __init__(self):
        self.window = Tk()
        self.window.title("Регистрация")
        self.window.geometry('450x200')
        self.window["bg"] = blue
        self.l_name = Label(self.window, text="Отель 'Виктория'", font=('Comic Sans MS', 24), bg=blue, fg=white)
        self.l_username = Label(self.window, text='Логин:', font=('Comic Sans MS', 18), bg=blue, fg=white)
        self.l_password = Label(self.window, text='Пароль:', font=('Comic Sans MS', 18), bg=blue, fg=white)
        self.lc_password = Label(self.window, text='Повторите пароль:', font=('Comic Sans MS', 18), bg=blue, fg=white)
        self.e_username = Entry(self.window, font=('Comic Sans MS', 18))
        self.e_password = Entry(self.window, font=('Comic Sans MS', 18), show="*")
        self.ec_password = Entry(self.window, font=('Comic Sans MS', 18), show="*")
        self.btnReg = Button(self.window, text='Зарегистрироваться', font=('Comic Sans MS', 12))

    def registration(self):
        if len(self.e_username.get()) == 0 or len(self.e_password.get()) == 0:
            messagebox.showinfo('Ошибка', 'Пустое имя пользователя или пароль.')
        else:
            if self.ec_password.get() != self.e_password.get():
                messagebox.showinfo('Ошибка', 'Пароли не совпадают.')
            else:
                try:
                    cur.execute("INSERT INTO users(username, password, role) VALUES('{0}', '{1}', '{2}')"
                                .format(str(self.e_username.get()), str(self.ec_password.get()), 'manager'))
                    conn.commit()
                    messagebox.showinfo('Успешно', 'Вы зарегистрировались.')
                except:
                    messagebox.showinfo('Ошибка', 'Соединение с базой данных не установлено.')

    def Create(self):
        self.l_name.grid(row=0, column=1, columnspan=3)
        self.l_username.grid(row=1, column=0)
        self.l_password.grid(row=2, column=0)
        self.lc_password.grid(row=3, column=0)
        self.e_username.grid(row=1, column=1, columnspan=2)
        self.e_password.grid(row=2, column=1, columnspan=2)
        self.ec_password.grid(row=3, column=1, columnspan=2)
        self.btnReg.grid(row=4, column=1)
        self.btnReg.configure(command=self.registration)

