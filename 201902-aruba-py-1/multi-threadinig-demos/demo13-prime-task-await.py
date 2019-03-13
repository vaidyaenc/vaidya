import threading as t
from threadutils import Task
import primeutils
import sys
import time


    

def main(name,args):
    task1= Task(primeutils.prime_count,0,100) #sum 0-10
    task2= Task(primeutils.prime_count,0,100000) # 50-60

    print('waiting for tasks to finish')

    result1=task1.wait()

    print('prime_count(0,100) ={}'.format(result1))

    print('prime_count(0,100000) ={}'.format(task2.wait()))
    print('end of program')

if __name__=='__main__':
    main(sys.argv[0],sys.argv[1:])