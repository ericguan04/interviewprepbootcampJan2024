from ast import List
from cmath import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #time complexity: O(n + klogn)
        #space complexity: O(n)

        #use min heap; list of lists
        min_heap = []
        for i, pt in enumerate(points):
            #for the heap, add the distance and the index
            min_heap.append([sqrt(pt[0]**2 + pt[1]**2), i])
        
        #heapify function will sort heap of lists with first element in each list
        #in this case, it will sort by min distance
        heapq.heapify(min_heap)

        #return k number of min distance points
        k_pts=[]
        for i in range(k):
            #pop returns the current min: contains [distance,index]
            elem = heapq.heappop(min_heap)
            #elem[1] is the index of the min point. get it from points
            k_pts.append(points[elem[1]])

        return k_pts