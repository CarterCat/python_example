##

from datetime import datetime

dt = datetime.now()

dt = datetime.utcnow()

f"{dt.year}-{dt.month}-{dt.day}"

ts = dt.timestamp()

datetime.fromtimestamp(ts)

datetime.utcfromtimestamp(ts)

##

from datetime import timedelta

dt = datetime.now()

dt + timedelta(days=1, hours=12)

##

import time

time.sleep(5)

##

import arrow

t = arrow.now()

arrow.utcnow()

arrow.get("1991-10-25 11:11:11")

arrow.get('2013-05-11T21:23:58.970460+07:00')


t.shift(hours=-1)

t.shift(weeks=+2)

t.floor("hour")

t.ceil("hour")

t.timestamp

arrow.get(t.timestamp)

t.year
t.month
t.day
t.hour
t.minute
t.second

t.datetime # -> datetime.datetime

t.date() # -> datetime.date

t.time() # -> datetime.time

t.format()

t.format('YYYY-MM-DD')

t.format('YYYY-MM-DD HH:mm:ssZZ')

t.humanize()

t.humanize(locale="zh")