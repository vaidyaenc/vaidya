
'''
Take a min-max range
find average of all primes in the range
'''
import console
import maths
import primes

def main():
    repeat=True
    while repeat:
        lo=console.read_int('min?')
        hi=console.read_int('max?')

        primevalues= primes.prime_range(lo,hi)
        print('primes {}'.format(primevalues))

        avg=maths.average(*primevalues)

        print('average is {}'.format(avg))

        repeat=console.read_bool('repeat?')

main()


