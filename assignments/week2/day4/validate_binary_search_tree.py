from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #use depth first search algorithm
        #root node can be any number (-inf to inf)
        #on the left side, num must be (-inf < child < root)
        #on the right side, num must be (5 < child < inf)
        #recursive solution is the best

        def valid(node, left, right):
            #base case
            if not node:
                return True

            #if not between boundaries, return false
            if not (node.val < right and node.val > left):
                return False

            #when checking the left, leave left bound the same and update right bound to parent
            #when checking the right, leave right bound the same and update left bound to parent
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float("-inf"), float("inf"))