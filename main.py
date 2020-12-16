from loginForm import *
from regForm import *


reg = Reg
win = Login()
win.Create()
win.btnEnter['command'] = win.Enter
win.btnReg['command'] = win.Reg
win.window.mainloop()