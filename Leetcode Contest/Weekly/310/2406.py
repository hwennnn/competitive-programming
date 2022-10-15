# 2406. Divide Intervals Into Minimum Number of Groups
# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

from sortedcontainers import SortedList
​
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        sl = SortedList(intervals)
        res = 0
        
        while len(sl) > 0:
            s, e = sl[0]
            nextStart = e + 1
            index = sl.bisect_left([nextStart, ])
            
            while index < len(sl):
                ns, ne = sl[index]
                nextStart = ne + 1
                sl.remove([ns, ne])
                index = sl.bisect_left([nextStart, ])
                
            sl.remove([s, e])
            res += 1
            
        return res
