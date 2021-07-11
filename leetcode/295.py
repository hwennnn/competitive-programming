# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream

from sortedcontainers import SortedList
​
class MedianFinder:
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sl = SortedList()
​
    def addNum(self, num: int) -> None:
        self.sl.add(num)
​
    def findMedian(self) -> float:
        n = len(self.sl)
        if n & 1:
            return self.sl[n // 2]
        else:
            return (self.sl[n // 2] + self.sl[n // 2 - 1]) / 2
​
​
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
