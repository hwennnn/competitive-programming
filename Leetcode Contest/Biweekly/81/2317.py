# 2317. Maximum XOR After Operations 
# https://leetcode.com/problems/maximum-xor-after-operations/

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        res = 0
        
        for x in nums:
            res |= x
        
        return res
            
