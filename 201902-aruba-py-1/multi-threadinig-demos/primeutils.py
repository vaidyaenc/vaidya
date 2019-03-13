

def is_prime(number):
    if number<0:number*=-1
    if number<2:return False

    for value in range(2,number):
        if number%value==0:
            return False

    return True


def prime_count(min,max=None):
    if max==None:
        min,max=2,min
    primes=0
    for n in range(min,max):
        if is_prime(n):
            primes+=1

    print('debug: primes in range {}-{}={}'.format(min,max,primes))
    return primes

    
        