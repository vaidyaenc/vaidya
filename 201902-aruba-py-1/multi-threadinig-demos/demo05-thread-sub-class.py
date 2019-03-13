import threading  as t
import sys

class CountDownThread(t.Thread):
    def run(self):
        name=t.current_thread().name
        max=100
        while max>0:
            print('{} counts {}'.format(name,max))
            max-=1

        print('{} ends'.format(name))


def main(name,args):
    t1=CountDownThread(name='marker')
    t2=CountDownThread(name='seeker')

    t1.start() 
    t2.start()
    
    print('end of program')

if __name__=='__main__':
    main(sys.argv[0],sys.argv[1:])