import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def importantTask():
    logging.debug('Starting')
    time.sleep(5)
    logging.debug('Exiting')

def nonImportantTask():
    logging.debug('Starting')
    time.sleep(10)
    logging.debug('Exiting')

if __name__ == '__main__':

    n = threading.Thread(name='non-daemon', target=importantTask)

    d = threading.Thread(name='daemon', target=nonImportantTask)
    d.setDaemon(True)

    d.start()
    n.start()
    print('waiting for non-daemon thread to finish ...')