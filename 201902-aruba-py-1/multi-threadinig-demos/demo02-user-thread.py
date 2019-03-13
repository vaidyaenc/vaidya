import threading  as t
import sys

def print_info():
    print('Current Thread is {}'.format(t.current_thread()))

def main(name,args):
    t1=t.Thread(target=print_info)
    t1.start() # interally call print_info() on a new thread
    print_info() #calls print_info() on the main thread
    print('end of program')

if __name__=='__main__':
    main(sys.argv[0],sys.argv[1:])