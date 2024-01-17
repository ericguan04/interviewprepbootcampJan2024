from ast import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #time complexity: O(n*4^n)
        #space complexity: O(n*4^n)
        
        #backtracking question: permutation question

        combos = []
        digit_to_char = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
                        '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        def backtrack(i, curr_str):
            if i == len(digits):
                combos.append(curr_str)
                return
            
            for c in digit_to_char[digits[i]]:
                backtrack(i+1, curr_str+c)

        if digits:
            backtrack(0,'')
        return combos