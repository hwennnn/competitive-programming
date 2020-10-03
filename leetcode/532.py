# 532. K-diff Pairs in an Array
# https://leetcode.com/problems/k-diff-pairs-in-an-array/
    
import collections

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = collections.Counter(nums)
        res = 0
        
        for c in dic:
            if k == 0 and dic[c] > 1 or k > 0 and c+k in dic:
                res += 1
        
        return res 