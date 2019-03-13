import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                      format='[%(levelname)s] (%(threadName)-9s) %(message)s')


def slow():
    logger=logging.getLogger()
    logger.info('started')
    time.sleep(5)
    logger.info('ends')


def main():
    logger=logging.getLogger()
    logger.info('main starts')
    t=threading.Thread(target=slow,name='slow')
    t.start()
    logger.info('main ends')

if __name__=='__main__':
    main()
