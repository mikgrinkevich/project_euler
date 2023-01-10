from datetime import date

def sundays(start,end):
    sundays = 0
    for year in range(start,end+1):
        for month in range(1,13):
            if date(year,month,1).weekday() == 6:
                sundays += 1
    return sundays

print(sundays(1901,2000))
