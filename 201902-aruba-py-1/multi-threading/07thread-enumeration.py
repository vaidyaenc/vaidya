import threading
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)



def f(sleepTime,isDaemon):
    t = threading.currentThread()
    #t.setDaemon(isDaemon)
    #r = random.randint(1,10)
    logging.debug('sleeping %s', sleepTime)
    time.sleep(sleepTime)
    logging.debug('ending')
    return

if __name__ == '__main__':
    thread_info={5:False, 3:False, 10:True}

    for i in thread_info.items():
        t = threading.Thread(target=f,args=(i[0],i[1]))
        t.setDaemon(i[1])
        t.start()

    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread or  t.isDaemon():
            continue # don't wait for main thread and daemon threads
        logging.debug('joining %s', t.getName())
        t.join()