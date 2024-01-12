# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from ast import List
from collections import deque
from typing import Optional

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs uses queue data structure
        #Time Complexity: O(n) where n is the number of nodes
        #Space Complexity: O(n)

        q = deque() #double ended queue; can pop from left and right
        
        #edge case
        if root:
            q.append(root)

        level_order=[]
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft() #from deque class; pop from left
                level.append(node.val) #add the value, not the node itself
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_order.append(level)
        
        return level_order