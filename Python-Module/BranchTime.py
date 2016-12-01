'''Branch Time Program written w/Python 2.7
By Logan Boespflug
Created 11-30-2016
'''

from datetime import datetime
from datetime import timedelta
from datetime import time

print 'Headquarters in Portland, OR Pacific Time(UTC-8)'
ptime=datetime.now()
print 'Current time at Portland HQ'
print '{:%H:%M}'.format(ptime) #Breaks time to just hour and minutes
if int(ptime.hour)>9 and int(ptime.hour)<21:
    print 'Currently Open'
else:
    print 'Currently Closed'
print ' '
print 'Time in New York City Branch'
nytime=datetime.now()+timedelta(hours=3) #Timezone difference
print '{:%H:%M}'.format(nytime)
if int(nytime.hour)>9 and int(nytime.hour)<21:
    print 'Currently Open'
else:
    print 'Currently Closed'
print ' '
print 'Time in London Branch'
ltime=datetime.now()+timedelta(hours=8) #Timezone difference
print '{:%H:%M}'.format(ltime)
if int(ltime.hour)>9 and int(ltime.hour)<21:
    print 'Currently Open'
else:
    print 'Currently Closed'



