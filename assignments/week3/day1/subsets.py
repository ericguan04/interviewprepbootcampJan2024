from ast import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #backtracking question: decision tree algorithm that explores all possibilities
        res = []

        subset = []
        #depth first search
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            #decision NOT to include nums[i]
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res