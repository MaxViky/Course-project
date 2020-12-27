from tkinter import *
from tkinter import messagebox
from AdminPanel import AdminMenu
from connection import *
from authorization.regForm import Reg

blue = '#42AAE8'
white = 'White'


class Login:
    def __init__(self):
        self.window = Tk()
        self.window.title("Авторизация")
        self.window.geometry('450x200')
        self.window["bg"] = blue
        self.l_name = Label(self.window, text="Отель 'Виктория'", font=('Comic Sans MS', 24), bg=blue, fg=white)
        self.l_username = Label(self.window, text='Логин:', font=('Comic Sans MS', 18), bg=blue, fg=white)
        self.l_password = Label(self.window, text='Пароль:', font=('Comic Sans MS', 18), bg=blue, fg=white)
        self.e_username = Entry(self.window, font=('Comic Sans MS', 18))
        self.e_password = Entry(self.window, font=('Comic Sans MS', 18), show="*")
        self.btnEnter = Button(self.window, text='Войти', font=('Comic Sans MS', 12))
        self.btnReg = Button(self.window, text='Зарегистрироваться', font=('Comic Sans MS', 12))
        self.btnEnter['command'] = self.Enter
        self.btnReg['command'] = self.Reg

    def Create(self):
        self.l_name.grid(row=0, column=1, columnspan=3)
        self.l_username.grid(row=1, column=0)
        self.l_password.grid(row=2, column=0)
        self.e_username.grid(row=1, column=1, columnspan=2)
        self.e_password.grid(row=2, column=1, columnspan=2)
        self.btnEnter.grid(row=3, column=1)
        self.btnReg.grid(row=3, column=2)
        self.window.mainloop()

    def Enter(self):
        username = str(self.e_username.get())
        password = str(self.e_password.get())
        cur.execute("SELECT username, password, role FROM users WHERE username='{0}' AND password='{1}'"
                    .format(username, password))
        user = cur.fetchall()
        if not user:
            messagebox.showinfo('Ошибка', 'Неверный логин или пароль.')
        else:
            adminPanel = AdminMenu()

    def Reg(self):
        reg = Reg()
        reg.Create()
