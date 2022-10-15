# 2006. Count Number of Pairs With Absolute Difference K
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) == k:
                    res += 1
        
        return res
