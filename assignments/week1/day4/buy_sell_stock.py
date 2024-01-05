from ast import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Two Pointer / Sliding Window Problem
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # The idea is to have two points l (buy) and r (sell)
        # We move left forward until we find r > l (buy low, sell higher)
        # If this continues to be the case, then we keep track of max profit.
        # If there is some r smaller than l, then change l to r (new minimum)
        # Algorithm continues until list is completed

        l,r = 0,1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l=r
            r+=1

        return max_profit