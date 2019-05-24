from datetime import datetime
#import datetime
import time
dt = datetime(2018, 1, 1)
print(dt)
dt = datetime.now()
print(dt)
# converts String to a DateTime object
dt = datetime.strptime('2018/01/01', '%Y/%m/%d')
print(dt)
dt = datetime.fromtimestamp(time.time())
print(dt)

print(f'{dt.year}/{dt.month}')
# converts a DateTime object into String
print(dt.strftime('%Y/%m'))
# Output:
# 2018-01-01 00:00:00
# 2019-05-23 14:09:33.675415
# 2018-01-01 00:00:00
# 2019-05-23 14:09:33.700483
# 2019/5
# 2019/05


# We can compare the date objects as well
