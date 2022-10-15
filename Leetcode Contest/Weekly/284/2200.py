# 2200. Find All K-Distant Indices in an Array
# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        indices = [i for i, x in enumerate(nums) if x == key]
        res = []
        
        for i in range(n):
            for j in indices:
                if abs(i - j) <= k:
                    res.append(i)
                    break
        
        return res
