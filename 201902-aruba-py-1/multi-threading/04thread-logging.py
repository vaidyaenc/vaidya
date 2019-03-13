import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                      format='[%(levelname)s] (%(threadName)-9s) %(message)s')



def f1():
    logging.info ( 'Starting')
    time.sleep(1)
    logging.info ( 'Exiting')

class T2(threading.Thread):
    def __init__(self,name):
        super().__init__(name=name)

    def run(self):
        logging.info ( 'Starting')
        time.sleep(1)
        logging.info ( 'Exiting')



t1 = threading.Thread(target=f1) # use default name
t2 = threading.Thread(name='marker', target=f1)
t3 = T2('seeker')

t1.start()
t2.start()
t3.start()