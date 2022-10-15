# 2310. Sum of Numbers With Units Digit K
# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0: return 0
        
        A = []
        INF = 100000
        
        for x in range(k, num + 10, 10):
            A.append(x)
​
        A.reverse()
        
        @cache
        def go(index, total):
            if index >= len(A):
                return INF
            
            if total > num:
                return INF
            
            if total == num:
                return 0
            
            # skip current
            res = go(index + 1, total)
            
            # take current
            if A[index] > 0:
                res = min(res, 1 + go(index, total + A[index]))
            
            return res
        
        ans = go(0, 0)
        if ans == 100000:
            return -1
        
        return ans
            
                
