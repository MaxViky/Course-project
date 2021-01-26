import sqlite3 as sql

from tkinter import messagebox

import mysql.connector
from mysql.connector import errorcode, Error

conn = mysql.connector.connect(host='localhost', database='hostel', user='root', password='1234')

cur = conn.cursor()

if conn.is_connected():
        print('Connected to MySQL database')
else:
    messagebox.showinfo('Ошибка', 'Не удалось соединиться с базой данных.')
