from datetime import datetime

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
