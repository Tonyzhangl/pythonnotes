#coding=utf-8

import threading, time, sys

class test(threading.Thread):

    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print "%s delay for %s" %(self.name, self.delay)
        time.sleep(self.delay)
        c = 0
        while True:
            print "This is thread %s on line %s" % (self.name, c)
            c = c+1
            if c == 3:
                print "End of thread %s" % self.name
                break

t1 = test('T1', 2)
t2 = test('T2', 2)
t1.start()
print 'Wait t1 to end'
t1.join()
t2.start()
print 'End of main'
