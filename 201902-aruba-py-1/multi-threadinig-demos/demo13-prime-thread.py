from threading import Thread
from primeutils import prime_count

import sys

def main(name,args):
    
    t1=Thread(target=prime_count,args=(2,100))
    t1.start()


    print('please wait...')
    while t1.isAlive():
        pass
    # I still have no way to get the prime_count result

if __name__=='__main__':
    main(sys.argv[0],sys.argv[1:])