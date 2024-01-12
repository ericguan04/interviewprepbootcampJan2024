from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #iterative solution using stacks
        
        #number of elements visited
        n=0
        stack = []
        cur = root #pointer at cur node

        while cur or stack:
            #go all the way left and add to stack
            while cur:
                stack.append(cur)
                cur = cur.left

            #cur will now be the latest node (aka the smallest)
            #add one to counter
            cur = stack.pop()
            n+=1
            if n == k:
                return cur.val
            #if not the kth node, go right
            #this algorithm allows us to traverse BST in order
            cur = cur.right