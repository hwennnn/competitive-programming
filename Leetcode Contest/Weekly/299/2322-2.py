# 2322. Minimum Score After Removals on a Tree
# https://leetcode.com/problems/minimum-score-after-removals-on-a-tree

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        N, M = len(nums), len(edges)
        
        graph = defaultdict(list)
        V = 0
        
        for node in range(N):
            V ^= nums[node]
            
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        children = defaultdict(set)
        seen = set([0])
        xor = nums.copy()
        
        def go(node):
            for nei in graph[node]:
                if nei in seen: continue
                seen.add(nei)
                go(nei)
                children[node].add(nei)
                children[node] |= children[nei]
                xor[node] ^= xor[nei]
        
        go(0)
        
        res = float('inf')
        
        for i in range(M - 1):
            for j in range(i + 1, M):
                a, b = edges[i]
                
                if b in children[a]:
                    a, b = b, a
                
                c, d = edges[j]
                
                if d in children[c]:
                    c, d = d, c
                
                if a in children[c]:
                    curr = [xor[a], xor[c] ^ xor[a], V ^ xor[c]]
                elif c in children[a]:
                    curr = [xor[c], xor[a] ^ xor[c], V ^ xor[a]]
                else:
                    curr = [xor[c], xor[a], V ^ xor[c] ^ xor[a]]
                
                res = min(res, max(curr) - min(curr))
        
        return res
