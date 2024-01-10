class Solution:
    def isValid(self, s: str) -> bool:
        #good problem to introduce stacks
        #valid parentheses are always palindromes

        #create a map to organize all the information
        close_to_open={'}': '{', ']': '[', ')': '('}
        #create a stack: use list to replicate stack
        stack = []

        #iterate through string
        for c in s:
            if c in close_to_open.values():
                stack.append(c)
            #check top of the stack
            elif stack and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                return False
        
        return not stack