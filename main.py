from authorization.loginForm import Login

win = Login()
win.Create()
win.btnEnter['command'] = win.Enter
win.btnReg['command'] = win.Reg
win.window.mainloop()