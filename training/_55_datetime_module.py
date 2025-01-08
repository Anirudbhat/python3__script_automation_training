#!/usr/bin/python3
#strftime.org is the website to check the details of strftime(string format time) 

import datetime
import pytz

#print(dir(datetime))
print("Local date & time:",datetime.datetime.now())        #This will give present date and time
print("Local date & time:",datetime.datetime.today())      #This will give present date and time too
#Although now() & today() function gives same result without any input, using now() function we can get time of other timezones too.
gmt = pytz.timezone('Europe/London')
print("London date & time:",datetime.datetime.now(gmt))
print(f"Type() of gmt variable is:{type(gmt)}")
print(f"current year:{datetime.datetime.now().year}")
print(f"current month:{datetime.datetime.now().month}")
print(f"current date:{datetime.datetime.now().day}")
print(f"hour:{datetime.datetime.now().hour}")
print(f"minute:{datetime.datetime.now().minute}")
print(f'year-month-date:{datetime.datetime.now().strftime("%y-%m-%d")}')
print(f'year-month-date:{datetime.datetime.now().strftime("%Y-%m-%d")}') #Capital y inside the bracket gives full year

print(f'unix timestamp:{datetime.datetime.fromtimestamp(2983749)}')
