# 1282. Group the People Given the Group Size They Belong To
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution:
    def groupThePeople(self, arr: List[int]) -> List[List[int]]:
        mp = collections.defaultdict(list)
        
        for i,x in enumerate(arr):
            mp[x].append(i)
        
        res = []
        
        for key in mp:
            groups = mp[key]
            n = len(groups)
            
            if n == key:
                res.append(groups)
            else:
                for i in range(0, n, key):
                    res.append(groups[i:i+key])
        
        return res