

import utils.console as c

from computations.primes import prime_range

from computations.maths import sum,average

def main():

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


if __name__=='__main__':
    main()

