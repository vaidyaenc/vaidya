import threading as t
import sys

class CountDownTask:
    def __init__(self, max,min=0,name=None):
        self._min=min
        self._max=max
        self._name=name
        self._thread=t.Thread(target=self.count_down,name=name)
        self._thread.start()

    def count_down(self):
        name=self._name if self._name!=None else t.current_thread().name
        print('{}:starts'.format(name))
        count=self._max
        while count>=self._min:
            print('{}: counts {}'.format(name,count))
            count-=1

        print('{}: ends'.format(name))




def main(name,args):
    c1=CountDownTask(50,name='marker')
    c2=CountDownTask(50,30)
    print('end of program')

if __name__=='__main__':
    main(sys.argv[0],sys.argv[1:])