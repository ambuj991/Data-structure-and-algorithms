# overlapping  lists (not cyclic)
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def insert_end(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(new_data)
    
    def overlapping(self,L2):
        L1,L2=self.head,L2.head
        
        def len(L):
            c=0
            while L:
                L=L.next
                c=c+1
            return c
        L1_len,L2_len=len(L1),len(L2)
        if L1_len > L2_len:
            L1,L2=L2,L1

        for _ in range(abs(L1_len-L2_len)):
            L2=L2.next
        while L2 and L1 and L1 is not L2:
            L1,L2=L1.next,L2.next
        return L1
    
    

l=LinkedList()
l2=LinkedList()

l.insert_end(1)
l.insert_end(2)
l.insert_end(3)
l.insert_end(4)

l2.insert_end(7)
l2.insert_end(3)
l2.insert_end(4)

l.print_list()
print('\n')
l2.print_list()
print(l.overlapping(l2))