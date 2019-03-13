import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def n():
	logging.debug('Starting')
	time.sleep(5)
	logging.debug('Exiting')

def d():
    logging.debug('Starting')
    time.sleep(10)
    logging.debug('Exiting')

if __name__ == '__main__':

	n = threading.Thread(name='non-daemon', target=n)

	d = threading.Thread(name='daemon', target=d)
	d.setDaemon(True)

	d.start()
	n.start()

	print('main waiting for non-daemon thread...')
	#d.join()
	n.join()

	print('main ends...')