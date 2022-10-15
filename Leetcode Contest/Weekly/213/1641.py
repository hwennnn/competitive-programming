# 1641. Count Sorted Vowel Strings
# https://leetcode.com/problems/count-sorted-vowel-strings/

# bfs
class Solution:
    def countVowelStrings(self, n: int) -> int:

        if n == 1: return 5
        mp = {"a":0, "e":1, "i":2, "o":3, "u":4}
        v = ["a","e","i","o","u"]
        deq = collections.deque(v)
        
        res = 0
        while deq:
            c = deq.popleft()
            nc = len(c)
            if nc == n:
                break

            i = mp[c[-1]]
            if nc + 1 <= n:
                for j in range(i,len(v)):
                    if nc + 1 == n:
                        res += 1
                    else:
                        deq.append(c + v[j])
        return res
                
    # math dp
    def countVowelStrings(self, n: int) -> int:
        
        a = e = i = o = u = 1
        
        for _ in range(n-1):
            a, e ,i, o, u = a+e+i+o+u, e+i+o+u , i+o+u, o+u, u
        
        return a+e+i+o+u