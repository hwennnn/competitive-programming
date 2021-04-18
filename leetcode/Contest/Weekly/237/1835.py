# 1835. Find XOR Sum of All Pairs Bitwise AND
# https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xora = xorb = 0
        
        for num in arr1:
            xora ^= num
        
        for num in arr2:
            xorb ^= num
        
        return xora & xorb
