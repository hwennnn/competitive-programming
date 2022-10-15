# 2406. Divide Intervals Into Minimum Number of Groups
# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        minHeap = []
        
        for s, e in intervals:
            if minHeap and s > minHeap[0]:
                heappop(minHeap)
            
            heappush(minHeap, e)
        
        return len(minHeap)
