


class LinkedList:
    class Node:
        def __init__(self,value,next=None,previous=None):
            self.value=value
            self.next=next
            self.previous=previous


    def __init__(self):
        self._first=None
        self._last=None
        self._count=0

    
    def _old_add(self,value):
        new_node=LinkedList.Node(value)
        ptr=self._first
        if ptr==None: #list is empty
            self._first=new_node
        else:
            while ptr.next!=None:
                ptr=ptr.next
            new_node.previous=ptr
            ptr.next=new_node

    def add(self,value):
        new_node=LinkedList.Node(value)
        new_node.next=None
        new_node.previous=self._last

        if self._count==0: # list is empty
            self._first=new_node
        else:
            self._last.next=new_node

        self._last=new_node
        self._count+=1


    def size(self):
        return self._count

    def _locate(self,index=None):
        if index==None:
            index=self._count-1 #defaults to last node
        if index>=self._count:
            raise IndexError('invalid index {}'.format(index))

        if index==self._count-1: return self._last
        if index==0: return self._first

        ptr=self._first

        for i in range(0,index):
            ptr=ptr.next
        return ptr

    def get(self,index):        
        return self._locate(index).value

    def set(self,index,value):
        self._locate(index).value=value

    def remove(self,index=None):
        del_node=self._locate(index)
        # logic to remove the value from the list
        if del_node is self._first:
            self._first=del_node.next
        else:
            del_node.previous.next=del_node.next

        if del_node is self._last:
            self._last=del_node.previous
        else:
            del_node.next.previous=del_node.previous

        value=del_node.value
        del del_node
        self._count-=1
        return value

    def info(self):
        s='LinkedList(\t'
        ptr=self._first
        while ptr!=None:
            s+='{}\t'.format(ptr.value)
            ptr=ptr.next
        s+=")"
        return s