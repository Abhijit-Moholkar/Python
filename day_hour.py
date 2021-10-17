from datetime import datetime,timedelta

given_date = datetime(2020, 3, 22, 10, 0, 0)
resultant_date = given_date + timedelta(days = 7,hours=12)
print(resultant_date)
