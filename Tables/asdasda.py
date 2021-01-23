
import math
from datetime import datetime

now = datetime.now().date().strftime('%d.%m.%Y')
my = '10.01.21'
if now > my:
    print(now)