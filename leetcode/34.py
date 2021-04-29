# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        mp = collections.defaultdict(list)
        
        for i,x in enumerate(nums):
            mp[x].append(i)
​
        return [-1, -1] if len(mp[target]) == 0 else [mp[target][0], mp[target][-1]]
