from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # #recursive solution; Time Complexity: O(n), where n is the # of nodes in tree
        #                      Space Complexity O(1)
        # if not root:
        #     return 0

        # #base case is 1
        # #as we go deeper in the tree, we keep track of how deep it is.
        # #we simply use the side which is larger
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


        #iterative dfs algorithm using stack data structure
        #Time Complexity: O(n) ; Space Complexity: O(1)
        #more efficient by implementing the stack directly in our code (take away overhead from recursion)

        #create stack that holds the root value and the current depth
        stack = [[root, 1]]
        res = 0

        #while the stack is not empty, meaning did not reach end of tree yet
        while stack:
            #pop the root and depth and save them into variables
            node, depth = stack.pop()

            #look at node and update max depth if necessary
            #keep appending until there is nothing left to append
            #eventually, the stack will be completely empty, but max is already recorded
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        
        #return max depth
        return res