# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:
​
    def __init__(self, k: int):
        self.n = k
        self.deq = collections.deque()
​
    def enQueue(self, value: int) -> bool:
        m = not self.isFull()
        if m:
            self.deq.append(value)
        return m
​
    def deQueue(self) -> bool:
        m = not self.isEmpty()
        if m:
            self.deq.popleft()
        return m
​
    def Front(self) -> int:
        m = not self.isEmpty()
        return self.deq[0] if m else -1
​
    def Rear(self) -> int:
        m = not self.isEmpty()
        return self.deq[-1] if m else -1
​
    def isEmpty(self) -> bool:
        return len(self.deq) == 0
​
    def isFull(self) -> bool:
        return len(self.deq) >= self.n
​
​
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
