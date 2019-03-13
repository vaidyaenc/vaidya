import threading as t
import sys

class CountDownTask:
    def __init__(self, max,min=0,name=None):
        self._min=min
        self._max=max
        self._name=name
        

    def count_down(self):
        name=self._name if self._name!=None else t.current_thread().name
        print('{}:starts'.format(name))
        count=self._max
        while count>=self._min:
            print('{}: counts {}'.format(name,count))
            count-=1

        print('{}: ends'.format(name))

    @staticmethod
    def start_async(max,min=0,name=None):
        task=CountDownTask(max,min,name)
        t1=t.Thread(target=task.count_down,name=name)
        t1.start()
        return t1



def main(name,args):
    t1=CountDownTask.start_async(50,name='marker')
    t2=CountDownTask.start_async(50,30)
    print('end of program')

if __name__=='__main__':
    main(sys.argv[0],sys.argv[1:])