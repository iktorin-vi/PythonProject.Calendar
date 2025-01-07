import calendar

year = 2025
month = 4
day = 7
print(calendar.month(year, month))

if month<10 and day<10:
    print("0"+f"{day}."+"0" + f"{month}.{year}")
else:
    print(f"{day}.{month}.{year}")