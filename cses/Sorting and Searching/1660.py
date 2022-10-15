n, target = map(int,input().split())
arr = list(map(int,input().split()))

dic = {0:1}
s = 0
res = 0

for num in arr:
    s += num
    res += dic.get(s-target, 0)
    dic[s] = dic.get(s,0) + 1

print(res)