from dateutil.parser import parse
from dateutil.relativedelta import *

from datetime import *
print "parse example"
print parse('Mon, 11 Jul 2011 10:01:56 +0200 (CEST)')
s = "Today is 25 of September of 2003, exactly at 10:49:41 with timezone -03:00."
print parse(s, fuzzy=True)


today = datetime.now()
print 20*"=="
print today # today
print today+relativedelta(months=+1) # Next month
print today+relativedelta(years=+1) # Next year
print today+relativedelta(months=+1, weeks=+1) # Next month, plus one week
print today+relativedelta(months=+1, weeks=+1, hour=10) # Next month, plus one week, at 10am
print today+relativedelta(years=+1,months=-1) # One month before one year

print 20*"++"
print today+relativedelta(weekday=FR) # Next friday
print today+relativedelta(days=+1,weekday=SU(+1)) # Next sunday, but not today
print today+relativedelta(day=31, weekday=FR(-1)) # Last friday in this month


print "Calculate Age"
birthday = datetime(1971, 4, 5, 12, 0)
age = relativedelta(today, birthday)  # calculate age
print age
print "years: ",age.years," months: ",age.months," day: ",age.days
