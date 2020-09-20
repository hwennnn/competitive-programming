# 1589. Maximum Sum Obtained of Any Permutation
# https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/

# Suffix sum version (sweep line) or "Lazy propagation"
class Solution:
    def maxSumRangeQuery(self, A: List[int], R: List[List[int]]) -> int:
        mod = 1000000007
        n = len(A)
        count = [0] * (n+1)
        
        for s,e in R:
            count[s] += 1
            count[e+1] -= 1
        
        for i in range(1, n+1):
            count[i] += count[i-1]
        
        count = sorted(count[:-1])
        A = sorted(A)
        
        res = 0
        for i, v in zip(count, A):
            res += i*v
            
        return res % mod
        
        
# TLE Version
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        
        d = {}
        m = 1000000007
        
        for r in requests:
            for i in range(r[0], r[1]+1):
                d[i] = d.get(i,0) + 1
        
        d = sorted(d.items(), key=lambda x: -x[1])
        nums.sort(reverse=True)

        res = 0
        i = 0
        for r in d:
            res += nums[i] * r[1]
            i+=1
        
        return res%m