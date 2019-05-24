import time

# following time method returns the current time in seconds from the epoch time of OS
# for windows it is 1 January 1601
# for unix it is 1 January 1970
print(time.time())
#Output: 1558627115.478033

# above time is not human readable
print(time.ctime())
# Output: Thu May 23 12:06:49 2019

# to calculate the time that a iteration took


def send_emails():
    for i in range(100000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)
# Output: 0.0030083656311035156
