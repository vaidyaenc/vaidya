
'''
Take a min-max range
find average of all primes in the range
'''
# create object c for console module
import console as c 

# import selected elements from a module
# to global space
# this name may conflict with some other name
from primes import prime_range
# import everything from a module
# N O T  R E C O M M E N D E D
from maths import *

if __name__=='__main__':

    print('Welcome to primeapp')
    print('module name {}'.format(__name__))
    repeat=True
    while repeat:
        lo=c.read_int('min?')
        hi=c.read_int('max?')

        primevalues= prime_range(lo,hi)
        print('primes {}'.format(primevalues))

        s=sum(*primevalues)
        avg=average(*primevalues)

        print('average is {}'.format(avg))
        print('sum is {}'.format(s))

        repeat=c.read_bool('repeat?')
