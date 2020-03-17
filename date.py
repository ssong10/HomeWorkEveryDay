import datetime
def getDays(year,month):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if not year % 4 and(year % 100 or not year % 400):
        days[1] += 1
    return days[month -1]

today = datetime.datetime.today()
print(getDays(today.year,today.month))
