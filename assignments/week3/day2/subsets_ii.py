from ast import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #hint: same exact solution as the original subset problem 
        #but you have to tweak the solution
        #introduce the notion of pruning: eliminating subtrees from the implicit tree

        power_set = []
        #sort the array: adjacent indicies will have similar subtrees
        #allows us to find duplicates because they must be next to each other
        nums.sort()

        def backtrack(i, sub_set):
            #once the final level is hit
            if i == len(nums):
                power_set.append(sub_set[::])
                return

            #case where we add ith element (left)
            sub_set.append(nums[i])
            backtrack(i+1, sub_set)

            #case where we don't add ith element (right)
            sub_set.pop()
            
            #skip over any duplicates. This is where the pruning happens
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1

            backtrack(i+1, sub_set)
        
        backtrack(0,[])
        return power_set