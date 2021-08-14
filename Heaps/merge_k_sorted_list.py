# merge k sorted linked lists
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr = []
        cur = beg = ListNode()
        while(l1):
            arr.append(l1.val)
            l1 = l1.next
        while(l2):
            arr.append(l2.val)
            l2 = l2.next
            
        arr = sorted(arr)
        for i in range(len(arr)):        
            cur.next = ListNode(arr[i])
            cur = cur.next
			
        return beg.next


# Time complexity : O(N\log k)O(Nlogk) where \text{k}k is the number of linked lists.

# The comparison cost will be reduced t O(\log k)O(logk) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1)time.
# There are N nodes in the final linked list.

# Space Complexity: O(n)