import threading
import time

class MyThread(threading.Thread):
    def __init__(self,id):
        super().__init__()
        self._id=id

    def run(self):
        print ('thread function {}'.format(self._id))
        time.sleep(1)
        print('thread stops {}'.format(self._id))
        

if __name__ == '__main__':
    for i in range(1,4):
        t = MyThread(i)
        t.start()