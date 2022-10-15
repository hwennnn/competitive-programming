# 1268. Search Suggestions System
# https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products: List[str], word: str) -> List[List[str]]:
        res = []
        mp = collections.defaultdict(list)
        n = len(word)
        
        for i in range(n):
            w = word[:i+1]
            for p in products:                
                if i < len(p) and p[:i+1] == w:
                    mp[i].append(p) 
        
        for key in range(n):
            results = sorted(mp[key])
            tmp = []
            for i in range(min(3, len(results))):
                tmp.append(results[i])
            res.append(tmp)
        
        return res