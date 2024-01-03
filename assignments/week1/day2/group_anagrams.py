from ast import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap + sorting method: time complexity O(m*nlog(n))
        #since we have to sort (nlog(n)) every string (m)
        map = {}

        #because sorted anagrams are always the same, we simple sort all the values
        #sorted string will be the key and values will be a list of all anagrams
        for str in strs:
            #standard way to sort strings in python
            sort = "".join(sorted(str))
            #if sorted string matches, add it to key
            if sort in map:
                map[sort] += [str]
            #create first instance
            else:
                map[sort] = [str]

        #convert values to list and return
        return list(map.values())