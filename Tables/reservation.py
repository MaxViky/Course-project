
from pydoc import Doc
from tkinter import ttk, messagebox, filedialog
from tkinter import *

from docxtpl import DocxTemplate
from tkcalendar import DateEntry

from datetime import  *

from UI import UI
from connection import *


class Reservation:
    def __init__(self, win):

        self.command = "SELECT reservation.id, client, name, room, arrival_date, departure_date, payment_day, amount " \
                       "FROM reservation INNER JOIN clients on reservation.client = clients.id"
        self.reservation_table = ttk.Treeview(win, height=10)

        self.fieldsRU = ['Клиент', 'Комната', 'Дата прибытия', 'Дата отбытия', 'Дата оплаты', 'Итог']
        self.fieldsEN = ['name', 'room', 'arrival_date', 'departure_date', 'payment_day', 'amount']

        self.amount = 0

        self.AddBtn = Button(win, text='Добавить')
        self.EditBtn = Button(win, text='Редактировать', width=15)
        self.DeleteBtn = Button(win, text='Удалить', width=15)
        self.Docbtn = Button(win, text='Квитанция', width=10)

        self.l_client = Label(win, text="Клиент", justify=RIGHT)
        self.l_room = Label(win, text="Комната")
        self.l_dateArrive = Label(win, text="Дата прибытия")
        self.l_dateDepart = Label(win, text="Дата отбытия")
        self.l_datePay = Label(win, text="Дата оплаты")

        self.l_amount = Label(win, text="Итоговая стоимость: {0}".format(self.amount))

        cur.execute('SELECT id, name FROM clients')
        self.e_client = ttk.Combobox(win, width=30, values=["{} - {}".format(*row) for row in cur.fetchall()])

        cur.execute('SELECT id, name FROM rooms WHERE busy like 0')
        self.e_room = ttk.Combobox(win, width=30, values=["{} - {}".format(*row) for row in cur.fetchall()])

        self.e_dateArrive = DateEntry(win, width=20, date_pattern="YYYY-mm-dd", borderwidth=2)
        self.e_dateDepart = DateEntry(win, width=20, date_pattern="YYYY-mm-dd", borderwidth=2)
        self.e_datePay = DateEntry(win, width=20, date_pattern="YYYY-mm-dd", borderwidth=2)
        self.initUI(win)

    def initUI(self, win):
        UI(win, self.command, 'SELECT COUNT(*) FROM reservation', self.reservation_table, self.fieldsRU, self.fieldsEN)

        self.reservation_table["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
        self.reservation_table["show"] = 'headings'

        self.reservation_table.column("1", width=50)
        self.reservation_table.column("2", width=50)
        self.reservation_table.column("3", width=200)
        self.reservation_table.column("4", width=50)
        self.reservation_table.column("5", width=100)
        self.reservation_table.column("6", width=100)
        self.reservation_table.column("7", width=100)
        self.reservation_table.column("8", width=100)

        self.reservation_table.heading("1", text="Ид")
        self.reservation_table.heading("2", text="Клиент")
        self.reservation_table.heading("3", text="ФИО")
        self.reservation_table.heading("4", text="Комната")
        self.reservation_table.heading("5", text="Дата прибытия")
        self.reservation_table.heading("6", text="Дата отбытия")
        self.reservation_table.heading("7", text="Дата оплаты")
        self.reservation_table.heading("8", text="Итог")

        self.reservation_table.bind('<ButtonRelease>', self.fillField)
        self.e_room.bind('<<ComboboxSelected>>', self.choiceRoom)
        self.e_dateArrive.bind('<<DateEntrySelected>>', self.choiceRoom)
        self.e_dateDepart.bind('<<DateEntrySelected>>', self.choiceRoom)
        self.e_datePay.bind('<<DateEntrySelected>>', self.choiceRoom)

        self.Docbtn['command'] = self.CreateReceipt
        self.AddBtn['command'] = self.Add
        self.EditBtn['command'] = self.Update
        self.DeleteBtn['command'] = self.Delete

    def create(self):
        cur.execute("SELECT reservation.id, client, name, room, arrival_date, departure_date, payment_day, amount "
                    "FROM reservation INNER JOIN clients on reservation.client = clients.id LIMIT 5 OFFSET 0")
        rows = cur.fetchall()
        for row in rows:
            self.reservation_table.insert("", "end", values=row)

        self.reservation_table.grid(row=0, column=1, columnspan=20)

        self.l_client.grid(row=3, column=1, sticky='w')
        self.l_room.grid(row=4, column=1, sticky='w')
        self.l_dateArrive.grid(row=5, column=1, sticky='w')
        self.l_dateDepart.grid(row=6, column=1, sticky='w')
        self.l_datePay.grid(row=7, column=1, sticky='w')
        self.l_amount.grid(row=8, column=1, sticky='w')

        self.e_client.grid(row=3, column=2, sticky='w')
        self.e_room.grid(row=4, column=2, sticky='w')
        self.e_dateArrive.grid(row=5, column=2, sticky='w')
        self.e_dateDepart.grid(row=6, column=2, sticky='w')
        self.e_datePay.grid(row=7, column=2, sticky='w')

        self.AddBtn.grid(row=10, column=2)
        self.EditBtn.grid(row=10, column=1)
        self.DeleteBtn.grid(row=11, column=1)
        self.Docbtn.grid(row=7, column=3)

    def Add(self):
        client = self.e_client.get().split(" - ")[0]
        room = self.e_room.get().split(" - ")[0]

        now = datetime.now().date()

        if self.e_dateArrive.get_date() <= now <= self.e_dateDepart.get_date():
            cur.execute('UPDATE rooms SET busy = 1 WHERE id={0}'.format(room))
        else:
            cur.execute('UPDATE rooms SET busy = 0 WHERE id={0}'.format(room))
        conn.commit()

        if self.e_dateArrive.get_date() > self.e_dateDepart.get_date():
            messagebox.showinfo('Ошибка', 'Дата прибытия позже даты отбытия')
        elif self.e_dateArrive.get_date() > self.e_datePay.get_date() < self.e_dateDepart.get_date():
            messagebox.showinfo('Ошибка', 'Дата оплаты Должна быть в период снятия номера')
        else:
            try:
                command = "INSERT INTO reservation VALUES(Null, {0}, {1}, '{2}', '{3}', '{4}', {5})".format(
                    client, room, self.e_dateArrive.get(),
                    self.e_dateDepart.get(), self.e_datePay.get(), self.amount
                )
                cur.execute(command)
                conn.commit()
                self.reservation_table.delete(*self.reservation_table.get_children())
                cur.execute("SELECT reservation.id, client, name, room, arrival_date, departure_date, payment_day, amount "
                            "FROM reservation INNER JOIN clients on reservation.client = clients.id LIMIT 5 OFFSET 0")
                rows = cur.fetchall()
                for row in rows:
                    self.reservation_table.insert("", "end", values=row)
            except:
                messagebox.showinfo('Ошибка', 'Не удалось добавить данные')

    def Update(self):
        if self.e_dateArrive.get_date() > self.e_dateDepart.get_date():
            messagebox.showinfo('Ошибка', 'Дата прибытия позже даты отбытия')
        elif self.e_dateArrive.get_date() > self.e_datePay.get_date() < self.e_dateDepart.get_date():
            messagebox.showinfo('Ошибка', 'Дата оплаты Должна быть в период снятия номера')
        else:
            try:
                _id = self.reservation_table.item(self.reservation_table.selection(), 'values')[0]
                client = self.e_client.get().split(" - ")[0]
                room = self.e_room.get().split(" - ")[0]
                now = datetime.now().date()

                if self.e_dateArrive.get_date() <= now <= self.e_dateDepart.get_date():
                    cur.execute('UPDATE rooms SET busy = 1 WHERE id={0}'.format(room))
                else:
                    cur.execute('UPDATE rooms SET busy = 0 WHERE id={0}'.format(room))
                conn.commit()

                command = "UPDATE reservation SET " \
                          "client={0}, room={1}, arrival_date='{2}', departure_date='{3}', payment_day='{4}', amount={5}" \
                          " WHERE id={6}" \
                    .format(
                    client, room, self.e_dateArrive.get(),
                    self.e_dateDepart.get(), self.e_datePay.get(), self.amount, _id
                )
                cur.execute(command)
                conn.commit()

                self.reservation_table.delete(*self.reservation_table.get_children())

                cur.execute(
                    "SELECT reservation.id, client, name, room, arrival_date, departure_date, payment_day, amount "
                    "FROM reservation INNER JOIN clients on reservation.client = clients.id LIMIT 5 OFFSET 0")
                rows = cur.fetchall()
                for row in rows:
                    self.reservation_table.insert("", "end", values=row)

            except:
                messagebox.showinfo('Ошибка', 'Не удалось обновить данные')

    def Delete(self):
        room = self.e_room.get().split(" - ")[0]
        answer = messagebox.askyesno(
            title="Удаление",
            message="Удалить бронь?")
        if answer:
            _id = self.reservation_table.item(self.reservation_table.selection(), 'values')[0]
            command = "DELETE FROM reservation WHERE id={0}".format(_id)
            try:
                cur.execute(command)

                cur.execute('UPDATE rooms SET busy = 0 WHERE id={0}'.format(room))
                conn.commit()

                self.reservation_table.delete(*self.reservation_table.get_children())
                cur.execute(
                    "SELECT reservation.id, client, name, room, arrival_date, departure_date, payment_day, amount "
                    "FROM reservation INNER JOIN clients on reservation.client = clients.id LIMIT 5 OFFSET 0")
                rows = cur.fetchall()

                for row in rows:
                    self.reservation_table.insert("", "end", values=row)
            except:
                messagebox.showinfo('Ошибка', 'Не удалось обновить данные')
            conn.commit()

    def fillField(self, event):
        try:
            self.e_client.delete(0, END)
            self.e_room.delete(0, END)
            self.e_dateArrive.delete(0, END)
            self.e_dateDepart.delete(0, END)
            self.e_datePay.delete(0, END)

            _id = self.reservation_table.item(self.reservation_table.selection(), 'values')[0]
            cur.execute('SELECT * FROM reservation WHERE id={0}'.format(_id))
            list = cur.fetchone()
            self.e_client.insert(0, list[1])
            self.e_room.insert(0, list[2])
            self.e_dateArrive.insert(0, list[3])
            self.e_dateDepart.insert(0, list[4])
            self.e_datePay.insert(0, list[5])
            self.choiceRoom(event)
        except:
            pass

    def choiceRoom(self, event):
        self.amount = 0
        _id = self.e_room.get().split(" - ")[0]
        cur.execute("SELECT cost, breakfast FROM rooms WHERE id={0}".format(_id))
        cost = cur.fetchone()

        self.amount = cost[0]+cost[1]

        d1 = self.e_dateArrive.get_date()
        d2 = self.e_dateDepart.get_date()
        difference = (d2 - d1).days
        if difference == 0:
            difference = 1
        cur.execute("SELECT discount FROM discounts WHERE id={0}".format(_id))
        discount = cur.fetchone()
        self.amount = self.amount * difference
        if not discount:
            self.l_amount['text'] = 'Итоговая стоимость: ' + str(self.amount)
        else:
            self.amount = self.amount - ((self.amount * difference) / 100 * discount[0])
            self.l_amount['text'] = 'Итоговая стоимость: {0}(Скидка {1}%)'.format(self.amount, discount[0])

    def CreateReceipt(self):
        _id = self.reservation_table.item(self.reservation_table.selection(), 'values')[0]

        Client_id = self.e_client.get().split(" - ")[0]

        cur.execute('SELECT name FROM clients WHERE id={0}'.format(Client_id))
        Client_name = cur.fetchone()[0]

        doc = DocxTemplate('Templates/Квитанция.docx')

        context = {'code': _id, 'id': Client_id, 'name': Client_name, 'room': self.e_room.get(),
                   'dateArrive': self.e_dateArrive.get(), 'dateDepart': self.e_dateDepart.get(), 'cost': self.amount}
        doc.render(context)
        doc.save('Documents/Квитанция №{0}.docx'.format(_id))
