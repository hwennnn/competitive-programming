# 1656. Design an Ordered Stream
# https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream:
    
    def __init__(self, n: int):
        self.arr = [None]*n
        self.ptr = 1

    def insert(self, id: int, value: str) -> List[str]:
        
        self.arr[id-1] = value
        res = []
        lastI = None

        for i in range(self.ptr-1, len(self.arr)):
            if self.arr[i] != None:
                res.append(self.arr[i])
                lastI = i
            else:
                break
        
        if len(res) > 0:
            self.ptr = lastI + 2
        
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)