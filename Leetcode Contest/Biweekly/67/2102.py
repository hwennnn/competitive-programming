# 2102. Sequentially Ordinal Rank Tracker
# https://leetcode.com/problems/sequentially-ordinal-rank-tracker

from sortedcontainers import SortedSet, SortedList
​
class SORTracker:
​
    def __init__(self):
        self.scores = SortedSet()
        self.places = collections.defaultdict(SortedList)
        self.q = 0
​
    def add(self, name: str, score: int) -> None:
        self.scores.add(-score)
        self.places[score].add(name)
​
    def get(self) -> str:
        count = 0
        
        for score in self.scores:
            if count + len(self.places[-score]) < self.q: 
                count += len(self.places[-score])
                continue
                
            for name in self.places[-score]:
                if count == self.q:
                    self.q += 1
                    return name
                
                count += 1
        
        
# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
