# 1862. Sum of Floored Pairs
# https://leetcode.com/problems/sum-of-floored-pairs

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        M, N = 10 ** 9 + 7, 10 ** 5 + 1
        res = mmax = 0
        prefix = [0] * (2 * N + 1)
        
        for x in nums:
            mmax = max(mmax, x)
            prefix[x] += 1
        
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]
        
        for num in nums:
            l, r, t = num, num * 2 - 1, 1
            
            while l <= mmax:
                res += (prefix[r] - prefix[l - 1]) * t
                l += num
                r += num
                t += 1
        
        return res % M
