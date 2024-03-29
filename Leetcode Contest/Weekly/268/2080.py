# 2080. Range Frequency Queries
# https://leetcode.com/problems/range-frequency-queries/

class RangeFreqQuery:
​
    def __init__(self, arr: List[int]):
        self.mp = collections.defaultdict(list)
        for i, x in enumerate(arr):
            self.mp[x].append(i)
​
    def query(self, left: int, right: int, value: int) -> int:
        a = bisect.bisect_left(self.mp[value], left)
        b = bisect.bisect_right(self.mp[value], right)
        
        return b - a
        
​
​
# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
