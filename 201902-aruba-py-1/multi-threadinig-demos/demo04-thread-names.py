import threading  as t
import sys

def count_down():
    name=t.current_thread().name
    max=100
    while max>0:
        print('{} counts {}'.format(name,max))
        max-=1

    print('{} ends'.format(name))


def main(name,args):
    t1=t.Thread(target=count_down,name='marker')
    t2=t.Thread(target=count_down,name='seeker')

    t1.start() 
    t2.start()
    
    print('end of program')

if __name__=='__main__':
    main(sys.argv[0],sys.argv[1:])