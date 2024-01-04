from ast import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointer method because list is sorted
        #Time Complexity: O(n)
        #Space Complexity: O(1)

        #standard two pointer method, start with l and r variables
        l = 0
        r = len(numbers)-1

        #idea: since the list is sorted: 
        #we know that, if the sum of start and end is larger than target, then we lower the end value to get a smaller sum.
        #otherwise, if the sum is too small, we can increase the start value to increase the sum.
        #since we are guaranteed a solution, eventually we will get two numbers that add up to target
        while l < r:
            if numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                #once sum equals target, return pointers + 1 (as requested by the problem)
                return l+1, r+1