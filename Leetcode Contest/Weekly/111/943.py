# 943. Find the Shortest Superstring
# https://leetcode.com/problems/find-the-shortest-superstring/

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        
        def distance(s1, s2):
            for i in range(1, len(s1)):
                if s2.startswith(s1[i:]):
                    return len(s1) - i + 1
            
            return 1
        
        n = len(words)
        weights = [[0] * n for _ in range(n)]
        dp = [[0] * n for _ in range(1 << n)]
        queue = deque([(0, i, 1 << i, [i]) for i in range(n)])
        full_mask = (1 << n) - 1
        maxWeight, maxPath = -1, []
        
        for i in range(n):
            for j in range(i, n):
                weights[i][j] = distance(words[i], words[j])
                weights[j][i] = distance(words[j], words[i])
        
        while queue:
            w, node, mask, path = queue.popleft()
            
            if dp[mask][node] != w:
                continue
            
            if mask == full_mask and w > maxWeight:
                maxWeight = w
                maxPath = path
                continue
            
            for nei in range(n):
                if mask & (1 << nei) > 0: continue
                
                new_mask = mask | (1 << nei)
                old = dp[new_mask][nei]
                new = dp[mask][node] + weights[node][nei]
                
                if new > old:
                    dp[new_mask][nei] = new
                    queue.append((new, nei, new_mask, path + [nei]))
        
        res = words[maxPath[0]]
        
        for i in range(1, n):
            prev, curr = maxPath[i - 1], maxPath[i]
            overlap = weights[prev][curr] - 1
            res += words[curr][overlap:]
            
        return res
            
