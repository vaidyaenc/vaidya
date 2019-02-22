import shapes.circle as circle
import shapes.triangle as triangle

def main():
    t1=triangle.Triangle()
    t2=triangle.Triangle()

    print('type(t1)={}'.format(type(t1)))
    print('type(t2)={}'.format(type(t2)))

    print('id(t1)={}'.format(id(t1)))
    print('id(t2)={}'.format(id(t2)))

    

if __name__=='__main__':
    main()

    