# 2322. Minimum Score After Removals on a Tree
# https://leetcode.com/problems/minimum-score-after-removals-on-a-tree

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        N, M = len(nums), len(edges)
        
        graph = defaultdict(list)
        children = defaultdict(set)
        degree = [0] * N
        xor = nums.copy()
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        V = 0
        dq = deque()
        seen = set()
        
        for node in range(N):
            V ^= nums[node]
            
            if degree[node] == 1:
                dq.append(node)
                seen.add(node)
        
        while dq:
            node = dq.popleft()
            
            for nei in graph[node]:
                if nei not in seen:
                    children[nei].add(node)
                    children[nei] |= children[node]
                    xor[nei] ^= xor[node]
                
                degree[nei] -= 1
                
                if degree[nei] == 1 and len(seen) != N - 1:
                    seen.add(nei)
                    dq.append(nei)
        
        res = float('inf')
        
        for i in range(M - 1):
            for j in range(i + 1, M):
                a, b = edges[i]
                if b in children[a]: a, b = b, a
                
                c, d = edges[j]
                if d in children[c]: c, d = d, c
                
                if a in children[c]:
                    s = [xor[a], xor[c] ^ xor[a], V ^ xor[c]]
                elif c in children[a]:
                    s = [xor[c], xor[a] ^ xor[c], V ^ xor[a]]
                else:
                    s = [xor[c], xor[a], V ^ xor[c] ^ xor[a]]
                
                res = min(res, max(s) - min(s))
        
        return res
