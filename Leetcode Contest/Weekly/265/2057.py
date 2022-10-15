# 2057. Smallest Index With Equal Value
# https://leetcode.com/problems/smallest-index-with-equal-value/

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, x in enumerate(nums):
            if i % 10 == x:
                return i
            
        return -1
