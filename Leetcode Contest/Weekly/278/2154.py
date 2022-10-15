# 2154. Keep Multiplying Found Values by Two
# https://leetcode.com/problems/keep-multiplying-found-values-by-two/

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)
        res = original
        found = res in s
        
        while found:
            res *= 2
            found = res in s
        
        return res
