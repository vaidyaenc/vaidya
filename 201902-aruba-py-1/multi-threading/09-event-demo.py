import threading as t
import time 
import threadutils as u


def wait_function(event,timeOut=None):
    u.print_thread('waiting for event')
    event.wait(timeOut) #wait for ever if timeOut is None
    u.print_thread('ends')

def main():
    event=t.Event()
    t1=t.Thread(target=wait_function, args=(event,),name='wait1')
    t2=t.Thread(target=wait_function, args=(event,30), name='wait for 30 sec')

    

    t1.start()
    t2.start()

    x=input('hit enter to send signal')
    u.print_thread('sending signal')
    event.set() #send singal to waiting threads
    u.print_thread('stops')
    
    
if __name__=='__main__':
    main()


