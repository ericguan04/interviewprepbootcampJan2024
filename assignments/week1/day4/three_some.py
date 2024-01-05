from ast import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity: O(n^2)
        # We want to sort the array then use two pointers algorithm
        # This is an extension of two_sum_2
        # We first have a set value, then traverse the remaining list (this becomes a two_sum problem)
        # 

        nums.sort()
        sol = []

        for i, num in enumerate(nums):
            #skip duplicate values
            if i > 0 and num == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1
            while l < r:
                sum = num + nums[l] + nums[r]
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    sol.append([num, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return sol