from ast import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Time Complexity: O()
        #Space Complexity: O()
        
        #create max heap by negating the values
        max_heap = []
        for i in stones:
            max_heap.append(-i)

        #pass by reference: heapify the array
        heapq.heapify(max_heap)

        #while there are more than one elements in heap
        while len(max_heap) > 1:
            #pop root twice: these must be the max
            #negate values to turn back to normal
            x = -1*heapq.heappop(max_heap)
            y = -1*heapq.heappop(max_heap)

            #if not the same, subtract, negate, and push back to max heap
            if x != y:
                heapq.heappush(max_heap, -1*abs(x-y))
        
        #if max_heap checks if max_heap has elements
        if max_heap:
            #return the only element (don't forget to negate)
            return -1*max_heap[0]
        else:
            #no elements left, return 0
            return 0