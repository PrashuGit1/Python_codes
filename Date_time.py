import datetime

# Current date and time
now = datetime.datetime.now()
print("Now:", now)

# Current date only
today = datetime.date.today()
print("Today:", today)

# Custom date
d = datetime.date(2023, 6, 7)
print("Custom Date:", d)

# Formatting date
print("Formatted:", now.strftime("%d-%m-%Y %H:%M:%S"))
