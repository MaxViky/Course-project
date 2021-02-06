import sqlite3 as sql

from tkinter import messagebox

import mysql.connector
from mysql.connector import errorcode, Error

try:
    conn = mysql.connector.connect(host='localhost', database='hostel', user='root', password='1234')
    cur = conn.cursor()
except:
    messagebox.showinfo('Ошибка', 'Не удалось соединиться с базой данных.')
