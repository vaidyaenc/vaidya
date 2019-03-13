import threading as t
from threadutils import Task
import sys
import time


def sum(min,max=None):
    if max==None:
        min,max=0,min
    
    total=0
    
    for value in range(min,max+1):
        total+=value
        time.sleep(0.1)

    print('debug:{}'.format(total))
    return total        

def main(name,args):
    task1= Task(sum,10) #sum 0-10
    task2= Task(sum,50,60) # 50-60

    print('end of program')

if __name__=='__main__':
    main(sys.argv[0],sys.argv[1:])