from datetime import date, timedelta

first, last = date(1901, 1, 1), date(2000, 12, 31)
count = 0
while first < last:
    if first.day == 1 and first.weekday() == 6:
        count += 1
    first += timedelta(days=1)
print(count)