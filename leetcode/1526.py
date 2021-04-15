# 1526. Minimum Number of Increments on Subarrays to Form a Target Array
# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = x = target[0]
        
        for num in target:
            if num <= x:
                x = num
            else:
                res += num - x
                x = num
        
        return res
