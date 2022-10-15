# 2192. All Ancestors of a Node in a Directed Acyclic Graph
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [[] for _ in range(n)]
        graph = collections.defaultdict(list)
        
        for x, y in edges:
            graph[y].append(x)
        
        for i in range(n):
            stack = [i]
            visited = set()
            
            while stack:
                node = stack.pop()
                
                for anc in graph[node]:
                    if anc in visited: continue
                    visited.add(anc)
                    stack.append(anc)
                    res[i].append(anc)
            
            res[i].sort()
        
        return res
