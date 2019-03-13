import threading
import time

def f1():
    print (threading.currentThread().getName(), 'Starting')
    time.sleep(1)
    print (threading.currentThread().getName(), 'Exiting')

class T2(threading.Thread):
    def __init__(self,name):
        super().__init__(name=name)

    def run(self):
        print (threading.currentThread().getName(), 'Starting')
        time.sleep(1)
        print (threading.currentThread().getName(), 'Exiting')



t1 = threading.Thread(target=f1) # use default name
t2 = threading.Thread(name='marker', target=f1)
t3 = T2('seeker')

t1.start()
t2.start()
t3.start()