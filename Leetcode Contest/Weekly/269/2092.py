# 2092. Find All People With Secret
# https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        m = len(meetings)
        known = set([0])
        times = collections.defaultdict(list)
        
        for x, y, t in meetings:
            times[t].append((x, y))
        times[0].append((0, firstPerson))
        
        keys = sorted(times.keys())
        
        for t in keys:
            propagate = set()
            met = collections.defaultdict(set)
            
            for x, y in times[t]:
                if x in known:
                    propagate.add(x)
                if y in known:
                    propagate.add(y)
                    
                met[x].add(y)
                met[y].add(x)
            
            stack = list(propagate)
            while stack:
                x = stack.pop()
                
                for people in met[x]:
                    if people in propagate: continue
                    propagate.add(people)
                    known.add(people)
                    stack.append(people)
            
        return list(known)
        
