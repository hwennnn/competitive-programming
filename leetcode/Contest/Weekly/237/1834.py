# 1834. Single-Threaded CPU
# https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        available = collections.defaultdict(list)
        t = float('inf')
        
        for i, (a,b) in enumerate(tasks):
            available[a].append((b, i))
            t = min(t, a)
        
        res = []
        heap = []
        ki = 0
        kn = len(available)
        keys = list(available.keys())
        keys.sort()
​
        while len(res) != n:
            isUpdated = False
            while ki < kn and keys[ki] <= t:
                new = available[keys[ki]]
                for at in new:
                    heap.append(at)
                isUpdated = True
                ki += 1
            
            if isUpdated:
                heapq.heapify(heap)
            
            if ki == kn:
                while heap:
                    time, i = heapq.heappop(heap)
                    res.append(i)
            else:
                if heap:
                    time, i = heapq.heappop(heap)
                    t += time
                    res.append(i)
                else:
                    t = keys[ki]
        
        return res
