# 729. My Calendar I
# https://leetcode.com/problems/my-calendar-i/

class MyCalendar:
​
    def __init__(self):
        self.intervals = []   
​
    def book(self, start: int, end: int) -> bool:
        
        for s,e in self.intervals:
            if not (start >= e or end <= s): return False
​
        self.intervals.append((start, end))
        
        return True
​
​
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
