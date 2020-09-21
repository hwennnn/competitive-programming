# 1590. Make Sum Divisible by P
# https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, A, p):
        #find the remainder
        need = sum(A) % p 
        
        # Subproblem : find the minimum subarray with the sum of remainder
        dic = {0:-1}
        n = res = len(A)
        c = 0
        
        for i, val in enumerate(A):
            c = (c + val) % p
            dic[c] = i
            if (c-need) % p in dic:
                res = min(res, i - dic[(c-need)%p])
            
        return res if res != n else -1
        
            