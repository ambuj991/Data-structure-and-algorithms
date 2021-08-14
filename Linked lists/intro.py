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
    
    def length_list(self):
        c=0
        cur=self.head
        if cur is None:
            return 0
        while cur:
            c=c+1
            cur=cur.next
        print(c,"is the length")
        return
    def insert_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("Previous node is absent!")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def insert_end(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(new_data)

    
    def reverse(self):
        if self.head is None:
            return None
        curr = self.head
        prev = None
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        self.head = prev

    def remove(self,data):
        if self.head is None:
            return
        curr=self.head
        while curr.next:
            if curr.next.data==data:
                curr.next=curr.next.next
                break
            else: curr=curr.next
    def remove_duplicates(self):
        
        cur = self.head
        prev = None

        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                # Remove node:
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before.
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def rotate(self, k):
        p = self.head 
        q = self.head 
        prev = None
        
        count = 0
        
        while p and count < k:
            prev = p
            p = p.next 
            q = q.next 
            count += 1
        p = prev
        while q:
            prev = q 
            q = q.next 
        q = prev 

        q.next = self.head 
        self.head = p.next 
        p.next = None
        

        
llist = LinkedList()
llist.insert_end(1)
llist.insert_end(2)
llist.insert_end(3)
llist.insert_after(llist.head.next.next, 4)
llist.insert_end(5)
llist.insert_front(0)
llist.reverse()
llist.remove(3)
llist.length_list()
llist.print_list()
a=int(input())
llist.rotate(a)
llist.print_list()