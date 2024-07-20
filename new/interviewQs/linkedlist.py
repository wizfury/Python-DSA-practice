from random import randint
class Node:
    def __init__(self,value=None):
        self.data = value
        self.prev = None
        self.next = None
        
    def __str__(self) -> str:
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None
        
    def __str__(self):
        values = [str(x.data) for x in self]
        return '->'.join(values)
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node=node.next 
        return count
    
    def add(self,val):
        if self.head is None:
            newNode = Node(val)
            self.head = newNode
            self.tail = newNode
            
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        return self.tail
    
    def generate(self,n,minval,maxval):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(minval,maxval))
        return self

        