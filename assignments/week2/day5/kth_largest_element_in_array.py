from ast import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        #sorting solution
        nums.sort()
        return nums[len(nums)-k]
        '''

        #heap solution
        #convert array to a max heap
        #not sure how this solution works, so learn heaps next class
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]