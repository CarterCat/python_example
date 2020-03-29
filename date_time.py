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
