import threading  as t
import sys

class CountDownThread(t.Thread):
    def __init__(self,max,min=0,**kwargs):
        name=kwargs.get('name')
        
        super(CountDownThread,self).__init__(name=name,kwargs=kwargs)
        
        self._max=max
        self._min=min
        


    def run(self):
        name=t.current_thread().name
        max=self._max
        while max>=self._min:
            print('{} counts {}'.format(name,max))
            max-=1

        print('{} ends'.format(name))


def main(name,args):
    t1=CountDownThread(30,name='marker')
    t2=CountDownThread(50,30)

    t1.start() 
    t2.start()
    
    print('end of program')

if __name__=='__main__':
    main(sys.argv[0],sys.argv[1:])