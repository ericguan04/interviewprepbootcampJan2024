from ast import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        #sorting solution
        nums.sort()
        return nums[len(nums)-k]
        '''

        #time complexity: O(klogn)
        #space complexity: O(n)

        #create maxheap by negating minheap
        nums_maxheap=[]
        for num in nums:
            nums_maxheap.append(-num)

        #heapify function: parameter is array I want to convert
        #pass by reference
        heapq.heapify(nums_maxheap)

        #continuously pop the root, which is always the max until kth is reached
        for i in range(k-1):
            heapq.heappop(nums_maxheap)

        #top of max heap is now the kth largest
        #negate it to turn it back to normal
        return -1*heapq.heappop(nums_maxheap)