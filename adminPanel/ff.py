from tkinter import *
from tkinter import *
from PIL import ImageTk, Image
import sqlite3 as sql

conn = sql.connect("hostels.db")
cur = conn.cursor()

cur.execute("SELECT photo from rooms WHERE id=1")
user = cur.fetchall()



root = Tk()
root.geometry('240x240')
canvas = Canvas(root, width=150, height=150)
canvas.pack()

pilImage = Image.open(user[0][0])
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(0, 0, image=image, anchor='nw')
root.mainloop()