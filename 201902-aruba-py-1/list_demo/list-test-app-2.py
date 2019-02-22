from utils.linkedlist import LinkedList

def main():
    l=LinkedList()
    for i in range(1,11):
        l.add(i)

    print(l.info())

    i=0
    while i<l.size():
        print(l.get(i))
        l.set(i,i*100)
        i+=1

    print(l.info())

    print('l.remove(3)={}'.format(l.remove(3))) #300
    print('l.remove(5)={}'.format(l.remove(5))) #600
    print('l.remove()={}'.format(l.remove())) #900

    print(l.info())

    while l.size()>0:
        print('removing {}'.format(l.remove()))

if __name__=='__main__':
    main()