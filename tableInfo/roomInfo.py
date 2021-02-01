import os
from tkinter import *
from tkinter import filedialog

from PIL import ImageTk, Image

from connection import cur, conn


class RoomInfo():
    def __init__(self, id, name, type, cost, beds, breakfast, busy, photo):
        self.win = Toplevel()
        self.win.geometry('400x500')

        self.photo = photo
        self.id = id

        if busy == 0:
            busy_str = 'Нет'
        else:
            busy_str = 'Да'

        self.l_name = Label(self.win, text='Название: ' + name)
        self.l_type = Label(self.win, text='Тип комнаты: ' + str(type))
        self.l_cost = Label(self.win, text='Стоимость: ' + str(cost))
        self.l_beds = Label(self.win, text='Кроватей: ' + str(beds))
        self.l_breakfast = Label(self.win, text='Завтрак: ' + str(breakfast))
        self.l_busy = Label(self.win, text='Занят: ' + busy_str)

        self.changePhoto = Button(self.win, text='...')

        self.canvas = Canvas(self.win, width=300, height=300)
        img = ImageTk.PhotoImage(Image.open(self.photo))
        self.canvas.create_image(0, 0, anchor='nw', image=img)

        self.create()

    def create(self):
        self.canvas.grid(row=1, column=0, rowspan=20)
        self.l_name.grid(row=1, column=1, sticky='w')
        self.l_type.grid(row=2, column=1, sticky='w')
        self.l_cost.grid(row=3, column=1, sticky='w')
        self.l_beds.grid(row=4, column=1, sticky='w')
        self.l_breakfast.grid(row=5, column=1, sticky='w')
        self.l_busy.grid(row=6, column=1, sticky='w')

        self.changePhoto['command'] = self.browse
        self.changePhoto.grid(row=7, column=1, sticky='w')
        self.win.mainloop()

    def browse(self):
        file = filedialog.askopenfilename()
        image = Image.open(file)
        imageName = os.path.basename(file)
        imagePath = 'Images/Hotels/{0}'.format(imageName)
        image = image.resize((300, 200), Image.ANTIALIAS)
        image.save(imagePath, "JPEG")

        command = "UPDATE rooms SET photo='{0}' WHERE id={1}".format(imagePath, self.id)
        cur.execute(command)
        conn.commit()
        self.win.update()
