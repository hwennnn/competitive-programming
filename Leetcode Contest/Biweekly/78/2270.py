# 2270. Number of Ways to Split Array
# https://leetcode.com/problems/number-of-ways-to-split-array/

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [0] + list(accumulate(nums))
        total = sum(nums)
        n = len(nums)
        res = 0
        
        for i in range(n - 1):
            left = prefix[i + 1]
            right = prefix[-1] - prefix[i + 1]
            
            if left >= right:
                res += 1
        
        return res
