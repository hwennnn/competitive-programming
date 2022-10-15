# 1288. Remove Covered Intervals
# https://leetcode.com/problems/remove-covered-intervals/

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)
        res = 0
        
        for i in range(n):
            a,b = intervals[i]
            check = True
            for j in range(n):
                if i != j:
                    c,d = intervals[j]
                    
                    if c <= a and b <= d: 
                        check = False
                        break
            
            if check: res += 1
        
        return res

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = right = 0
        
        intervals.sort(key = lambda x:(x[0],-x[1]))
        
        for start,end in intervals:
            res += end > right
            right = max(right, end)
        
        return res