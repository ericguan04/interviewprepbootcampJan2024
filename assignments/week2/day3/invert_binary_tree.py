from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #use recursion
        '''
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        '''

        #end case: once there are no more roots (pass the leaves), return None
        if not root:
            return
        
        #this is how to perform swaps in python
        root.left, root.right = root.right, root.left
        #goes deeper into the tree
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root