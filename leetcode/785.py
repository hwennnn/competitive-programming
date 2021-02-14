# 785. Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        coloured = {}
        
        for i in range(n):
            if i not in coloured:
                coloured[i] = 1
                
                queue = collections.deque([i])
                
                while queue:
                    node = queue.popleft()
                    for nei in graph[node]:
                        if nei not in coloured:
                            coloured[nei] = -coloured[node]
                            queue.append(nei)
                        elif coloured[nei] == coloured[node]:
                            return False
        
        return True
