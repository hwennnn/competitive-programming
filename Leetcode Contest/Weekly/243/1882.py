# 1882. Process Tasks Using Servers
# https://leetcode.com/problems/process-tasks-using-servers/

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(tasks)
        queue = []
        
        for i,x in enumerate(servers):
            queue.append((x, i))
        
        heapq.heapify(queue)
        
        running = []
        res = []
        i = t = 0
        
        while t < n:
            while running and running[0][0] <= i:
                _, capacity, index = heapq.heappop(running)
                heapq.heappush(queue, (capacity, index))
            
            while t < n and queue and i >= t:
                capacity, index = heapq.heappop(queue)
                res.append(index)
​
                heapq.heappush(running, (i + tasks[t], capacity, index))
                t += 1
​
            i = i + 1 if queue else running[0][0]
            
        return res
