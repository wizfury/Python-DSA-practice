from linkedlist import LinkedList

def partition(ll,x):
    curnode = ll.head
    ll.tail = ll.head
    
    while curnode:
        newNode = curnode.next
        curnode.next = None
        if curnode.data < x:
            curnode.next = ll.head
            ll.head = curnode
        else:
            ll.tail.next = curnode
            ll.tail = curnode
        curnode = curnode.next
            
        