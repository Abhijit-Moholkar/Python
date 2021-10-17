from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)

string_data = given_date.strftime('%Y-%M-%D %H:%M:%S')
print(string_data)
