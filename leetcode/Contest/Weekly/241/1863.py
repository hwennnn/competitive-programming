# 1863. Sum of All Subset XOR Totals
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        
        for i in range(1 << n):
            t = 0
            for j in range(n):
                if i >> j & 1:
                    t ^= nums[j]
​
            res += t
        
        return res
