#coding=utf-8
import threading, time

def myfunc(a, delay):
    print "I will calculate square of %s after delay for %s" % (a ,delay)
    time.sleep(delay)
    print "calculate begins..."
    result = a*a
    print result
    return result


t1 = threading.Thread(target=myfunc, args=(2, 5))
t2 = threading.Thread(target=myfunc, args=(6, 8))

print t1.isDaemon()
print t2.isDaemon()

t2.setDaemon(True)
t1.start()
t2.start()
