import threading  as t
import sys

def count_down(max,**kwargs):
    name=t.current_thread().name
    min=kwargs.get('min',0)
    #max=100
    while max>=min:
        print('{} counts {}'.format(name,max))
        max-=1

    print('{} ends'.format(name))


def main(name,args):
    t1=t.Thread(target=count_down,name='marker',args=(20,))
    t2=t.Thread(target=count_down,name='seeker',args=[50],kwargs={'min':30})

    t1.start() 
    t2.start()
    
    print('end of program')

if __name__=='__main__':
    main(sys.argv[0],sys.argv[1:])