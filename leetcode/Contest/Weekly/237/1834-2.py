# 1834. Single-Threaded CPU
# https://leetcode.com/problems/single-threaded-cpu

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks = sorted([(a, b, i) for i, (a,b) in enumerate(tasks)])
        t = tasks[0][0]
        heap = []
        res = []
        i = 0
        
        while len(res) < n:
            while i < n and tasks[i][0] <= t:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if heap:
                time, ki = heapq.heappop(heap)
                t += time
                res.append(ki)
            elif i < n:
                t = tasks[i][0]
        
        return res
