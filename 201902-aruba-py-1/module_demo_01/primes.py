

def is_prime(number):
    if number<0:number*=-1
    
    if number<2:return False

    for test in range(2,number):
        if number%test==0:
            return False

    return True


def prime_range(min,max=None):
    primes=list()
    if max==None:
            min,max=2,min
    for n in range(min,max):
        if is_prime(n):
            primes.append(n)
    return primes



def main():
        print('testing primes module')
        print('module name {}'.format(__name__))
        test_data={1:False,2:True,-5:False,0:False,-9:False,13:True}
        for (number,expectedResult)  in test_data.items():
                actualResult=is_prime(number)
                if actualResult!=expectedResult:
                        print('FAILED for {}\t expected:{}\tfound={}'.format(number,expectedResult,actualResult))

        print(prime_range(10,20))
        print(prime_range(0,100))
        print(prime_range(10))
        print('='*20)


if __name__=='__main__':
        main()
