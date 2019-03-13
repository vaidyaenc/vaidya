from threading import Thread,current_thread


def count_down(max,min=0):
    name=current_thread().name
    print('{} starts...'.format(name))
    count=max
    while count>=min:
        print('{} counts {}'.format(name,count))
        count-=1

    print('{} stops'.format(name))


    

import sys

def main(name,args):
    
    c1=Thread(target=count_down,args=[100],name='critcal100')
    nc1=Thread(target=count_down,args=[2000],daemon=True, name='non-critical2000')
    c2=Thread(target=count_down,args=[200], name='critical200')

    c1.start()
    nc1.start()
    c2.start()

    c1.join()
    c2.join()
    nc1.join()

    print('end of program')
    

if __name__=='__main__':
    main(sys.argv[0],sys.argv[1:])