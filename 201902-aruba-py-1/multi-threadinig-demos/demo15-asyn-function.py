from  primeutils import is_prime
from threadutils import asynchronous

@asynchronous
def prime_count(min,max=None):
    if max==None:
        min,max=2,min
    primes=0
    for n in range(min,max):
        if is_prime(n):
            primes+=1

    return primes

import sys

def main(name,args):
    c1=prime_count(2,100)
    c2=prime_count(2,100000)
    c3=prime_count(2,500)
    
    print('waiting for results...')

    print(c1.result)
    print(c2.result)
    print(c3.result)



if __name__=='__main__':
    main(sys.argv[0],sys.argv[1:])

    
     