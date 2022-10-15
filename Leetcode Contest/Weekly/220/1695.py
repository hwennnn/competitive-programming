# 1695. Maximum Erasure Value
# https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        c = collections.Counter()
        j = curr = res = 0
        
        for i,x in enumerate(nums):
            curr += x
            c[x] += 1
            
            if c[x] == 2:
                while c[x] > 1:
                    curr -= nums[j]
                    c[nums[j]] -= 1
                    j += 1
            
            res = max(res, curr)
        
        return res
            
        