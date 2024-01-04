class Solution:
    def isPalindrome(self, s: str) -> bool:
        #less efficient method since we go through entire string twice
        #Time complexity: O(n)
        #Space complexity: O(n)
        '''
        s1="" #create a new string that has all lower and is alphanumeric
        for c in s:
            if c.isalnum():
                s1+c.lower()
        return s1==s1[::-1] #slicing to reverse the string
        '''

        #two pointer method: time complexity O(n/2)
        #constant space complexity: O(1)
        #since we only go through half of the string at worst case
        
        #create two pointers
        start = 0
        end = len(s)-1

        #uses a while loop to make sure pointers don't cross each other
        #idea: ignore all non alphanumeric characters and see if characters equal each other
        #if not, return False
        #after loop, return True meaning all characters equal
        while start < end:
            if s[start].isalnum():
                if s[end].isalnum():
                    if s[start].lower() != s[end].lower():
                        return False
                    else:
                        start+=1
                        end-=1
                else:
                    end-=1
            else:
                start+=1

        return True