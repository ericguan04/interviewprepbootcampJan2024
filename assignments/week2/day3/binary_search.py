from ast import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #important algorithm to know for interview questions
        #won't be asked explicitly, but will be expected to know
        #nums has to be sorted for binary search to be used
        
        start, end = 0, len(nums)-1

        while start <= end:
            mid = (start+end)//2 #integer division, includes floor operation

            if target > nums[mid]:
                start=mid+1

            elif target < nums[mid]:
                end=mid-1

            else:
                return mid
        
        return -1