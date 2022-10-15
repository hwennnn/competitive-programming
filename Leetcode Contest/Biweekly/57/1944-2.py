# 1944. Number of Visible People in a Queue
# https://leetcode.com/problems/number-of-visible-people-in-a-queue

from sortedcontainers import SortedList
​
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        heights.reverse()
        res = []
        sl = SortedList()
        
        for h in heights:
            res.append(min(len(sl), sl.bisect_left(h) + 1))
            
            while sl and h > sl[0]:
                sl.pop(0)
            
            sl.add(h)
            
        return res[::-1]
