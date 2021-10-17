from datetime import datetime, timedelta
given_date = datetime(2020, 2, 22)

Days_to_subtract = 5
resultant_date = given_date - timedelta(days = Days_to_subtract)
print('Resulted date is',resultant_date)

weeks_to_subtract = 2
resultant_date = given_date - timedelta(weeks = weeks_to_subtract)
print('Resultant date is',resultant_date)
