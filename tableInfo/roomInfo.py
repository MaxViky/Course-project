from tkinter import *

from PIL import ImageTk, Image


class RoomInfo():
    def __init__(self, name, type, cost, beds, breakfast, busy, photo):
        self.win = Tk()
        self.win.geometry('1000x1000')

        # self.canvas = Canvas(self.win, width=999, height=999)
        canvas = Canvas(self.win, height=400, width=700)

        Hotelimage = Image.open(photo)
        Hotelimage = ImageTk.PhotoImage(Hotelimage)
        image = canvas.create_image(0, 0, anchor='nw', image=Hotelimage)
        canvas.grid(row=0, column=0)

        self.l_name = Label(self.win, text=name)
        self.l_type = Label(self.win, text=type)
        self.l_cost = Label(self.win, text=cost)
        self.l_beds = Label(self.win, text=beds)
        self.l_breakfast = Label(self.win, text=breakfast)
        self.l_busy = Label(self.win, text=busy)

        self.create()


    def create(self):
        # self.canvas.grid(row=0, column=0)
        self.l_name.grid(row=3, column=1, sticky='w')
        self.l_type.grid(row=4, column=1, sticky='w')
        self.l_cost.grid(row=5, column=1, sticky='w')
        self.l_beds.grid(row=6, column=1, sticky='w')
        self.l_breakfast.grid(row=7, column=1, sticky='w')
        self.l_busy.grid(row=8, column=1, sticky='w')
        self.win.mainloop()

