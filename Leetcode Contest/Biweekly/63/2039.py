# 2039. The Time When the Network Becomes Idle
# https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = collections.defaultdict(list)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        res = 0
        queue = collections.deque([(0, 0)])
        seen = set([0])
        
        while queue:
            x, distance = queue.popleft()
            p = patience[x]
            
            if x != 0:
                firstTimeReceive = 2 * distance
                numOfResend = (firstTimeReceive - 1) // p
                res = max(res, firstTimeReceive + numOfResend * p)
            
            for y in graph[x]:
                if y not in seen:
                    seen.add(y)
                    queue.append((y, distance + 1))
        
        return res + 1
