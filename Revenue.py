from datetime import datetime
from docxtpl import DocxTemplate
from connection import cur


class Revenue:
    def MonthlyRevenue(self):
        month = datetime.now().month
        year = datetime.now().year
        cur.execute("SELECT date('now','start of month','+1 month','-1 day')")
        if month < 10:
            start_date = '{1}-0{0}-01'.format(month, year)
        else:
            start_date = '{1}-{0}-01'.format(month, year)
        end_date = cur.fetchone()[0]

        cur.execute("SELECT COUNT(client), SUM(amount) FROM reservation "
                    "WHERE date(payment_day) BETWEEN date('{0}') AND date('{1}')".format(start_date, end_date))
        data = cur.fetchone()
        count = data[0]
        amount = data[1]

        doc = DocxTemplate('Templates/Выручка.docx')

        context = {'code': month + year, 'start_date': start_date, 'end_date': end_date, 'count': count,
                   'amount': amount}
        doc.render(context)
        doc.save('Documents/Выписка №{0}{1}.docx'.format(month, year))