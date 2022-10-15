n = int(input())
arr = list(map(int,input().split()))

prefix = {0:1}
s = 0
res = 0

for num in arr:
    s += num
    if (s - n)%n in prefix:
        res += prefix[(s-n)%n]
    prefix[s%n] = prefix.get(s%n, 0) + 1

print(res)