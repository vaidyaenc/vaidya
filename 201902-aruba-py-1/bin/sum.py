#! py -3

def main(name,*args):
    result=0
    for value in args:
        result+=float(value)
        #print(value)

    print ('result',result)

if __name__=='__main__':
    import sys
    main(*sys.argv)