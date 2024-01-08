class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Brute Force Method
        #Time Complexity: O(n^2)
        #Space Complexity: O(26) = O(1)
        '''
        max_length = 0
        for l in range(len(s)):
            char_set = set() #like a map with one element
            # set is a collection of items that are unique
            # char set is a set of characters, and we only have 26 characters
            for r in range(l, len(s)):
                if s[r] in char_set:
                    break
                else:
                    char_set.add(s[r])
                    max_length=max(max_length,len(char_set))
        return max_length
        '''    

        #More Efficient Sliding Window Method
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        l, r, max_len = 0,0,0
        char_set = set() # keeps track of all char between l and r
        
        #while condition for sliding window algo
        while r < len(s):
            #if char is already in char_set, we remove it from set and increase l by one
            #this essentially resets the substring search
            if s[r] in char_set:
                char_set.remove(s[l])
                l+=1
            #otherwise, add char to set and update max if necessary
            else:
                char_set.add(s[r])
                max_len = max(max_len, len(char_set))
                r+=1
        
        return max_len