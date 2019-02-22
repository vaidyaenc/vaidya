from utils.linkedlist import LinkedList

def main():
    l=LinkedList()
    l.add(10)
    l.add(2)
    l.add(15)

    print('size={}'.format(l.size()))
    print(l.info())

    c=0
    while c< l.size():
        print(l.get(c))
        c+=1

if __name__=='__main__':
    main()