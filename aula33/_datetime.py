from datetime import date, datetime

# basics datetime
print(dir(datetime))

# Datetime now
now = datetime.now()
print(now)

# Basic use Today
dt = datetime.today()
print(dt)

# day
print(dt.day)

# Month
print(dt.month)

# Year
print(dt.year)

# timetuple.tm_yday
print(dt.timetuple().tm_yday)

# timetuple.tm_isdst
print(dt.timetuple().tm_isdst)

# timetuple.tm_mday
print(dt.timetuple().tm_mday)

# strftime
print(dt.strftime('%d/%m/%Y :: %H:%M:%S'))

# Date
d = datetime.date(datetime(2022, 4, 23))
print(d)
d2 = date(2022, 1, 2)
print(d2)

# Datetime
dt1 = datetime(2022, 10, 20, 12, 34, 10, 345311)
print(dt1)
print(dt1.hour)
print(dt1.minute)
print(dt1.second)
print(dt1.microsecond)
