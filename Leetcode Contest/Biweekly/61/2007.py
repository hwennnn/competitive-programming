# 2007. Find Original Array From Doubled Array
# https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n & 1: return []
​
        res = []
        mp = Counter(changed)
        keys = sorted(mp.keys(), reverse = 1)
        
        for key in keys:
            if key % 2: continue
                
            if key == 0:
                res += [0] * (mp[key] // 2)
            else:
                count = min(mp[key], mp[key // 2])
                mp[key] -= count
                mp[key // 2] -= count
                res += [key // 2] * count
                    
        return res if len(res) == n // 2 else []
