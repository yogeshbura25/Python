from datetime import datetime, timedelta
a = input()
date_format = "%b %d %Y %I:%M %p"
x=datetime.strptime(a,date_format)
y=datetime(2024, 1, 1)
dt = y - x 
h = dt.days*24+dt.seconds//3600
m=(dt.seconds//60)%60 
print("{} hours {} minutes".format(h,m))