from collections import defaultdict

N = int(input())
graph = defaultdict(list)
starts = set()

for _ in range(N):
    start, end = map(int, input().split())
    graph[start].append(end)
    starts.add(start)

res = 0
visited = set()

for start in starts:
    if start in visited:
        continue

    seen = set()
    loops = set()

    def dfs(x):
        seen.add(x)

        for nei in graph[x]:
            if nei in seen:
                loops.add(x)
            else:
                dfs(nei)

    dfs(start)

    for s in seen:
        if s not in loops:
            visited.add(s)

    res += 1

print(res)


'''
Test case 1

4 
1 2
2 3
3 1
3 4

=> 2

Test case 2

7
1 2
2 3
3 1
4 2
4 3
3 5
2 5

=> 2
'''
