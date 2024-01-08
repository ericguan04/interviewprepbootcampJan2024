class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window
        l, max_len = 0,0
        char_count = {} # counting frequency of each character seen within the window

        for r in range(len(s)):
            char_count[s[r]] = 1+char_count.get(s[r],0)

            if (r-l+1) - max(char_count.values()) > k:
                char_count[s[l]]-=1
                l+=1

            max_len = max(max_len, r-l+1)
        return max_len
