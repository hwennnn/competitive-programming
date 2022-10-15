# 2266. Count Number of Texts
# https://leetcode.com/problems/count-number-of-texts/

class Solution:
    def countTexts(self, A: str) -> int:
        n = len(A)
        M = 10 ** 9 + 7
        
        @cache
        def go(i):
            if i == n: return 1
            
            res = go(i + 1)
            
            if A[i] in "79":
                for k in range(i + 1, min(n, i + 4)):
                    if A[k] == A[i]:
                        res += go(k + 1)
                    else:
                        break
            else:
                for k in range(i + 1, min(n, i + 3)):
                    if A[k] == A[i]:
                        res += go(k + 1)
                    else:
                        break
                
            return res % M
        
        return go(0)
                
            
            
