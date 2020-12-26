import sqlite3 as sql

conn = sql.connect("database/hostels.db")
cur = conn.cursor()