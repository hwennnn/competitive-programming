# 2102. Sequentially Ordinal Rank Tracker
# https://leetcode.com/problems/sequentially-ordinal-rank-tracker

from sortedcontainers import SortedList
​
class SORTracker:
    def __init__(self):
        self.sl = SortedList()
        self.counter = 0
​
    def add(self, name: str, score: int) -> None:
        self.sl.add((-score, name))
​
    def get(self) -> str:
        ans = self.sl[self.counter][1]
        self.counter += 1
        return ans
​
# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
