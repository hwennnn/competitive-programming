# 2289. Steps to Make Array Non-decreasing
# https://leetcode.com/problems/steps-to-make-array-non-decreasing

from sortedcontainers import SortedList
​
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('inf')]
        res = 0
        
        sl = SortedList([(i, x) for i, x in enumerate(nums)])
        p = set()
        
        for i, (a, b) in enumerate(zip(nums, nums[1:])):
            if a > b:
                p.add((i + 1, b))
                
        while p:
            newP = set()
            res += 1
            
            for j, b in p:
                index = sl.bisect_left((j, b))
                i, a = sl[index - 1]
                k, c = sl[index + 1]
                del sl[index]
                
                if a > c and (k, c) not in p:
                    newP.add((k, c))
            
            p = newP
        
        return res
