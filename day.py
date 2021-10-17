# day extraction using datetime module

from datetime import datetime

given_date = datetime(2020, 7, 26)

print(given_date.today().weekday())

print(given_date.strftime('%A'))

###########################################################
# Day extraction using calender module

import calendar
from datetime import datetime

given_date = datetime(2020, 7, 26)
weekday = calendar.day_name[given_date.weekday()]
print(weekday)
