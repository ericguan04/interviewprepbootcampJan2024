from ast import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Two pointer method; similar to two_sum_2 question
        #Time Complexity:
        #Space Complexity:

        l, r = 0, len(height)-1

        #water area can be calculated using the smaller height and the width
        max_water = min(height[l], height[r]) * (r-l)
        
        #makes sure the pointers do not cross each other
        while l < r:
            #always move the pointer pointing to the lower line
            #we do this because we want to keep the largest height when minimizing the width
            #mathematically, since we are decreasing width, the only way to get a bigger max
            #is to increase the height
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
    
            #check if new area is greater and update if necessary
            if min(height[l], height[r]) * (r-l) > max_water:
                max_water = min(height[l], height[r]) * (r-l)
        
        return max_water