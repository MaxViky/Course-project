from datetime import datetime
from docxtpl import DocxTemplate
from connection import cur


class Revenue:
    def MonthlyRevenue(self):
        month = datetime.now().month
        year = datetime.now().year
        start_date = '{1}-{0}-01'.format(month, year)
        end_date = '{1}-{0}-31'.format(month, year)
        cur.execute('SELECT COUNT(client), SUM(amount) FROM reservation '
                    'WHERE payment_day >= {0} or payment_day <= {1}'.format(start_date, end_date))
        data = cur.fetchone()
        count = data[0]
        amount = data[1]

        doc = DocxTemplate('Templates/Выручка.docx')

        context = {'code': month + year, 'start_date': start_date, 'end_date': end_date, 'count': count,
                   'amount': amount}
        doc.render(context)
        doc.save('Documents/Выписка №{0}{1}.docx'.format(month, year))