from ast import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force solution: time solution O(n^2)
        #space complexity O(1) OR O(c)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return i,j
        

        #hashmap solution: time complexity O(n)
        #space complexity O(n)
        map = {}

        #enumerate method in python gives us the index and value
        #same thing can be achieved with range() function
        for i, num in enumerate(nums):
            #for a given value, the solution is the complement
            #if complement is in map, then those two indexes are the solution (only 1 solution)
            if target - num in map:
                sol = [i, map[target - num]]
                return sol
            #if not, add the value as key and index as value
            else:
                map[num] = i
