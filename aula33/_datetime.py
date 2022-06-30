import datetime

# basics datetime
print(dir(datetime))

# Basic use Today
dt = datetime.date.today()
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
