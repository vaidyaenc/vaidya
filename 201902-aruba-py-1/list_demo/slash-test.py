

def f1(x,y,z):
    print('x={}\ty={}\tz={}'.format(x,y,z))

def f2(x,/,y,z):
    print('x={}\ty={}\tz={}'.format(x,y,z))

def main():
    f1(1,2,3) #fixed positions
    f1(z=4,x=1,y=9)
    f2(1,2,3)

if __name__=='__main__':
    main()