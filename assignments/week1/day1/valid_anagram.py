class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hashmap solution: time complexity O(2n)?; not sure about space complexity

        #anagrams must be the same length, so return false if not
        if len(s) != len(t):
            return False
        
        #create two hashmaps to store the characters of each string
        map_s = {}
        map_t = {}

        #zip() method allows us to iterate through s and t at the same time
        #this effect can also be achieved through range() function
        #if char is in map, increase the count. else start at count 1
        for ch_s, ch_t in zip(s,t):
            if ch_s in map_s:
                map_s[ch_s] += 1
            else:
                map_s[ch_s] = 1

            if ch_t in map_t:
                map_t[ch_t] += 1
            else:
                map_t[ch_t] = 1

        #len has to be the same
        #if some character is not in both or counts are different, not anagram: return false
        for i in map_s.keys():
            if i not in map_t.keys() or map_s[i] != map_t[i]:
                return False
        return True