from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Time Complexity: O(length of shorter list)
        #Space Complexity: O(1)

        merge = ListNode()
        tail = merge 
        # tail allows us to traverse through the linked list
        # at the end, tail will be pointing at the end of the linked list
        # we can then just return merge.next since merge is still pointing at the beginning
        # .next is to account for the empty node in the beginning

        #while neither are null checks if they still have values
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1 # next has to point to a linked list node, not a value
                #update list1 to point to next value
                list1 = list1.next
            else:
                tail.next = list2
                #update list2 to point to next value
                list2 = list2.next
            #update tail to point to the next node to continue adding nodes
            tail = tail.next
        
        # once one of them reaches null, we simply append the remaining nodes
        # of the list that still has values
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return merge.next