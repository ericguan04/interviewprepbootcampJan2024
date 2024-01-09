from tkinter.tix import ListNoteBook
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNoteBook]) -> Optional[ListNode]:
        #Time Complexity: O(size of list)
        #Space Complexity: O(1)

        # We can use two pointers to solve this problem
        
        #prev points at null and curr points to the head
        prev, curr = None, head

        #this allows us to traverse the linked-list
        while curr:
            #use a temp variable to swap adjacent variable values
            temp = curr.next
            #need to study up on how the swapping works
            curr.next = prev
            prev = curr
            curr = temp
        #prev will be the new head so we can return this
        return prev