# 2097. Valid Arrangement of Pairs
# https://leetcode.com/problems/valid-arrangement-of-pairs

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        din, dout = Counter(), Counter()
        
        for x, y in pairs:
            graph[x].append(y)
            dout[x] += 1
            din[y] += 1
        
        S = pairs[0][0]
        for x in dout:
            if dout[x] - din[x] == 1:
                S = x
                break
        
        stack = [S]
        routes = []
        
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            routes.append(stack.pop())
        routes.reverse()
        
        return [[routes[i], routes[i + 1]] for i in range(len(routes) - 1)]
