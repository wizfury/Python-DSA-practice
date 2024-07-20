from linkedlist import LinkedList

def removeDups(ll):
    if ll.head is None:
        return
    else:
        currentnode = ll.head
        visited = set([currentnode.data])
        while currentnode.next:
            if currentnode.next.data in visited:
                currentnode.next = currentnode.next.next
            else:
                visited.add(currentnode.next.data)
                currentnode = currentnode.next 
        return ll
                
customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
removeDups(customLL)
print(customLL)