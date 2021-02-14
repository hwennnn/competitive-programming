# 785. Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    # dfs
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def dfs(i):
            for nei in graph[i]:
                if nei in coloured:
                    if coloured[nei] == coloured[i]:
                        return False
                else:
                    coloured[nei] = -coloured[i]
                    if not dfs(nei):
                        return False
            
            return True
                    
                   
        coloured = {}
        
        for i in range(len(graph)):
            if i not in coloured:
                coloured[i] = 1
                if not dfs(i):
                    return False
        
        return True
    
    # bfs
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
