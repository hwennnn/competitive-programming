# 1239. Maximum Length of a Concatenated String with Unique Characters
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution:
    def maxLength(self, A: List[str]):
        dp = [set()]
        
        for a in A:
            if len(set(a)) < len(a): continue
            
            a = set(a)
            for b in dp[:]:
                if a & b: continue
                dp.append(a | b)
            
            
        return max(len(a) for a in dp)

    def maxLength(self, arr: List[str]):
        n = len(arr)
        res = 0
        
        for i in range(1 << n):
            tmp = ""
            for j in range(n):
                if i >> j & 1:
                    tmp += arr[j]
            
            c = Counter(tmp)
            if all(v == 1 for v in c.values()):
                res = max(res, len(tmp))
            
        return res