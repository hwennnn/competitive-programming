# 784. Letter Case Permutation
# https://leetcode.com/problems/letter-case-permutation

class Solution:
    # backtracking
    def letterCasePermutation(self, S: str):
        res = []
        n = len(S)
        
        def backtrack(i, s):
            if i == n: 
                res.append("".join(s))
                return
            
            if s[i].isalpha():
                s[i] = s[i].upper()
                backtrack(i+1, s)
                
                s[i] = s[i].lower()
                backtrack(i+1, s)
            
            else:
                backtrack(i+1, s)
        
        backtrack(0, list(S))
        
        return res
    
    # bitmask
    def letterCasePermutation(self, S: str):
        n = len(S)
        res = set()
        
        for i in range(1<<n):
            s = list(S)
            for j in range(n):
                if i >> j & 1:
                    s[j] = s[j].upper()
                else:
                    s[j] = s[j].lower()
            
            res.add("".join(s))
                
        return list(res)
