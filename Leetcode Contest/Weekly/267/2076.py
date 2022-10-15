# 2076. Process Restricted Friend Requests
# https://leetcode.com/problems/process-restricted-friend-requests

class DSU:
    def __init__(self, n):
        self.graph = list(range(n))
    
    def find(self, x):
        if self.graph[x] != x:
            self.graph[x] = self.find(self.graph[x])
        
        return self.graph[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        
        self.graph[px] = py
​
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        res = []
        
        for x, y in requests:
            px, py = dsu.find(x), dsu.find(y)
            valid = True
            
            for a, b in restrictions:
                pa, pb = dsu.find(a), dsu.find(b)
                
                if set([pa, pb]) == set([px, py]):
                    valid = False
                    break
            
            res.append(valid)
            if valid:
                dsu.union(x, y)
        
        return res
