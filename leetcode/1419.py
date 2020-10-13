# 1419. Minimum Number of Frogs Croaking
# https://leetcode.com/problems/minimum-number-of-frogs-croaking/

class Solution:
    def minNumberOfFrogs(self, S: str) -> int:
        dic = {"c","r","o","a","k"}
        
        c = m = 0
        peak = 0
        for s in S:
            added = False
            if s == "c":
                m += 1
                c += 4
                added = True
            
            else:
                c -= 1
            
            if s == "k":
                m -= 1

            if c < 0:
                return -1
            
            peak = max(peak, m)

        mp = collections.Counter(S)
        check = None
        for c in mp:
            if not check:
                check = mp[c]
            else:
                if mp[c] != check or c not in dic:
                    return -1
        
        return peak