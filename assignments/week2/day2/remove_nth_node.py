from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Time Complexity: O(n)
        #Space Complexity: 

        dummy = ListNode(0, head) #create a dummy node followed by given linked list
        #left is at dummy node and right is at the start of head
        l = dummy
        r = head

        #iterate through linked list until r is n steps ahead
        while n > 0 and r:
            r = r.next
            n-=1
        
        #iterate through linked list until r reaches the end
        #because it is n steps ahead, we are now on the node prev of what
        # we want to delete
        while r:
            l = l.next
            r = r.next
        
        #to delete the node, we reassign the pointer of the node to the next-next node
        l.next = l.next.next

        #dummy is still at the head, so we return dummy.next to remove dummy node
        return dummy.next