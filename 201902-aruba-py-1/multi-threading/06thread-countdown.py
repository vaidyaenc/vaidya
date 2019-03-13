from threading import Thread,currentThread
from time import sleep

def print_thread(msg):
    print('[{}] {}'.format(currentThread().getName(),msg))

def count_down(max):
    try:
        print_thread('starts')
        while max>=0:
            print_thread('counts {}'.format(max))
            max-=1

        print_thread('ends')
    except:
        print_thread('interrupted')


def main():
    t1=Thread(target=count_down, args=(200,), name='one')
    t2=Thread(target=count_down, args=(1500,),name='two')
    #t2.setDaemon(True)
    t3=Thread(target=count_down, args=(150,),name='three')

    t1.start()
    t2.start()
    t3.start()
    print_thread('waiting for other to finish')
    t1.join()
    t2.join()
    t3.join()
    print_thread('main program ends')



if __name__=='__main__':
    main()