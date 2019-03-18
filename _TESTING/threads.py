import threading
import time
import random

#####################################################################
class T(threading.Thread):
    name  = 'thread'
    count = 10
    def set(self, name, count):
        self.name  = name
        self.count = count
    def run(self):
        for i in range(self.count):
            print 'Running thread %s, count %04d out of %04d' % (self.name, i+1, self.count)
            time.sleep(0.1)
#####################################################################

t_array = []

for i in range(0, 50):
    t = T()
    t.set('thread_%04d' % (i+1), int(random.random()*15.0))
    t_array.append(t)
    time.sleep(random.random())
    t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    t.join()

print 'END!'
