class Solution:
    def climbStairs(self, n: int) -> int:
        #dynamic programming program
        #based on fibonacci sequence

        #time complexity: O(n)
        #space complexity: O(1)
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        
        return one