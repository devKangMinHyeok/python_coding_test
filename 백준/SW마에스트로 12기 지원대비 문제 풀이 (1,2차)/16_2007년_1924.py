x, y = map(int, input().split())
max_date = [-1,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0
month = 1
date = 1

while not (x == month and y == date):
    day = (day + 1) % 7
    if max_date[month] == date:
        month += 1
        date = 1
    else:
        date += 1

if day == 0: print("MON")
elif day == 1: print("TUE")
elif day == 2: print("WED")
elif day == 3: print("THU")
elif day == 4: print("FRI")
elif day == 5: print("SAT")
elif day == 6: print("SUN")
