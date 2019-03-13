import threading
import time



def f(id):
    print ('thread #{} starts'.format(id))
    time.sleep(3) # suspends execution for 3 seconds
    print('thread #{} stops'.format(id))
    return

if __name__ == '__main__':
    for i in range(1,4): # 1 , 2 ,3
        t = threading.Thread(target=f, args=(i,))
        t.start()

    print('all threads started')