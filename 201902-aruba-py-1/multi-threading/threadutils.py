from threading import currentThread
def print_thread(msg):
    print('[{}] {}'.format(currentThread().getName(),msg))
