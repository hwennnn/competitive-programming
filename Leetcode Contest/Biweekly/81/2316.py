# 2316. Count Unreachable Pairs of Nodes in an Undirected Graph
# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class DSU:
    def __init__(self, n):
        self.graph = list(range(n))
​
    def find(self, x):
        if self.graph[x] != x:
            self.graph[x] = self.find(self.graph[x])
​
        return self.graph[x]
​
    def union(self, x, y):
        ux, uy = self.find(x), self.find(y)
        self.graph[ux] = uy
​
    def connected(self, x, y):
        return self.find(x) == self.find(y)
​
    def disconnect(self, x):
        self.graph[x] = x
​
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        
        for a, b in edges:
            dsu.union(a, b)
        
        parents = [0] * n
        
        for node in range(n):
            p = dsu.find(node)
            parents[p] += 1
        
        res = 0
        
        for node in range(n):
            p = dsu.find(node)
            res += n - parents[p]
        
        return res // 2
