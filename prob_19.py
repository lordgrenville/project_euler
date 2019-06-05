first = datetime.date(1901, 1, 1)
last = datetime.date(2000, 12, 31)
count = 0
while first < last:
    if first.day == 1:
        if first.weekday() == 6:
            count += 1
    first += datetime.timedelta(days=1)
print(count)
