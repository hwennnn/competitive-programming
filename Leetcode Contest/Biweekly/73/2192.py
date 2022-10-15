# 2192. All Ancestors of a Node in a Directed Acyclic Graph
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        visited = collections.defaultdict(set)
        
        def go(node):
            if node in visited: return visited[node]
​
            parents = set()
            if node in graph:
                for parent in graph[node]:
                    parents.add(parent)
                    parents |= go(parent)
​
            visited[node] = parents
            return parents
​
        
        for x, y in edges:
            graph[y].append(x)
​
        for node in graph:
            if node not in visited:
                go(node)
        
        res = []
        
        for i in range(n):
            res.append(sorted(list(visited[i])))
        
        return res
        
