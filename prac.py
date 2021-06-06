import math

#print(math.pi) # 3.1415
#print(math.sqrt(100)) #10
#print(math.floor(9.23)) #9
#print(math.ceil(9.23))# 10
#print(math.gcd(9,3)) # 3
#print(math.fabs(-12))#12.0

from math import sqrt, fabs

#print(sqrt(25)) # 5.0
#print(fabs(-9)) #9.0

# Displaying the content of module
import multiplier as m

#print(m.__name__) # mod_n
#print(m)
#print(dir(m))

everything = dir(math)
#print(everything)# every math func and attribute

#print(help(math.sqrt))

import random as r

#print(random.randint(1,6))#return any num from 1 to 6
# another eg

#print(r.randint(0,100))
lst = ['parrot', 'dog', 'hen', 'lion', 'tiger', 'cat']
#print(r.choice(lst))#choise any from lst

r.shuffle(lst)
#lst.sort()
print(lst)

# another eg
a = [[x] for x in range(15)]

#print(a) # original lst
#print()
#r.shuffle(a)
#print(a) # shuffle lst
#print()
#a.sort()
#print(a)# sorted lst after shuffle

# another func call randrange

#for i in range(3):
#	print(r.randrange(0,50,2))

# universal import
from math import *

#print(sqrt(25))

#importing several modules at once

import math, multiplier

s = math.sqrt(25)
y = int(s)
x = r.randint(1,3)
#print(multiplier.multiply(y,x))

import time

x = time.localtime()
#print(x)
#print(x.tm_year)
#print(x.tm_mon)
#print(x.tm_mday)
#print(x.tm_hour)
#print(x.tm_min)
#print(x.tm_sec)
#print(x.tm_wday)
#print(x.tm_yday)
#print(x.tm_isdst)

#print(time.asctime(time.localtime()))
import calendar as c

july_cal = c.month(2016,7)
#print('Current cal of:')
#print(july_cal)

#time modules are as follow
#time.altzone
#time.asctime
#time.localtime
#time.ctime
#time.clock
#time.gmtime
#time.mktime
#time.sleep
#time.strptime(sring[, format='%a%b %d %H:%S:%Y'])
#time.time
#time.tzset

#print(c.calendar(2016,w=2,l=1,c=6))
#print(c.firstweekday())
#print(c.isleap(2016))
#print(c.isleap(2014))
#print(c.leapdays(2010,2016))
#print(c.leapdays(2010,2020))
#print(c.month(2016,7,w=2,l=1))
#print(c.monthrange(2016,7))
#print(c.monthcalendar(2020,1))

#print(c.prmonth(2020,1,w=2,l=1))
#print(c.weekday(2020,1,30))
#print(c.calendar(2016,w=2,l=1,c=15))

import calendar

#print('The 4th month of 1997 is: ')
#calendar.prmonth(1997, 4, 2, 1)
#calendar.setfirstweekday(3)
#print('\r')
#print('The new week day number is',calendar.firstweekday())

import datetime as d

x = d.datetime.now()
#x = d.date(2021,1,7)
#print(x)
#print(x.year, x.month)
#print(x.min)

from time import strftime

#print(strftime('%Y-%m-%d %H:%M:%S'))
l = [1,2,3]
print(list(enumerate(l)))




