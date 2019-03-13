

def greet(name):
    
    return 'Hello {}. Welcome to Python'.format(name)

def main(*args):
    result=greet(args[1])
    print(result)


if __name__=='__main__':
    import sys
    main(*sys.argv)

