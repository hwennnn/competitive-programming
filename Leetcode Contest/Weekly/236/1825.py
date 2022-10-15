# 1825. Finding MK Average
# https://leetcode.com/problems/finding-mk-average

class MKAverage:
​
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.A = []
​
    def addElement(self, num: int) -> None:
        self.A.append(num)
​
    def calculateMKAverage(self) -> int:
        if len(self.A) < self.m: return -1
        
        m, k = self.m, self.k
        A = self.A[:]
​
        if len(A) > m:
            A = self.A[len(A) - m:]
        A.sort()
        
        total = 0
        for i in range(k, len(A) - k):
            total += A[i]
​
        return total // (len(A) - 2 * k)
​
# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
