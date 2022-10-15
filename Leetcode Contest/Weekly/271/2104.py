# 2104. Sum of Subarray Ranges
# https://leetcode.com/problems/sum-of-subarray-ranges/

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        
        for i in range(n):
            smallest = largest = nums[i]
            for j in range(i + 1, n):
                smallest = min(smallest, nums[j])
                largest = max(largest, nums[j])
                
                res += largest - smallest
        
        return res
