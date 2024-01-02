from ast import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #brute force method: time complexity O(n^2), space complexity 1
        #iterate through list twice and find an instance of duplicate
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        
        return False
        '''

        #hashmap method: time complexity O(n), space complexity n
        #start with an empty map. Start adding list elements to map.
        #if element is already in map, then duplicate exists.

        #hashmap (dictionary in python) has a lookup time of O(1)
        map = {}
        for num in nums: #n time complexity
            if num in map.keys(): #runs in constant time
                return True
            else:
                map[num] = num
        
        return False