# 1944. Number of Visible People in a Queue
# https://leetcode.com/problems/number-of-visible-people-in-a-queue/

from sortedcontainers import SortedList
​
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [1] * (n - 1) + [0]
        sl = SortedList()
        mp = collections.defaultdict(int)
        
        for i, h in list(enumerate(heights))[::-1]:
            index = sl.bisect_left(h)
​
            if sl:
                res[i] = max(1, min(len(sl), index + 1))
            
            if i + 1 < n and h > heights[i + 1]:
                for _ in range(index):
                    sl.pop(0)
                    
            sl.add(h)  
            mp[h] = i
            
        return res
