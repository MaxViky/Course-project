import os
from tkinter import *
from tkinter import filedialog

from PIL import ImageTk, Image

from connection import cur, conn


class ClientInfo():
    def __init__(self, id, name, phone, passport, photo):
        self.win = Toplevel()
        self.win.geometry('400x500')

        self.photo = photo
        self.id = id

        self.l_name = Label(self.win, text='ФИО: ' + name)
        self.l_type = Label(self.win, text='Телефон: ' + phone)
        self.l_cost = Label(self.win, text='Паспорт: ' + passport)

        self.changePhoto = Button(self.win, text='...')

        self.canvas = Canvas(self.win, width=300, height=300)
        try:
            img = ImageTk.PhotoImage(Image.open(self.photo))
            self.canvas.create_image(0, 0, anchor='nw', image=img)
        except:
            pass
        self.create()

    def create(self):
        self.canvas.grid(row=1, column=0, rowspan=20)
        self.l_name.grid(row=1, column=1, sticky='w')
        self.l_type.grid(row=2, column=1, sticky='w')
        self.l_cost.grid(row=3, column=1, sticky='w')

        self.changePhoto['command'] = self.browse
        self.changePhoto.grid(row=4, column=1, sticky='w')
        self.win.mainloop()

    def browse(self):
        try:
            file = filedialog.askopenfilename()
            image = Image.open(file)
            imageName = os.path.basename(file)
            imagePath = 'Images/Clients/{0}'.format(imageName)
            image = image.resize((300, 200), Image.ANTIALIAS)

            image.save(imagePath, "JPEG")
            command = "UPDATE clients SET photo='{0}' WHERE id={1}".format(imagePath, self.id)
            cur.execute(command)
            conn.commit()
        except:
            pass
        self.win.update()

