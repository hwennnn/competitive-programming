# 1018. Binary Prefix Divisible By 5
# https://leetcode.com/problems/binary-prefix-divisible-by-5/

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        prev = 0
        res = []
        
        for x in nums:
            prev = prev * 2 + x
            res.append(prev % 5 == 0)
        
        return res
