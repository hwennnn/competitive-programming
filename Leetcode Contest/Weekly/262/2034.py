# 2034. Stock Price Fluctuation 
# https://leetcode.com/problems/stock-price-fluctuation/

from sortedcontainers import SortedList
​
class StockPrice:
​
    def __init__(self):
        self.sl = SortedList()
        self.records = collections.defaultdict(int)
        self.t = -1
        
    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.records:
            self.sl.remove(self.records[timestamp])
        self.records[timestamp] = price
        self.sl.add(price)
        self.t = max(self.t, timestamp)
​
    def current(self) -> int:
        return self.records[self.t]
​
    def maximum(self) -> int:
        return self.sl[-1]
​
    def minimum(self) -> int:
        return self.sl[0]
​
​
# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
